# BareBones Template Modpack (Forge)
BareBones is a template modpack for Minecraft 1.12.2 that aims to create a minimalistic standardized mod list that can be used as a base for new modpacks or a means of updating old modpacks to the new standards.

Effort was made to ensure that the only mods included in the template by default are those that provide significant QoL improvements, game optimizations, or bugfixes without directly affecting gameplay.

BareBones also includes a pre-configured Crash Assistant problematic mods config as well as the custom built PackCompanion mod, allowing users to easily identify mods that cause issues or are superseded by other mods.

This pack ***DOES NOT*** include any new content or gameplay modifications outside of minor tweaks present in Universal Tweaks.

This pack ***DOES NOT*** include any type of shader or lighting enhancement mods beyond those that directly improve performance.

---

## Installation Instructions
### Fresh Installations
<div class="spoiler">
  <blockquote>
    <ol>
      <li>Download or import the BareBones modpack into your preferred launcher.</li>
      <li>Add any desired mods from the 'Optional' section of this readme to the BareBones instance.</li>
      <li>Add any mods you want included in the modpack.</li>
      <li>
        Run the modpack.
        <ul>
          <li>If CrashAssistant notifies you of any problematic mods, remove them accordingly.</li>
          <li>If duplicate mod ids are found, remove any outdated versions.</li>
        </ul>
      </li>
      <li>Once the modpack has launched, either enter a new world and click the provided links in the chat window or navigate to <code>&#x3C;modpackinstance&#x3E;/config/packcompanion/outputs</code> and open the most recent <code>html</code> output log.</li>
      <li>The PackCompanion output features a list of recommended actions to ensure a stable modded environment. Follow the advised actions whenever possible.</li>
      <li>Once all changes have been made, delete or disable the PackCompanion mod.</li>
      <li>Launch the modpack and enjoy your updated instance!</li>
    </ol>
  </blockquote>
  </div>

### Modpack Updating
<div class="spoiler">
  <blockquote>
    <ol>
      <li>Download a new instance of the modpack you wish to update.</li>
      <li>
        Update the following mods to their most recent version if they are present.
        <ul>
          <li>Dynamic Surroundings</li>
          <li>Orelib</li>
        </ul>
      </li>
      <li>Create an instance of the BareBones pack template using your preferred launcher.</li>
      <li>Add any desired mods from the 'Optional' section of this readme to the BareBones instance.</li>
      <li>Copy the <code>config</code> and <code>mods</code> folders from the BareBones instance into the other modpack.</li>
      <li>
        Run the modpack.
        <ul>
          <li>If CrashAssistant notifies you of any problematic mods, remove them accordingly.</li>
        </ul>
      </li>
      <li>Once the modpack has launched, either enter a new world and click the provided links in the chat window or navigate to <code>&#x3C;modpackinstance&#x3E;/config/packcompanion/outputs</code> and open the most recent <code>html</code> output log.</li>
      <li>The PackCompanion output features a list of recommended actions to ensure a stable modded environment. Because some mod updates may break CraftTweaker scripts, it is advised to only update a few mods at a time. If errors occur, you can either update the scripts to reflect any changes or revert to the previous version of the mod.</li>
      <li>Once all changes have been made, delete or disable the PackCompanion mod.</li>
      <li>Launch the modpack and enjoy your updated instance!</li>
    </ol>
  </blockquote>
</div>

---

