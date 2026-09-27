# Create Aeronautics - Vanilla Plus

Minecraft **1.21.1**, NeoForge **21.1.252**, Java **21**.

**1.12.0 updates 46 mods and NeoForge while keeping Minecraft 1.21.1.**
Install the matching client and server update together. Older servers reject the
new network channels added by several updated mods.

[<img src="assets/icons/prism.svg" width="18" height="18" alt="Prism"> Download 1.12.0 Prism ZIP](https://github.com/DearDanielr/anechoic-create-modpack/releases/download/v1.12.0/Create-Aeronautics-Vanilla-Plus-1.12.0-Prism.zip) · [<img src="assets/icons/modrinth.svg" width="18" height="18" alt="Modrinth"> Download 1.12.0 MRPACK](https://github.com/DearDanielr/anechoic-create-modpack/releases/download/v1.12.0/Create-Aeronautics-Vanilla-Plus-1.12.0.mrpack) · [Release notes](https://github.com/DearDanielr/anechoic-create-modpack/releases/tag/v1.12.0)

## What's new in 1.12.0

NeoForge is now **21.1.252**, the newest 1.21.1 build checked on September 27, 2026.
Updated mods include Distant Horizons, JEI, the RPG classes, Sophisticated
Backpacks/Storage, JourneyMap, Aquamirae and their libraries. MezzConfig 0.6.5
is added because the new JEI requires it. Six selected upstream builds are betas.
The complete version list is in [mod-updates-1.12.0.json](mod-updates-1.12.0.json).

**Spell Engine is pinned to 1.10.7.** Version 1.10.8 changes its loot API and crashes
with the latest Witcher 3.1.4 during server startup (`LootHelper.configure`
`NoSuchMethodError`). The pin retains Witcher and updates Spell Engine from 1.10.5.
The single-worker startup fix from 1.11.1 remains enabled. Existing pack balance
configuration and resource packs are retained.

**CurseForge imports require one additional download.** After importing the
[1.12.0 CurseForge ZIP](https://github.com/DearDanielr/anechoic-create-modpack/releases/download/v1.12.0/Create-Aeronautics-Vanilla-Plus-1.12.0-CurseForge.zip),
install the **NeoForge** jar from [WilderNature 1.1.6](https://modrinth.com/mod/lets-do-wildernature/version/jwvFJJGi)
into the instance's `mods` folder before launching. That build is absent from
the author's CurseForge files. The ZIP includes `EXTERNAL-MODS.txt` with the
exact upstream URL and checksum. Prism and MRPACK downloads install it automatically.

## Startup fix in 1.11.1

NeoForge now loads mods with one worker (`maxThreads = 1` in
`config/fml.toml`). Architectury 13.0.11 collects spawn registrations in an
unsynchronized list; concurrent mod construction can crash inside that list,
as observed while Critters and Companions 2.7.0 was initializing. This explains
why the same files can launch successfully before failing on another launch.
Better Mods Button's later "Cannot get config value before config is loaded"
exception was a secondary failure after mod construction had already failed.

Existing **1.11.0** installations can apply the fix without reinstalling:
close Minecraft, open the instance's `minecraft/config/fml.toml` (some launchers
use `.minecraft/config/fml.toml`), change `maxThreads = -1` to `maxThreads = 1`,
and launch again. Preserve the rest of the file. This limits startup mod loading;
it does not set gameplay, chunk generation, or rendering to one thread.
No mods, saves, controls, or server configuration need changing.

Source: [Architectury spawn registration](https://github.com/architectury/architectury-api/blob/1.21/neoforge/src/main/java/dev/architectury/registry/level/entity/forge/SpawnPlacementsRegistryImpl.java).
Verification and limitations: [validation-1.11.1.json](validation-1.11.1.json).

## What's new in 1.11.0

Tectonic is removed to address terrain seams and floating village buildings
observed after the terrain update. Terralith, Nature's Spirit, YUNG's Cave
Biomes and Gardens of the Dead remain, with standard world height. Existing
Nether and End terrain is preserved. The server uses **Hard** difficulty.

[Relics (RPG Series)](https://modrinth.com/mod/relics-rpg) adds 48 trinkets with
active and passive abilities through the existing Spell Engine system. Find
rewards in dungeon chests and from enemies and bosses; some use Jewelry gems.
This is an addition to the separate Relics mod already present in the pack.
It adds no structures or separate casting system.

Relics combat attribute bonuses are halved to limit stacking with Apotheosis
and class gear. Its stuns last one second, its crowd-control abilities have
at least 30-second cooldowns, and stuns/levitation exclude the shared boss tag,
including the Warden and the pack's major modded bosses. Movement and roll
utility remain. See [BALANCE.md](BALANCE.md) for the full balance scope.

The existing structure rarity and class balance remain. New biomes appear
in newly generated chunks. Sodium's fog occlusion remains disabled for cave
sandstorm visuals; Iris/Distant Horizons can still alter those effects.
Chunky pregeneration remains paused; this update does not restart it.

## Structure rates from 1.9.1

Large structure placement chances are **50% lower** than 1.9.0, including
When Dungeons Arise, Seven Seas, The Lost Castle, major boss dungeons, large
End ships, fortresses, mansions, and monuments. Other configured structure
sets have **25% lower** placement chances. Existing structures remain in
place; the change applies to newly generated terrain. Spacing, boss difficulty,
loot, mod versions, and existing Moog multipliers are retained. Exact per-set
settings are in [structure-density-1.9.1.json](structure-density-1.9.1.json).

## Additions in 1.9.0

Create: Diesel Generators, Apotheosis (including its Attributes, Enchanting and
Spawners modules), VeinMiner, and GraveStone Mod are added to the exploration
and RPG pack below. The balance profile limits gear stacking and strengthens
major bosses from Legendary Monsters, Aquamirae, and Illager Invasion.

Hold **Sneak** while mining ore to mine up to **16 connected blocks** with the
correct pickaxe. Each extra block costs durability and hunger, with a two-second
cooldown between veins. Graves protect items for their owner; return to the
place of death to recover them.

See [BALANCE.md](BALANCE.md) for the exact boss stats, gear limits, and test scope.

## Exploration and RPG classes

The pack adds When Dungeons Arise, The Lost Castle, Seven Seas, and Lootr.
Lootr gives each player their own loot from eligible containers. New structures
appear in newly generated terrain; already explored or pregenerated chunks
retain their existing terrain.

Spell Engine powers the following class mods:

| Mod | Classes and specializations |
| --- | --- |
| Archers | Archer |
| Wizards | Arcane, Fire, Frost |
| Paladins & Priests | Paladin, Priest |
| Rogues & Warriors | Rogue, Warrior |
| Bard | Bard |
| Berserker | Berserker |
| Archers Expansion | Rogue Archer, Tundra Hunter, War Archer |
| Forcemaster | Forcemaster |
| Elemental Wizards | Water, Earth, Wind |
| Witcher | Witcher signs and sword techniques |

The update also includes the main RPG Series Skill Tree, Runes, Jewelry,
Additional Jewelry, Arsenal, Armory, Gazebos, Village Taverns, and their required
libraries. **F7** opens the skill tree. Class spellbooks and the Spell Binding
Table provide access to spells. Existing controls are preserved.

Druids 1.2 and More RPG Classes - Skill Tree 1.1.2 use removed Spell Engine APIs
and are excluded. The latter is an optional addon; the main RPG Series Skill
Tree is included. Death Knights and Spellblades and Such have no native
NeoForge 1.21.1 releases. RPG versions and exclusions are recorded in
[update-1.8.0.json](update-1.8.0.json); the new additions are in
[update-1.9.0.json](update-1.9.0.json).

Aeronautics Delivery Quests, ADQ Tweaks, and the server notification addon are
removed. Delivery Quests caused confirmed quest-sync packet errors that kicked
players. These mods are no longer loaded, and existing quest tables no longer
function. Saved quest files are retained in the server backup.

## Install

1. In [Prism Launcher](https://prismlauncher.org/), choose **Add Instance → Import**
   and select the 1.11.1 Prism ZIP or MRPACK. Import it as a separate instance
   to preserve any local saves and settings in your older instance.
2. Use Java 21 and allow up to **8 GiB** of client memory.
3. Join `play.create.anechoicaxolotl.com`.
   New players can use the [whitelist site](https://whitelist.anechoicaxolotl.com/).

For the **CurseForge app**, choose **Minecraft → Import → Import Profile .zip**
and select the **CurseForge ZIP**. Use a separate profile, Java 21, and up to
8 GiB of memory. The Prism ZIP is intended for Prism; select the archive for
your launcher. [CurseForge's import instructions](https://support.curseforge.com/support/solutions/articles/9000197912)
show the app's import screen.

The Prism ZIP and MRPACK download the pinned files from Modrinth.
The CurseForge ZIP downloads all 177 mods and one shader from CurseForge,
with the same pack settings, resource pack, and controls. No manual mod copying
is needed. All 178 downloads were verified; 165 match the Modrinth files byte
for byte, and 13 use upstream builds of the same versions with only verified
build metadata, generated build IDs, ZIP packaging, or access-rule ordering
differences. CurseForge's Terralith JAR has a different filename but identical
bytes. Actual import in the CurseForge app has not been tested.

 An internet
connection is required. The Prism ZIP uses Prism's Modrinth importer; it is
not an offline bundle. The Configs ZIP contains settings, controls, and the
resource pack for an installation that already has these exact mod versions.

## Contents and checks

The production server also includes the pack's matching JEI 19.51.0.418, which
supports the **Move Items** / **+** recipe-transfer button. This fixes the
"server must have JEI installed" message. The current pack includes this exact version.

1.11.1 contains **177 client mods and one shader**, with exactly the same
upstream files as 1.11.0. It is compatible with the existing 1.11.0 server
and its server-only tools. No mod or shader binaries
are redistributed by this repository: manifests reference upstream downloads.

[THIRD-PARTY.md](THIRD-PARTY.md) lists projects and licenses.
`modrinth.index.json` pins URLs, sizes, and SHA-1/SHA-512 hashes; `mods.sha256`
records an additional inventory. `curseforge-lock.json` pins CurseForge project/file
IDs and hashes; `curseforge-validation-1.11.0.json` records the unchanged upstream conversion checks. `SHA256SUMS.txt` accompanies the release assets.

Startup-fix checks are recorded in `validation-1.11.1.json`; earlier terrain
and gameplay deployment checks remain in `validation-1.11.0.json`.
Automated compatibility and terrain samples do not establish that every
structure, class combination, or boss fight has been playtested.

Download icon sources and attribution are in [assets/icons/ATTRIBUTION.txt](assets/icons/ATTRIBUTION.txt).
