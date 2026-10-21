"""Gate download buttons on the exact signed beta assets being public and intact.

Uses the runner's repository-scoped GitHub authentication through gh. Never logs
credentials; streaming asset hashes are verified without storing APKs in Git.
"""
import hashlib
import json
import os
from pathlib import Path
import subprocess
import urllib.error
import urllib.request

ROOT = Path(__file__).resolve().parent.parent
manifest = json.loads((ROOT / 'docs/release-manifest.json').read_text(encoding='utf-8-sig'))
tag = 'v' + manifest['versionName']
repository = os.environ.get('GH_REPO', 'mxge25/music-mxge')
if repository != 'mxge25/music-mxge':
    raise SystemExit('Unexpected release repository')
result = subprocess.run(['gh', 'api', f'repos/{repository}/releases/tags/{tag}'], capture_output=True, text=True)
published = False
if result.returncode == 0:
    release = json.loads(result.stdout)
    if release.get('draft') is False and release.get('prerelease') is True:
        if 'Not yet verified on physical devices. The cutter is experimental.' not in (release.get('body') or ''):
            raise SystemExit('Required beta validation warning is missing')
        assets = {item['name']: item for item in release.get('assets', [])}
        if 'SHA256SUMS.txt' in assets and all(item['file'] in assets for item in manifest['artifacts']):
            for item in manifest['artifacts']:
                asset = assets[item['file']]
                if asset['size'] != item['afterBytes']:
                    raise SystemExit(f'Unexpected release size: {item["file"]}')
                expected = f'https://github.com/{repository}/releases/download/{tag}/{item["file"]}'
                if asset['browser_download_url'] != expected:
                    raise SystemExit('Unexpected asset URL')
                digest = hashlib.sha256()
                with urllib.request.urlopen(expected, timeout=90) as stream:
                    while chunk := stream.read(65536):
                        digest.update(chunk)
                if digest.hexdigest() != item['sha256']:
                    raise SystemExit(f'Release hash mismatch: {item["file"]}')
            checksum_url = f'https://github.com/{repository}/releases/download/{tag}/SHA256SUMS.txt'
            with urllib.request.urlopen(checksum_url, timeout=30) as stream:
                checksums = stream.read(8192).decode('ascii')
            for item in manifest['artifacts']:
                if f'{item["sha256"]}  {item["file"]}' not in checksums:
                    raise SystemExit('Published checksum file is incomplete or incorrect')
            published = True
        else:
            print('Published release has missing APK assets; download buttons remain unavailable.')
    else:
        print('Release is a draft or is not the required pre-release; downloads remain unavailable.')
else:
    if '404' not in result.stderr:
        raise SystemExit('Could not query release status. Check repository Actions permissions.')
    print('No published beta release yet; downloads remain unavailable.')
script = ROOT / 'site/app.js'
text = script.read_text(encoding='utf-8')
text = text.replace('published: true', 'published: false')
if published:
    text = text.replace('published: false', 'published: true')
script.write_text(text, encoding='utf-8')
print('Download availability:', published)
