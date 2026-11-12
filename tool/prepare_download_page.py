"""Enable each application's downloads only after its published assets verify."""
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import ssl
import subprocess
import urllib.request

ca_bundle = Path('D:/Program Files/Git/mingw64/etc/ssl/certs/ca-bundle.crt')
if ca_bundle.exists():
    ssl._create_default_https_context = lambda: ssl.create_default_context(cafile=str(ca_bundle))

ROOT = Path(__file__).resolve().parent.parent
REPOSITORY = os.environ.get('GH_REPO', 'mxge25/music-mxge')
if REPOSITORY != 'mxge25/music-mxge':
    raise SystemExit('Unexpected release repository')

def verify(filename, warning):
    manifest = json.loads((ROOT / 'docs' / filename).read_text(encoding='utf-8-sig'))
    tag = manifest['releaseTag']
    if shutil.which('gh'):
        result = subprocess.run(['gh', 'api', f'repos/{REPOSITORY}/releases/tags/{tag}'], capture_output=True, text=True)
        if result.returncode:
            if '404' not in result.stderr:
                raise SystemExit('Could not read release status')
            return False, tag
        release = json.loads(result.stdout)
    else:
        curl_cmd = ['curl.exe', '-sS', f'https://api.github.com/repos/{REPOSITORY}/releases/tags/{tag}', '-A', 'MXGE-Verifier']
        token = os.environ.get('GH_TOKEN')
        if token:
            curl_cmd.extend(['-H', f'Authorization: Bearer {token}'])
        proc = subprocess.run(curl_cmd, capture_output=True, text=True)
        if proc.returncode != 0 or 'Not Found' in proc.stdout:
            return False, tag
        release = json.loads(proc.stdout)
    if release.get('draft') is not False or release.get('prerelease') is not True:
        return False, tag
    if warning not in (release.get('body') or ''):
        raise SystemExit('Required experimental validation warning is missing')
    assets = {item['name']: item for item in release.get('assets', [])}
    files = manifest['artifacts'] + manifest.get('sourceArtifacts', [])
    if 'SHA256SUMS.txt' not in assets or any(item['file'] not in assets for item in files):
        return False, tag
    base = f'https://github.com/{REPOSITORY}/releases/download/{tag}'
    req = urllib.request.Request(base + '/SHA256SUMS.txt', headers={'User-Agent': 'MXGE-Verifier'})
    with urllib.request.urlopen(req, timeout=30) as response:
        checksums = response.read(16384).decode('ascii')
    for item in files:
        expected_bytes = item.get('bytes', item.get('afterBytes'))
        asset = assets[item['file']]
        expected_url = base + '/' + item['file']
        if asset['size'] != expected_bytes or asset['browser_download_url'] != expected_url:
            raise SystemExit('Release asset metadata mismatch: ' + item['file'])
        if f'{item["sha256"]}  {item["file"]}' not in checksums:
            raise SystemExit('Checksum file does not match: ' + item['file'])
        local_dist = ROOT / 'dist' / item['file']
        if local_dist.exists() and local_dist.stat().st_size == expected_bytes:
            local_hash = hashlib.sha256(local_dist.read_bytes()).hexdigest()
            if local_hash == item['sha256']:
                continue
        digest = hashlib.sha256()
        req = urllib.request.Request(expected_url, headers={'User-Agent': 'MXGE-Verifier'})
        with urllib.request.urlopen(req, timeout=90) as response:
            while chunk := response.read(1024 * 1024):
                digest.update(chunk)
        if digest.hexdigest() != item['sha256']:
            raise SystemExit('Release checksum mismatch: ' + item['file'])
    return True, tag

player, player_tag = verify('release-manifest.json', 'Not yet verified on physical devices. The cutter is experimental.')
companion, companion_tag = verify('companion-release-manifest.json', 'Experimental companion. Downloads from supported public links are not yet verified on physical devices.')
scanner_manifest = ROOT / 'docs' / 'scanner-release-manifest.json'
scanner, scanner_tag = (
    verify(scanner_manifest.name, 'Camera and OCR have not been verified on a physical Android device.')
    if scanner_manifest.exists() else (False, 'mxge-scanner-v0.1.0-beta.1')
)
script = ROOT / 'site/app.js'
text = script.read_text(encoding='utf-8')
for name, available, tag in [
    ('release', player, player_tag),
    ('companionRelease', companion, companion_tag),
    ('scannerRelease', scanner, scanner_tag),
]:
    text, count = re.subn(r'const ' + name + r' = \{[^;]+\};',
        f"const {name} = {{ published: {str(available).lower()}, tag: '{tag}' }};", text, count=1)
    if count != 1:
        raise SystemExit('Missing release availability declaration')
script.write_text(text, encoding='utf-8')
print('Verified downloads:', {'player': player, 'companion': companion, 'scanner': scanner})
