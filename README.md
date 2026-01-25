# BareBones Template Modpack
BareBones is a template modpack for Minecraft 1.12.2 that aims to create a minimalistic standardized mod list that can be used as a base for new modpacks or a means of updating old modpacks to the new standards.

Effort was made to ensure that the only mods included in the template by default are those that provide significant QoL improvements, game optimizations, or bugfixes without directly affecting gameplay.

BareBones also includes a pre-configured Crash Assistant problematic mods config, allowing users to easily identify mods that cause significant issues, or those that are superseded by other mods within the pack.

This pack ***DOES NOT*** include any new content or gameplay modifications outside of minor tweaks present in Universal Tweaks.

This pack ***DOES NOT*** include any type of shader or lighting enhancement mods beyond those that directly improve performance.

---

## Installation Instructions
### Fresh Installations

### Modpack Updating


---

## Included Mods
- **[Advancement Locator](https://www.curseforge.com/minecraft/mc-mods/advancement-locator)** - A QoL mod that adds left click interaction to chat frame Advancements as well as an Advancement locator command.
- **[Alfheim Lighting Engine](https://www.curseforge.com/minecraft/mc-mods/alfheim-lighting-engine)** - A lighting engine replacement for Minecraft, optimized for performance and fixing many bugs. If you encounter issues with Alfheim, you can try using [燐/Hesperus](https://www.curseforge.com/minecraft/mc-mods/hesperus), though it is not recommended.
- **[CensoredASM](https://www.curseforge.com/minecraft/mc-mods/lolasm)** - A collection of large optimizations targeted at 1.12.2.
- **[ConfigAnytime](https://www.curseforge.com/minecraft/mc-mods/configanytime)** - A utility mod allowing early configuration loading. Used by Universal Tweaks and many other mods that modify Minecraft's code with mixins.
- **[Crash Assistant](https://www.curseforge.com/minecraft/mc-mods/crash-assistant)** - An advanced crash log handler with several important debugging tools. Used in the BareBones template to locate incompatible and depreciated mods.
- **[Fixeroo](https://www.curseforge.com/minecraft/mc-mods/xp-orb-clump)** - A collection of small fixes for Minecraft, most notably an improved implementation of the [Clumps](https://www.curseforge.com/minecraft/mc-mods/clumps) mod.
- **[Flare](https://www.curseforge.com/minecraft/mc-mods/flare)** - A performance profiler for 1.12.2 clients and servers based off of Spark.
- **[FPS Reducer](https://www.curseforge.com/minecraft/mc-mods/fps-reducer)** - Reduces CPU and GPU usage when the game window is inactive or minimized.
- **[Gnetum](https://www.curseforge.com/minecraft/mc-mods/gnetum)** - Improves performance in GUIs by distributing HUD updates over multiple frames.
- **[Had Enough Items](https://www.curseforge.com/minecraft/mc-mods/had-enough-items)** - An updated fork of JEI for 1.12.2 with optimizations and more features.
- **[JEI Area Fixer](https://www.curseforge.com/minecraft/mc-mods/jei-area-fixer)** - A collection of mod fixes to prevent GUI overlap with JEI/HEI.
- **[LemonSkin](https://www.curseforge.com/minecraft/mc-mods/lemonskin)** - An updated fork of AppleSkin, adding item food value tooltips and advanced hunger bar appearance.
- **[MixinBooter](https://www.curseforge.com/minecraft/mc-mods/mixin-booter)** - (Forge only) A standardized library used for bytecode manipulation. Required by most mods in this pack.
- **[Mouse Tweaks Unofficial](https://www.curseforge.com/minecraft/mc-mods/mouse-tweaks-unofficial)** - A continuation of MouseTweaks for Minecraft 1.12.2, adding improved mouse GUI interactions.
- **[Reach Fix](https://www.curseforge.com/minecraft/mc-mods/reach-fix)** - Fixes the reach distance attribute not applying to player and entity attacks. Also improves hitbox interpolation when attacking entities.
- **[Red Core](https://www.curseforge.com/minecraft/mc-mods/red-core)** - A library mod used by Alfheim Lighting Engine.
- **[SerializationIsBad](https://www.curseforge.com/minecraft/mc-mods/serializationisbad)** - (Forge only) Fixes a number of serious security vulnerabilities present in several mods.
- **[Sound Device Options](https://www.curseforge.com/minecraft/mc-mods/more-sound-config)** - A small mod that adds an option to switch the sound output device without reloading the game.
- **[StellarCore](https://www.curseforge.com/minecraft/mc-mods/stellarcore)** - A collection of tweaks, optimizations and fixes targeted at 1.12.2.
- **[Universal Tweaks](https://www.curseforge.com/minecraft/mc-mods/universal-tweaks)** - A community project to consolidate various bugfixes and tweaks into a single solution for Minecraft 1.12.2.
- **[VintageFix](https://www.curseforge.com/minecraft/mc-mods/vintagefix)** - An updated an improved version of FoamFix. Improves load times and RAM usage for Minecraft 1.12.2.

---

## Optional Mods
- **[Aqua Acrobatics](https://www.curseforge.com/minecraft/mc-mods/aqua-acrobatics)** - Backports 1.13+ swimming, crouching, and crawling. Also backports item floating, which may cause issues with some mods.
- **[Enchantment Descriptions](https://www.curseforge.com/minecraft/mc-mods/enchantment-descriptions)** - Adds descriptions to enchantments describing their effects. Supported by most, but not all, mods that add enchantments.
- **[Ender's Modpack Tweaks](https://www.curseforge.com/minecraft/mc-mods/ender-modpack-tweaks)** - A collection of modpack tweaks, most notably an updated enemy health bar render. Has a soft requirement for [AssetMover](https://www.curseforge.com/minecraft/mc-mods/assetmover) which may increase load times.
- **[Entity Culling (by tr7zw)](https://www.curseforge.com/minecraft/mc-mods/entityculling)** - Improves performance by hiding entities and tile entities that are not in the player's line of sight. May cause some tile entities to flicker. Performance increases may vary.
- **[FastEntityRender](https://github.com/Meldexun/FastEntityRender)** - Improves entity rendering performance. Mod has not been published to CurseForge and does not support shaders. 
- **[Inventory Bogo Sort](https://www.curseforge.com/minecraft/mc-mods/inventory-bogosorter)** - An updated and highly configurable inventory sorter. Requires [Key Binding Patch](https://www.curseforge.com/minecraft/mc-mods/key-binding-patch) which breaks existing keybind settings.
- **[JEI Utilities](https://www.curseforge.com/minecraft/mc-mods/jei-utilities)** - Adds a number of useful JEI functions such as view history and recipe bookmarks.
- **[Particle Culling](https://www.curseforge.com/minecraft/mc-mods/particle-culling)** - Prevents particles outside the player's view from rendering. May cause inconsistent particle behavior. Performance increases may vary.
- **[Packet Fixer](https://www.curseforge.com/minecraft/mc-mods/packet-fixer)** - Fixes a number of packet issues in Minecraft. Slight overlap with Universal Tweaks.
- **[Potion Descriptions (Forge)](https://www.curseforge.com/minecraft/mc-mods/potion-descriptions)** - Adds descriptions to potions describing their effects. Not as widely supported as Enchantment Descriptions.
- **[Raw Mouse Input - Blessed Edition](https://www.curseforge.com/minecraft/mc-mods/raw-mouse-input-blessed-edition)** - (Forge only) Makes Minecraft 1.12.2 use raw mouse input, making mouse input feel smoother.
- **[Roughly Enough IDs](https://www.curseforge.com/minecraft/mc-mods/reid)** - Extends the block, item, biome, potion, and enchantment ID limits. Required for large modpacks.
- **[ScalingGUIs](https://www.curseforge.com/minecraft/mc-mods/scalingguis)** - Decouples the scaling of individual GUIs, the HUD, and Tooltips. Extremely useful for anyone playing at resolutions higher than 1080p.
- **[Server Tab Info](https://www.curseforge.com/minecraft/mc-mods/server-tab-info)** - Adds a the mean tick time and ticks per second (TPS) to the server info tab. Extremely useful for detecting TPS lag on servers or single player worlds.
- **[ZS Packet](https://www.curseforge.com/minecraft/mc-mods/zs-packet)** - Improves client to server and server to client packet compression. Provides a very small performance increase when hundreds of packets are being generated every second (which is ***extremely*** rare).

---

## FAQ
<details>
  <summary>Why wasn't Optifine included?</summary>
  <blockquote>
    <p>
      Optifine for 1.12.2 is extremely outdated and no longer supported by the developers. It increases load times and can cause rendering issues with modded entities. It is not incompatible with the BareBones template, but it may require additional configuration. 
    </p>
    <p>
      If you do choose to include Optifine, be sure to also add <a href="https://www.curseforge.com/minecraft/mc-mods/optinotfine">OptiNotFine</a> to your modpack instance.
    </p>
  </blockquote>
</details>
<p>
<details>
  <summary>Why wasn't &#x3C;insert mod here&#x3E; included?</summary>
  <blockquote>
    <p>
      When it comes to optimizations and fixes there is a lot of misinformation in the community. Bad actors will describe massive performance gains while posting mods that do nothing (Performant) or actively make game performance worse (Frustum Culling).
    </p>
    <p>
      BareBones is configured to automatically detect the majority of these problematic mods, but you should always be wary of any mod describing itself as an "Optimization" or "Performance" mod.
    </p>
  </blockquote>
</details>
<p>
<details>
  <summary>Where can I find a list of updated mods and mod forks?</summary>
  <blockquote>
    <p>
      CleanroomMC maintains a incomplete, but constantly updated list of depreciated mods and their forks. You can find this list here: <a href="https://cleanroommc.com/wiki/end-user-guide/preparing-your-modpack">Preparing Your Modpack </a>
    </p>
  </blockquote>
</details>
