# Create Aeronautics - Vanilla Plus

Minecraft **1.21.1**, NeoForge **21.1.249**, Java **21**.

**1.9.0 is live on the Create server.** Download this version to join; older
1.7.1 and 1.8.0 instances do not contain the matching mod set.

[Download 1.9.0 Prism ZIP](https://github.com/DearDanielr/anechoic-create-modpack/releases/download/v1.9.0/Create-Aeronautics-Vanilla-Plus-1.9.0-Prism.zip) · [Download 1.9.0 MRPACK](https://github.com/DearDanielr/anechoic-create-modpack/releases/download/v1.9.0/Create-Aeronautics-Vanilla-Plus-1.9.0.mrpack) · [Release notes](https://github.com/DearDanielr/anechoic-create-modpack/releases/tag/v1.9.0)

## What's new in 1.9.0

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
   and select the 1.9.0 Prism ZIP or MRPACK. Import it as a separate instance
   to preserve any local saves and settings in your older instance.
2. Use Java 21 and allow up to **8 GiB** of client memory.
3. Join `play.create.anechoicaxolotl.com`.
   New players can use the [whitelist site](https://whitelist.anechoicaxolotl.com/).

Both import formats download the pinned files from Modrinth. An internet
connection is required. The Prism ZIP uses Prism's Modrinth importer; it is
not an offline bundle. The Configs ZIP contains settings, controls, and the
resource pack for an installation that already has these exact mod versions.

## Contents and checks

1.9.0 contains **173 client mods and one shader**. Compared with 1.7.1, the
update adds 43 mods and removes Delivery Quests and ADQ Tweaks; all remaining
original versions are retained. The matching server runs 138 mod files,
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
