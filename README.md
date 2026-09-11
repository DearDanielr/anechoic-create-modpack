# Create Aeronautics - Vanilla Plus

Minecraft **1.21.1**, NeoForge **21.1.249**, Java **21**.

**1.8.0 is installed on disk and waiting for the Create server's next restart.**
Keep using [1.7.1](https://github.com/DearDanielr/anechoic-create-modpack/releases/tag/v1.7.1)
to join the currently running server. The new release is marked as a prerelease
until the server update is activated.

[Download 1.8.0 Prism ZIP](https://github.com/DearDanielr/anechoic-create-modpack/releases/download/v1.8.0/Create-Aeronautics-Vanilla-Plus-1.8.0-Prism.zip) · [Download 1.8.0 MRPACK](https://github.com/DearDanielr/anechoic-create-modpack/releases/download/v1.8.0/Create-Aeronautics-Vanilla-Plus-1.8.0.mrpack) · [Release notes](https://github.com/DearDanielr/anechoic-create-modpack/releases/tag/v1.8.0)

## What's new in 1.8.0

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
NeoForge 1.21.1 releases. Exact versions and exclusions are recorded in
[update-1.8.0.json](update-1.8.0.json).

Aeronautics Delivery Quests, ADQ Tweaks, and the server notification addon are
removed. Delivery Quests caused confirmed quest-sync packet errors that kicked
players. Removal takes effect after the server restart; existing quest tables
will no longer function. Saved quest files are retained in the server backup.

## Install

1. In [Prism Launcher](https://prismlauncher.org/), choose **Add Instance → Import**
   and select the Prism ZIP or MRPACK. Import 1.8.0 as a separate instance so
   1.7.1 remains available while the server update is pending.
2. Use Java 21 and allow up to **8 GiB** of client memory.
3. After the server update is activated, join `play.create.anechoicaxolotl.com`.
   New players can use the [whitelist site](https://whitelist.anechoicaxolotl.com/).

Both import formats download the pinned files from Modrinth. An internet
connection is required. The Prism ZIP uses Prism's Modrinth importer; it is
not an offline bundle. The Configs ZIP contains settings, controls, and the
resource pack for an installation that already has these exact mod versions.

## Contents and checks

1.8.0 contains **162 client mods and one shader**. The update adds 32 mods and
removes Delivery Quests and ADQ Tweaks; all remaining original versions are
retained. The matching server has 127 mod files after restart, including its
existing server tools. No mod or shader binaries are
redistributed by this repository: the manifests reference upstream downloads.

[THIRD-PARTY.md](THIRD-PARTY.md) lists projects and licenses.
`modrinth.index.json` pins URLs, sizes, and SHA-1/SHA-512 hashes; `mods.sha256`
records an additional inventory. `SHA256SUMS.txt` accompanies the release assets.

The complete server mod set passed isolated startup and saved-world restart
checks. This does not replace client, multiplayer, flight, or class-balance
playtesting. Existing optional-integration warnings remain.

Run `python3 build.py` to reproduce the import archives and checksums in `dist/`.
