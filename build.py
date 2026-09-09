#!/usr/bin/env python3
"""Build Prism, MRPACK and configuration downloads from the pinned manifest."""
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
    assert index['dependencies'] == {'minecraft': '1.21.1', 'neoforge': '21.1.249'}
    assert len(index['files']) == 133
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
    assets = [prism, mrpack, config]
    checksums = ''.join(hashlib.file_digest(p.open('rb'), 'sha256').hexdigest() + '  ' + p.name + '\n' for p in assets)
    (DIST / 'SHA256SUMS.txt').write_text(checksums)
    for path in assets:
        print(f'{path.name}: {path.stat().st_size:,} bytes')


if __name__ == '__main__':
    main()
