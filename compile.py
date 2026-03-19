#!/usr/bin/env python3
"""
Modpack Compiler
- Manifest -> Root
- Everything else -> overrides/

Outputs: build/<name> V<version>.zip
"""

import json
import zipfile
from pathlib import Path

# ── Config ────────────────────────────────────────────────────────────────────
ROOT = Path(__file__).parent
BUILD_DIR = ROOT / "build"
ROOT_ENTRIES = {"manifest.json"}
SKIP = {Path(__file__).name, "build", ".git", ".gitignore"}
# ─────────────────────────────────────────────────────────────────────────────


def get_zip_name() -> str:
    manifest_path = ROOT / "manifest.json"
    with manifest_path.open(encoding="utf-8") as f:
        manifest = json.load(f)
    name = manifest["name"]
    version = manifest["version"]
    return f"{name} V{version}.zip"


def add_to_zip(zf: zipfile.ZipFile, path: Path, arcname: str) -> None:
    if path.is_file():
        zf.write(path, arcname)
    elif path.is_dir():
        for child in sorted(path.rglob("*")):
            if child.is_file():
                rel = child.relative_to(path)
                zf.write(child, f"{arcname}/{rel}")


def build_zip() -> None:
    BUILD_DIR.mkdir(exist_ok=True)

    zip_name = get_zip_name()
    output = BUILD_DIR / zip_name

    entries = sorted(ROOT.iterdir())

    with zipfile.ZipFile(output, "w", zipfile.ZIP_DEFLATED) as zf:
        for entry in entries:
            name = entry.name

            if name in SKIP:
                continue

            if name in ROOT_ENTRIES:
                arc = name                       # zip root
            else:
                arc = f"overrides/{name}"        # overrides folder

            add_to_zip(zf, entry, arc)
            print(f"  {'[root]     ' if name in ROOT_ENTRIES else '[overrides]'} {arc}")

    print(f"\nCreated: {output}  ({output.stat().st_size / 1024:.1f} KB)")


if __name__ == "__main__":
    print(f" Building zip from: {ROOT}\n")
    build_zip()
