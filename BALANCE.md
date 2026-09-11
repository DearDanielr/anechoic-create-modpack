# Balance profile for 1.9.0

This profile covers the installed modded bosses as well as equipment used
against vanilla bosses. It is a tested starting configuration, not a claim
that every class, party size, and equipment combination has been playtested.

## Bosses

| Mod | Boss | Previous health | New health |
| --- | --- | ---: | ---: |
| Legendary Monsters | The Obliterator | 450 | 675 |
| Legendary Monsters | Cloud Golem | 350 | 525 |
| Legendary Monsters | Possessed Paladin | 400 | 600 |
| Aquamirae | Captain Cornelia | 300 | 450 |
| Illager Invasion | Invoker | 250 | 375 |

Legendary Monsters' three major bosses also use a 1.15 damage multiplier.
Their native damage caps, invulnerability windows, adaptation, phases, and
protections against avoiding attacks remain enabled as previously configured.
Cornelia and the Invoker retain their original damage and spell mechanics.
The Invoker's health modifier applies once, preserves its health percentage,
and persists with the entity. Cornelia and the Invoker join the shared boss
tag, allowing Spell Engine and More RPG Library to recognize them as bosses
and apply their existing boss and stun-immunity rules.

Ordinary mobs and other minibosses retain their original base stats.
Apotheosis's existing world-tier unlocks and scaling remain in place; this
profile does not unlock higher-tier loot at the start of the game.

## Equipment and spell progression

- Most positive Apotheosis combat attribute bonuses from affixes and gems
  are halved. Utility bonuses and negative tradeoffs are retained.
- Generated equipment has at most two sockets. The existing socket-adding
  recipe also stops at two.
- The executing affix is removed from random generation and its execution
  threshold is zero. It can otherwise directly kill a boss through its
  remaining health and phase mechanics.
- Current-health damage bonuses are reduced to one tenth of their original
  values, capped at 2.5% per bonus. Lifesteal bonuses are reduced to one
  quarter, capped at 4% per bonus. These are per-bonus limits, not global
  character-stat caps.
- Apotheosis affix/gem strength, resistance, and regeneration effects are
  limited to level I and do not stack on reapplication.
- Enchantments keep their original mod or vanilla maximums, including RPG
  enchantments. Efficiency allows VI and Unbreaking IV; Berserker's Fury is
  limited to I. Forced effective caps prevent gem and item-data bonuses from
  bypassing these limits. Sharpness V, Protection IV, Power V, Fortune III,
  and Looting III remain the relevant vanilla caps.
- Potion charms must be equipped in Curios to function. Ancient Knowledge's
  XP multiplier is reduced from 4 to 1. Protection enchantments cannot supply
  more than 65% damage reduction through Apothic Attributes' formula.
- The existing RPG class tuning is retained, including the shared five-tick
  instant-spell cooldown and reduced execute, healing, stealth, and stun
  settings. The optional incompatible class-tree addon and Druids remain out.

## Mining, engines, and graves

VeinMiner applies only to the `c:ores` group with pickaxes. Hold Sneak and use
the correct mining tier. A vein is limited to 16 blocks, with a two-second
cooldown, normal tool wear for each block, and 0.4 exhaustion per extra block.
Extra blocks are processed with a short delay; the mining-speed setting also
slows the initial break as the vein grows. Stone, dungeon masonry, machines,
spawners, and graves are outside the allowed group. Fortune and Silk Touch
continue to follow the tool's enchantments and the limits above.

Turbocharged diesel engines use twice the normal fuel burn rate to match
their twice-normal speed multiplier. Refining, recipes, and ordinary engine
output retain the upstream settings. Harvesting an Apothic spawner with
Silk Touch costs 200 durability instead of 100.

Graves can be recovered only by their owner or an administrator. They require
returning to the death location; no teleport or free inventory-restoration
feature is enabled. Grave placement avoids replacing machine blocks, and
ghost spawning remains disabled. Death rules and XP handling are unchanged.

## Verification

The combined pack was checked in a disposable dedicated server. Runtime
checks verified the five boss health values, effective enchantment caps on
deliberately over-levelled items, and the loaded Apotheosis overrides.
Simulated mining verified the 16-block limit, cooldown, sneak requirement,
tool tier, stone exclusion, durability use, and hunger charge.

Full multiplayer combat, flight, boss-fight difficulty, and player death/grave
recovery have not been playtested. New mods take effect on the production
server's next authorized restart; no production restart was performed while
preparing this release.

Exact settings are recorded in [balance-1.9.0.json](balance-1.9.0.json).
Apotheosis data overrides retain its MIT license inside the balance datapack.
