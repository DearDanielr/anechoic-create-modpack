Fixes an intermittent startup crash in the 1.11.0 client pack.

NeoForge now constructs mods using one worker (`maxThreads = 1` in
`config/fml.toml`). This avoids concurrent writes to Architectury 13.0.11's
spawn-registration list, where Critters and Companions 2.7.0 failed during
startup. Better Mods Button's later config exception was a secondary failure.

**Same 177 mods and one shader as 1.11.0. Compatible with the existing server;
no server update or restart needed.** Gameplay threading is unchanged.

For an existing 1.11.0 instance, close Minecraft and change `maxThreads = -1`
to `maxThreads = 1` in its `minecraft/config/fml.toml` (or
`.minecraft/config/fml.toml`, depending on launcher). Preserve other settings.
You do not need to reinstall or copy your saves.

For a fresh installation, import the Prism ZIP, MRPACK, or CurseForge ZIP
appropriate for your launcher. Use Java 21 and up to 8 GiB memory.

All upstream file pins and hashes are unchanged. The sole gameplay-folder
change from the published 1.11.0 pack is `config/fml.toml`.

Validation: the installed client completed startup, joined the production
server, authenticated Sable UDP and connected to voice chat after the change.
The server remained running throughout. All four archives passed integrity
checks and contain the setting; all 178 download pins are unchanged.
This was one observed client launch and join, not a repeated-start or gameplay
soak test. Fresh CurseForge app import was not performed.
See `validation-1.11.1.json` for details.
