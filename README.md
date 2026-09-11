# Create Aeronautics - Vanilla Plus

Minecraft **1.21.1**, NeoForge **21.1.249**, Java **21**.

**1.10.0 adds larger landscapes and new surface, cave, and Nether biomes.**
Install this version to join the updated server; 1.9.x clients lack the new
biome blocks and mobs.

[Download 1.10.0 Prism ZIP](https://github.com/DearDanielr/anechoic-create-modpack/releases/download/v1.10.0/Create-Aeronautics-Vanilla-Plus-1.10.0-Prism.zip) · [Download 1.10.0 MRPACK](https://github.com/DearDanielr/anechoic-create-modpack/releases/download/v1.10.0/Create-Aeronautics-Vanilla-Plus-1.10.0.mrpack) · [Release notes](https://github.com/DearDanielr/anechoic-create-modpack/releases/tag/v1.10.0)

## What's new in 1.10.0

| Addition | What you can explore |
| --- | --- |
| Tectonic 3.0.26 | Large mountain ranges, valleys, deep oceans, canyons and underground rivers |
| Nature's Spirit 2.2.5 | 51 biomes, including redwood and wisteria forests, lavender fields and tropical shores |
| YUNG's Cave Biomes 3.1.1 | Frosted Caves and Lost Caves, with their own creatures, blocks and discoveries |
| Gardens of the Dead 5.0.2 | Soulblight Forest and Whistling Woods in the Nether |

Tectonic runs alongside the existing Terralith using its bundled compatibility
support. Standard world height and existing mod versions are retained. All
four additions are installed on the server and included in the client pack.
Nature's Spirit, YUNG's Cave Biomes, and Gardens of the Dead require clients
to update because they add blocks or mobs.

The reduced structure rates and RPG/boss balance remain. Nature's Spirit's
villages use the same reduced placement chance as existing villages. New
biomes appear in newly generated chunks. Existing Nether and End terrain is
preserved. Sodium's fog occlusion is disabled for the cave sandstorm visuals;
Iris/Distant Horizons can still alter those effects.

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
   and select the 1.10.0 Prism ZIP or MRPACK. Import it as a separate instance
   to preserve any local saves and settings in your older instance.
2. Use Java 21 and allow up to **8 GiB** of client memory.
3. Join `play.create.anechoicaxolotl.com`.
   New players can use the [whitelist site](https://whitelist.anechoicaxolotl.com/).

Both import formats download the pinned files from Modrinth. An internet
connection is required. The Prism ZIP uses Prism's Modrinth importer; it is
not an offline bundle. The Configs ZIP contains settings, controls, and the
resource pack for an installation that already has these exact mod versions.

## Contents and checks

The production server also includes the pack's matching JEI 19.51.0.418, which
supports the **Move Items** / **+** recipe-transfer button. This fixes the
"server must have JEI installed" message. The current pack includes this exact version. The biome additions in 1.10.0
require a client update even though JEI itself is unchanged.

1.10.0 contains **177 client mods and one shader**. Compared with 1.7.1, the
update adds 47 mods and removes Delivery Quests and ADQ Tweaks; all remaining
original versions are retained. The matching server runs 143 mod files,
including its existing server tools. No mod or shader binaries are
redistributed by this repository: the manifests reference upstream downloads.

[THIRD-PARTY.md](THIRD-PARTY.md) lists projects and licenses.
`modrinth.index.json` pins URLs, sizes, and SHA-1/SHA-512 hashes; `mods.sha256`
records an additional inventory. `SHA256SUMS.txt` accompanies the release assets.

The complete server mod set passed isolated startup and saved-world restart
checks. Production was activated on September 11, 2026 UTC after a verified
full offline backup. The balance datapack and Apotheosis registries loaded,
and read-only server checks returned 20 TPS with Chunky paused. This does not
replace client, multiplayer, flight, or class-balance playtesting. Existing
optional-integration warnings remain.

Run `python3 build.py` to reproduce the import archives and checksums in `dist/`.
