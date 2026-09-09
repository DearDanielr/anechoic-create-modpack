# Create Aeronautics - Vanilla Plus

Client pack for `play.create.anechoicaxolotl.com`.

Minecraft **1.21.1**, NeoForge **21.1.249**, pack **1.7.1**. Includes 132 mods, Simple Voice Chat, shaders, configs, and preset controls.

[Download Prism ZIP](https://github.com/DearDanielr/anechoic-create-modpack/releases/download/v1.7.1/Create-Aeronautics-Vanilla-Plus-1.7.1-Prism.zip) · [Download MRPACK](https://github.com/DearDanielr/anechoic-create-modpack/releases/download/v1.7.1/Create-Aeronautics-Vanilla-Plus-1.7.1.mrpack) · [All downloads](https://github.com/DearDanielr/anechoic-create-modpack/releases/tag/v1.7.1)

## Install

1. In [Prism Launcher](https://prismlauncher.org/), choose **Add Instance → Import** and select either download. The MRPACK also works with launchers that support Modrinth packs.
2. Use Java 21 and allow up to 8 GiB of memory for the instance.
3. Get whitelisted at [whitelist.anechoicaxolotl.com](https://whitelist.anechoicaxolotl.com/), then add `play.create.anechoicaxolotl.com` in Minecraft's Multiplayer menu.

Both import files download the pinned mod and shader files from Modrinth. An internet connection is required during import. The Prism ZIP uses the same manifest as the MRPACK; it is not an offline bundle. Configs and controls are included in both.

The separate **Configs ZIP** contains only settings, controls, and the resource pack. It is for an existing installation of this exact pack version. `SHA256SUMS.txt` contains checksums for all three downloads.

## Pack contents

[Included projects and credits](THIRD-PARTY.md) lists the mods and shaders. `modrinth.index.json` pins every download URL, file size, and SHA-1/SHA-512 hash. `mods.sha256` provides an additional file inventory.

All 93 mod JARs shared with the dedicated server were checked and match byte for byte. The other client mods provide graphics, sound, controls, and UI features. The server's five extra mods are server tools and do not belong in a client installation.

This is the client release for the current server. No full multiplayer gameplay test was performed as part of publishing this release.

## Build downloads

Run `python3 build.py`. The archives and checksums are written to `dist/`. The build uses only Python's standard library and packages the committed configs and manifest; mod binaries are downloaded by the launcher during import.
