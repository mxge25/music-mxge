"""Enable each application's downloads only after its published assets verify."""
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import urllib.request

ROOT = Path(__file__).resolve().parent.parent
REPOSITORY = os.environ.get('GH_REPO', 'mxge25/music-mxge')
if REPOSITORY != 'mxge25/music-mxge':
    raise SystemExit('Unexpected release repository')

def verify(filename, warning):
    manifest = json.loads((ROOT / 'docs' / filename).read_text(encoding='utf-8-sig'))
    tag = manifest['releaseTag']
    result = subprocess.run(['gh', 'api', f'repos/{REPOSITORY}/releases/tags/{tag}'], capture_output=True, text=True)
    if result.returncode:
        if '404' not in result.stderr:
            raise SystemExit('Could not read release status')
        return False, tag
    release = json.loads(result.stdout)
    if release.get('draft') is not False or release.get('prerelease') is not True:
        return False, tag
    if warning not in (release.get('body') or ''):
        raise SystemExit('Required experimental validation warning is missing')
    assets = {item['name']: item for item in release.get('assets', [])}
    files = manifest['artifacts'] + manifest.get('sourceArtifacts', [])
    if 'SHA256SUMS.txt' not in assets or any(item['file'] not in assets for item in files):
        return False, tag
    base = f'https://github.com/{REPOSITORY}/releases/download/{tag}'
    with urllib.request.urlopen(base + '/SHA256SUMS.txt', timeout=30) as response:
        checksums = response.read(16384).decode('ascii')
    for item in files:
        expected_bytes = item.get('bytes', item.get('afterBytes'))
        asset = assets[item['file']]
        expected_url = base + '/' + item['file']
        if asset['size'] != expected_bytes or asset['browser_download_url'] != expected_url:
            raise SystemExit('Release asset metadata mismatch: ' + item['file'])
        digest = hashlib.sha256()
        with urllib.request.urlopen(expected_url, timeout=90) as response:
            while chunk := response.read(1024 * 1024):
                digest.update(chunk)
        if digest.hexdigest() != item['sha256']:
            raise SystemExit('Release checksum mismatch: ' + item['file'])
        if f'{item["sha256"]}  {item["file"]}' not in checksums:
            raise SystemExit('Checksum file does not match: ' + item['file'])
    return True, tag

player, player_tag = verify('release-manifest.json', 'Not yet verified on physical devices. The cutter is experimental.')
companion, companion_tag = verify('companion-release-manifest.json', 'Experimental companion. Downloads from supported public links are not yet verified on physical devices.')
script = ROOT / 'site/app.js'
text = script.read_text(encoding='utf-8')
for name, available, tag in [('release', player, player_tag), ('companionRelease', companion, companion_tag)]:
    text, count = re.subn(r'const ' + name + r' = \{[^;]+\};',
        f"const {name} = {{ published: {str(available).lower()}, tag: '{tag}' }};", text, count=1)
    if count != 1:
        raise SystemExit('Missing release availability declaration')
script.write_text(text, encoding='utf-8')
print('Verified downloads:', {'player': player, 'companion': companion})
