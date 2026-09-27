#!/usr/bin/env python3
"""Build Prism, MRPACK, CurseForge and configuration downloads from the pinned manifest."""
from pathlib import Path, PurePosixPath
import hashlib
import json
import shutil
import zipfile

ROOT = Path(__file__).resolve().parent
DIST = ROOT / 'dist'


def write_zip(path, files):
    with zipfile.ZipFile(path, 'w', zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for name, source in files:
            parts = PurePosixPath(name).parts
            if name.startswith('/') or '..' in parts or source.is_symlink():
                raise ValueError('Unsafe archive path')
            info = zipfile.ZipInfo(name, (2026, 9, 9, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, source.read_bytes(), compresslevel=9)
    with zipfile.ZipFile(path) as archive:
        if archive.testzip() is not None:
            raise ValueError('Archive integrity check failed')
        if len(archive.namelist()) != len(set(archive.namelist())):
            raise ValueError('Duplicate archive paths')


def main():
    index = json.loads((ROOT / 'modrinth.index.json').read_text())
    assert index['formatVersion'] == 1 and index['game'] == 'minecraft'
    assert index['dependencies'] == {'minecraft': '1.21.1', 'neoforge': '21.1.252'}
    projects = json.loads((ROOT / 'upstream-projects.json').read_text())
    assert len(index['files']) == len(projects)
    assert len({entry['path'] for entry in index['files']}) == len(index['files'])
    assert {entry['path'] for entry in index['files']} == {p['path'] for p in projects}
    for entry in index['files']:
        assert not PurePosixPath(entry['path']).is_absolute() and '..' not in PurePosixPath(entry['path']).parts
        assert set(entry['hashes']) >= {'sha1', 'sha512'}
        assert all(url.startswith('https://cdn.modrinth.com/') and ' ' not in url for url in entry['downloads'])
    DIST.mkdir(exist_ok=True)
    stem = 'Create-Aeronautics-Vanilla-Plus-' + index['versionId']
    overlays = [(p.relative_to(ROOT).as_posix(), p) for p in sorted((ROOT / 'client-overrides').rglob('*')) if p.is_file()]
    mrpack = DIST / (stem + '.mrpack')
    write_zip(mrpack, [('modrinth.index.json', ROOT / 'modrinth.index.json'), *overlays])
    # Prism detects modrinth.index.json inside imported ZIPs and downloads its files.
    prism = DIST / (stem + '-Prism.zip')
    shutil.copyfile(mrpack, prism)
    config = DIST / (stem + '-Configs.zip')
    write_zip(config, [(name.removeprefix('client-overrides/'), source) for name, source in overlays])
    lock = json.loads((ROOT / 'curseforge-lock.json').read_text())
    assert lock['version'] == index['versionId']
    assert lock['minecraft'] == index['dependencies']['minecraft']
    assert lock['neoforge'] == index['dependencies']['neoforge']
    external = lock.get('external_files', [])
    all_locked = [*lock['files'], *external]
    assert {f['path'] for f in all_locked} == {f['path'] for f in index['files']}
    assert len(all_locked) == len(index['files'])
    assert len({(f['projectID'], f['fileID']) for f in lock['files']}) == len(lock['files'])
    originals = {f['path']: f for f in index['files']}
    for f in external:
        assert f['hashes'] == originals[f['path']]['hashes']
        assert f['downloads'] == originals[f['path']]['downloads']
    for f in lock['files']:
        assert f['modrinth_sha1'] == originals[f['path']]['hashes']['sha1']
        assert PurePosixPath(f['fileName']).name == f['fileName'] and '..' not in f['fileName']
        assert f['fileName'].endswith(PurePosixPath(f['path']).suffix)
        if not f['path'].startswith('mods/'):
            assert f['fileName'] == PurePosixPath(f['path']).name
        assert isinstance(f['projectID'], int) and f['projectID'] > 0
        assert isinstance(f['fileID'], int) and f['fileID'] > 0
    manifest = {
        'minecraft': {'version': lock['minecraft'], 'modLoaders': [
            {'id': 'neoforge-' + lock['neoforge'], 'primary': True}]},
        'manifestType': 'minecraftModpack', 'manifestVersion': 1,
        'name': index['name'], 'version': index['versionId'], 'author': 'DearDanielr',
        'files': [{'projectID': f['projectID'], 'fileID': f['fileID'], 'required': True}
                  for f in lock['files']],
        'overrides': 'overrides',
    }
    manifest_path = DIST / 'manifest.json'
    manifest_path.write_text(json.dumps(manifest, indent=2) + '\n')
    curseforge = DIST / (stem + '-CurseForge.zip')
    extra_files = []
    if external:
        instructions = DIST / 'EXTERNAL-MODS.txt'
        lines = ['Before launching this CurseForge import, download these upstream files',
                 'and place them in the indicated instance paths. Prism/MRPACK imports',
                 'download these files automatically.', '']
        for f in external:
            lines.extend([f['path'], f['downloads'][0],
                          'SHA512: ' + f['hashes']['sha512'], f['reason'], ''])
        instructions.write_text('\n'.join(lines) + '\n')
        extra_files.append(('overrides/EXTERNAL-MODS.txt', instructions))
    write_zip(curseforge, [('manifest.json', manifest_path), *extra_files,
        *[('overrides/' + name.removeprefix('client-overrides/'), source)
          for name, source in overlays]])
    manifest_path.unlink()
    if external:
        instructions.unlink()
    assets = [prism, mrpack, config, curseforge]
    checksums = ''.join(hashlib.file_digest(p.open('rb'), 'sha256').hexdigest() + '  ' + p.name + '\n' for p in assets)
    (DIST / 'SHA256SUMS.txt').write_text(checksums)
    for path in assets:
        print(f'{path.name}: {path.stat().st_size:,} bytes')


if __name__ == '__main__':
    main()
