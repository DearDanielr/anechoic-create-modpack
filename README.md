# Create Aeronautics - Vanilla Plus

Minecraft **1.21.1**, NeoForge **21.1.249**, Java **21**.

**1.11.0 removes Tectonic and expands the existing Spell Engine classes with
Relics (RPG Series).** Install this version to join the updated server.

[Download 1.11.0 Prism ZIP](https://github.com/DearDanielr/anechoic-create-modpack/releases/download/v1.11.0/Create-Aeronautics-Vanilla-Plus-1.11.0-Prism.zip) · [Download 1.11.0 MRPACK](https://github.com/DearDanielr/anechoic-create-modpack/releases/download/v1.11.0/Create-Aeronautics-Vanilla-Plus-1.11.0.mrpack) · [Release notes](https://github.com/DearDanielr/anechoic-create-modpack/releases/tag/v1.11.0)

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
Chunky is pregenerating a 5,000-block-radius circle around the saved spawn.
Storage monitoring pauses pregeneration if free space becomes low.

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
   and select the 1.11.0 Prism ZIP or MRPACK. Import it as a separate instance
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
"server must have JEI installed" message. The current pack includes this exact version.

1.11.0 contains **177 client mods and one shader**. The matching server runs
143 mod files, including its existing server tools. All 1.10.0 mod versions
other than the removed Tectonic file are retained. No mod or shader binaries
are redistributed by this repository: manifests reference upstream downloads.

[THIRD-PARTY.md](THIRD-PARTY.md) lists projects and licenses.
`modrinth.index.json` pins URLs, sizes, and SHA-1/SHA-512 hashes; `mods.sha256`
records an additional inventory. `SHA256SUMS.txt` accompanies the release assets.

Validation and deployment results are recorded in `validation-1.11.0.json`.
Automated compatibility and terrain samples do not establish that every
structure, class combination, or boss fight has been playtested.