## Included Mods
* **[Advancement Locator](https://www.curseforge.com/minecraft/mc-mods/advancement-locator)** **(1.2.2)** - A QoL mod that adds left click interaction to chat frame Advancements as well as an Advancement locator command.
* **[Alfheim Lighting Engine](https://www.curseforge.com/minecraft/mc-mods/alfheim-lighting-engine)** **(1.6)** - A lighting engine replacement for Minecraft, optimized for performance and fixing many bugs. If you encounter issues with Alfheim, you can try using [燐/Hesperus](https://www.curseforge.com/minecraft/mc-mods/hesperus), though it is not recommended.
* **[CensoredASM](https://www.curseforge.com/minecraft/mc-mods/lolasm)** **(5.3.1)** - A collection of large optimizations targeted at 1.12.2.
* **[ConfigAnytime](https://www.curseforge.com/minecraft/mc-mods/configanytime)** **(3.0)** - A utility mod allowing early configuration loading. Used by Universal Tweaks and many other mods that modify Minecraft's code with mixins.
* **[Crash Assistant](https://www.curseforge.com/minecraft/mc-mods/crash-assistant)** **(1.11.6)** - An advanced crash log handler with several important debugging tools. Used in the BareBones template to locate incompatible and depreciated mods.
* **[Fixeroo](https://www.curseforge.com/minecraft/mc-mods/xp-orb-clump)** **(2.3.6)** - A collection of small fixes for Minecraft, most notably an improved implementation of the [Clumps](https://www.curseforge.com/minecraft/mc-mods/clumps) mod.
* **[Flare](https://www.curseforge.com/minecraft/mc-mods/flare)** **(0.7.0)** - A performance profiler for 1.12.2 clients and servers based off of Spark.
* **[FPS Reducer](https://www.curseforge.com/minecraft/mc-mods/fps-reducer)** **(1.20)** - Reduces CPU and GPU usage when the game window is inactive or minimized.
* **[Gnetum](https://www.curseforge.com/minecraft/mc-mods/gnetum)** **(1.3.5)** - Improves performance in GUIs by distributing HUD updates over multiple frames.
* **[Had Enough Items](https://www.curseforge.com/minecraft/mc-mods/had-enough-items)** **(4.29.15)** - An updated fork of JEI for 1.12.2 with optimizations and more features.
* **[JEI Area Fixer](https://www.curseforge.com/minecraft/mc-mods/jei-area-fixer)** **(2.3.0)** - A collection of mod fixes to prevent GUI overlap with JEI/HEI.
* **[LemonSkin](https://www.curseforge.com/minecraft/mc-mods/lemonskin)** **(4.0.0)** - An updated fork of AppleSkin, adding item food value tooltips and advanced hunger bar appearance.
* **[MixinBooter](https://www.curseforge.com/minecraft/mc-mods/mixin-booter)** **(10.7)** - A standardized library used for bytecode manipulation. Required by most mods in this pack.
* **[Mouse Tweaks Unofficial](https://www.curseforge.com/minecraft/mc-mods/mouse-tweaks-unofficial)** **(3.1.5)** - A continuation of MouseTweaks for Minecraft 1.12.2, adding improved mouse GUI interactions.
* **[PackCompanion](https://www.curseforge.com/minecraft/mc-mods/packcompanion)** **(1.0.2)** - A utility mod used to assist players and modpack makers in finding updated forks and problematic mods.
* **[Reach Fix](https://www.curseforge.com/minecraft/mc-mods/reach-fix)** **(1.1.3)** - Fixes the reach distance attribute not applying to player and entity attacks. Also improves hitbox interpolation when attacking entities.
* **[Red Core](https://www.curseforge.com/minecraft/mc-mods/red-core)** **(0.7.1)** - A library mod used by Alfheim Lighting Engine.
* **[SerializationIsBad](https://www.curseforge.com/minecraft/mc-mods/serializationisbad)** **(1.5.2)** - Fixes a number of serious security vulnerabilities present in several mods.
* **[Sound Device Options](https://www.curseforge.com/minecraft/mc-mods/more-sound-config)** **(1.0.4)** - A small mod that adds an option to switch the sound output device without reloading the game.
* **[StellarCore](https://www.curseforge.com/minecraft/mc-mods/stellarcore)** **(1.5.22)** - A collection of tweaks, optimizations and fixes targeted at 1.12.2.
* **[Universal Tweaks](https://www.curseforge.com/minecraft/mc-mods/universal-tweaks)** **(1.19.1)** - A community project to consolidate various bugfixes and tweaks into a single solution for Minecraft 1.12.2.
* **[VintageFix](https://www.curseforge.com/minecraft/mc-mods/vintagefix)** **(0.6.2)** - An updated an improved version of FoamFix. Improves load times and RAM usage for Minecraft 1.12.2.

---

## Optional Mods
* **[Aqua Acrobatics](https://www.curseforge.com/minecraft/mc-mods/aqua-acrobatics)** - Backports 1.13+ swimming, crouching, and crawling. Also backports item floating, which may cause issues with some mods.
* **[Enchantment Descriptions](https://www.curseforge.com/minecraft/mc-mods/enchantment-descriptions)** - Adds descriptions to enchantments describing their effects. Supported by most, but not all, mods that add enchantments.
* **[Ender's Modpack Tweaks](https://www.curseforge.com/minecraft/mc-mods/ender-modpack-tweaks)** - A collection of modpack tweaks, most notably an updated enemy health bar render. Has a soft requirement for [AssetMover](https://www.curseforge.com/minecraft/mc-mods/assetmover) which may increase load times.
* **[Entity Culling (by tr7zw)](https://www.curseforge.com/minecraft/mc-mods/entityculling)** - Improves performance by hiding entities and tile entities that are not in the player's line of sight. May cause some tile entities to flicker. Performance increases may vary.
* **[FastEntityRender](https://github.com/Meldexun/FastEntityRender)** - Improves entity rendering performance. Mod has not been published to CurseForge and does not support shaders. 
* **[Inventory Bogo Sort](https://www.curseforge.com/minecraft/mc-mods/inventory-bogosorter)** - An updated and highly configurable inventory sorter. Requires [Key Binding Patch](https://www.curseforge.com/minecraft/mc-mods/key-binding-patch) which breaks existing keybind settings.
* **[JEI Utilities](https://www.curseforge.com/minecraft/mc-mods/jei-utilities)** - Adds a number of useful JEI functions such as view history and recipe bookmarks.
* **[Particle Culling](https://www.curseforge.com/minecraft/mc-mods/particle-culling)** - Prevents particles outside the player's view from rendering. May cause inconsistent particle behavior. Performance increases may vary.
* **[Packet Fixer](https://www.curseforge.com/minecraft/mc-mods/packet-fixer)** - Fixes a number of packet issues in Minecraft. Slight overlap with Universal Tweaks.
* **[Potion Descriptions (Forge)](https://www.curseforge.com/minecraft/mc-mods/potion-descriptions)** - Adds descriptions to potions describing their effects. Not as widely supported as Enchantment Descriptions.
* **[Raw Mouse Input - Blessed Edition](https://www.curseforge.com/minecraft/mc-mods/raw-mouse-input-blessed-edition)** - (Forge only) Makes Minecraft 1.12.2 use raw mouse input, making mouse input feel smoother.
* **[Roughly Enough IDs](https://www.curseforge.com/minecraft/mc-mods/reid)** - Extends the block, item, biome, potion, and enchantment ID limits. Required for large modpacks.
* **[ScalingGUIs](https://www.curseforge.com/minecraft/mc-mods/scalingguis)** - Decouples the scaling of individual GUIs, the HUD, and Tooltips. Extremely useful for anyone playing at resolutions higher than 1080p.
* **[Server Tab Info](https://www.curseforge.com/minecraft/mc-mods/server-tab-info)** - Adds a the mean tick time and ticks per second (TPS) to the server info tab. Extremely useful for detecting TPS lag on servers or single player worlds.
* **[ZS Packet](https://www.curseforge.com/minecraft/mc-mods/zs-packet)** - Improves client to server and server to client packet compression. Provides a very small performance increase when hundreds of packets are being generated every second (which is ***extremely*** rare).

---

## FAQ

**Q:** Are there any other render optimization mods?
<div class="spoiler">
  <blockquote>
    <p>
      Yes, there are three:
      <ul>
        <li><a href="https://optifine.net/adloadx?f=preview_OptiFine_1.12.2_HD_U_G6_pre1.jar&x=c2f6">Optifine</a>
        <li><a href="https://github.com/kappa-maintainer/Celeritas-auto-build/releases">Celeritas</a> (Cleanroom Exclusive)
        <li><a href="https://www.curseforge.com/minecraft/mc-mods/nothirium">Nothirium</a>
      </ul>
    </p>
    <p>
        The effectiveness of these mods varies heavily from user to user, with some people getting significantly better performance, while others get worse performance.
    </p>
    <p>
        While not included in the 'Optional' section of this template, <a href="https://www.curseforge.com/minecraft/mc-mods/nothirium">Nothirium</a> is the BareBones recommendation. If adding Nothirium to your pack, be sure to also include <a href="https://www.curseforge.com/minecraft/mc-mods/naughthirium">Naughthirium</a>.
    </p>
    <p>
        Should you choose to add Optifine to your modpack, be sure to also include <a href="https://www.curseforge.com/minecraft/mc-mods/optinotfine">OptiNotFine</a>.
    </p>
    <p>
        You can read more information about these mods here: <a href="https://cleanroommc.com/wiki/end-user-guide/preparing-your-modpack#render-optimization-mods">Render optimization mods </a>
    </p>
  </blockquote>
</div>

**Q:** Why wasn't Entity/Particle Culling included by default?
<div class="spoiler">
  <blockquote>
    <p>
      Culling mods need to perform calculations to determine whether an object should be culled. As a result, they will always have some processing overhead.
    </p>
    <p>
      This means that these mods only have a performance increase once a world or base reaches a considerable number of entities or tile entities that are loaded and rendered.
    </p>
    <p>
      These mods are safe to include by default, but their actual performance increase will vary on a case by case basis.
    </p>
  </blockquote>
</div>

**Q:** Why wasn't Optifine included?
<div class="spoiler">
  <blockquote>
    <p>
      Optifine for 1.12.2 is extremely outdated and no longer supported by the developers. It increases load times and can cause rendering issues with modded entities. It is not incompatible with the BareBones template, but it may require additional configuration. 
    </p>
    <p>
      If you do choose to include Optifine, be sure to also add <a href="https://www.curseforge.com/minecraft/mc-mods/optinotfine">OptiNotFine</a> to your modpack instance.
    </p>
  </blockquote>
</div>

**Q:** Why wasn't &#x3C;insert mod here&#x3E; included?
<div class="spoiler">
  <blockquote>
    <p>
      When it comes to optimizations and fixes there is a lot of misinformation in the community. Bad actors will describe massive performance gains while posting mods that do nothing (Performant) or actively make game performance worse (Frustum Culling).
    </p>
    <p>
      BareBones is configured to automatically detect the majority of these problematic mods, but you should always be wary of any mod describing itself as an "Optimization" or "Performance" mod.
    </p>
  </blockquote>
</div>

**Q:** How can I spot questionable mods?
<div class="spoiler">
  <blockquote>
    <p>
      BareBones includes a number of features to help you find mods that cause issues, but there are new problematic mods being added to CurseForge and Modrinth on a daily basis. 
    </p>
    <p>
      When determining if a mod is actually useful, be sure to look out for these warning signs:
    </p>
    <ol>
      <li><b>The mod description boasts improved FPS or increased optimization.</b> Watch out descriptions that are incredibly vague and use key phrases such as "improved FPS", "reduced CPU/GPU load", "increased performance", or "improved optimization". </li>
      <li><b>Don't fall for the hype.</b> Very few (if any) mods can actually boost performance by 50% or by 100 FPS. Be wary of any mod that boasts extremely high performance gains.</li>
      <li><b>Tons of features.</b> If a mod description seems like it is too good to be true, it probably is. AI generated text leans towards sycophantic tones, telling you what you want to hear. Hundreds of additions with no incompatibilities is virtually impossible in modded environments.</li>
      <li><b>The mod license is All Rights Reserved.</b> While this isn't an immediate indication the mod is problematic, most mods that actually improve performance use open source licenses so other people can learn from or help improve the mod.</li>
      <li><b>The mod is closed source.</b> Most actual performance mods will post a link to a source repository so people can view the code. A closed source optimization mod is a good indicator that the mod author is trying to hide something.</li>
      <li><b>The description heavily uses colored text symbols or emojis.</b> While mod authors do try to spruce up their description pages, AI generated descriptions heavily utilize colored symbols for all of their section headers. If a description is AI generated, there's a high chance the mod is as well.</li>
      <li><b>Beware small file sizes.</b> While Minecraft mods are not exactly large, mod jars that are smaller than 20 KB are extremely rare. When they are that small, chances are that their effect is equally limited.</li>
    </ol>
    <p>
      While none of these signs are enough to disqualify a mod on their own, together they serve as a decent litmus test for questionable mods.
    </p>
  </blockquote>
</div>

**Q:** Where can I find a list of updated mods and mod forks?
<div class="spoiler">
  <blockquote>
    <p>
      CleanroomMC maintains a incomplete, but constantly updated list of depreciated mods and their forks. You can find this list here: <a href="https://cleanroommc.com/wiki/end-user-guide/preparing-your-modpack">Preparing Your Modpack </a>
    </p>
  </blockquote>
</div>
