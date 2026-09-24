#!/usr/bin/env python3
"""Offline checks for this kit's Markdown, inventories and saved content digest."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys
from datetime import datetime, timezone
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
REPORT = 'PACKAGE-CHECKS.json'


def markdown(text):
    """Return prose and anchor IDs for the ATX headings/fences used by this kit."""
    prose, anchors, counts = [], set(), {}
    fence = None
    for line in text.splitlines():
        match = re.match(r'^ {0,3}(`{3,}|~{3,})(.*)$', line)
        if match:
            marker, tail = match.groups()
            if fence is None:
                fence = marker
            elif marker[0] == fence[0] and len(marker) >= len(fence) and not tail.strip():
                fence = None
            continue
        if fence:
            continue
        prose.append(line)
        heading = re.match(r'^#{1,6}\s+(.+?)\s*#*$', line)
        if heading:
            slug = re.sub(r'[^\w -]', '', heading[1].lower()).replace(' ', '-')
            occurrence = counts.get(slug, 0)
            anchors.add(slug + (f'-{occurrence}' if occurrence else ''))
            counts[slug] = occurrence + 1
        anchors.update(re.findall(r'<a\s+id="([^"]+)"', line))
    if fence:
        raise ValueError('unclosed Markdown code fence')
    return '\n'.join(prose), anchors


def check(write_report=False):
    listed = subprocess.check_output(
        ['git', 'ls-files', '--cached', '--others', '--exclude-standard', '-z'], cwd=ROOT
    ).decode().split('\0')
    names = sorted(set(filter(None, listed)))
    files, docs, data = {}, {}, {}
    for name in names:
        path = ROOT / name
        if path.is_symlink() or not path.is_file():
            raise ValueError(f'{name}: missing file or unsupported symlink')
        files[name] = path.read_bytes()
        if path.suffix == '.md':
            try:
                docs[name] = markdown(files[name].decode())
            except ValueError as error:
                raise ValueError(f'{name}: {error}') from error
        if path.suffix == '.json':
            data[name] = json.loads(files[name])

    links = 0
    for name, (prose, _) in docs.items():
        for href in re.findall(r'\[[^\]\n]+\]\(([^)\n]+)\)', prose):
            url = urlsplit(href)
            if url.scheme or url.netloc:
                continue
            links += 1
            target = (ROOT / name).parent / unquote(url.path) if url.path else ROOT / name
            target = target.resolve()
            try:
                relative = target.relative_to(ROOT).as_posix()
            except ValueError as error:
                raise ValueError(f'{name}: link outside kit: {href}') from error
            if relative not in files:
                raise ValueError(f'{name}: unresolved link: {href}')
            if url.fragment and unquote(url.fragment) not in docs.get(relative, ('', set()))[1]:
                raise ValueError(f'{name}: unresolved anchor: {href}')

    manifest = data['manifest.json']
    prompts = sorted(n for n in files if n.startswith('prompts/') and n.endswith('.md'))
    if sorted(manifest['prompt_files']) != prompts or manifest['prompt_count'] != len(prompts):
        raise ValueError('manifest prompt inventory differs from prompt files')
    if not re.search(r'\bv' + re.escape(manifest['version']) + r'\b', files['README.md'].decode()):
        raise ValueError('README version differs from manifest')
    index = files['PROMPTS.md'].decode()
    if any(f']({p})' not in index for p in prompts):
        raise ValueError('prompt index omits a prompt')
    sources = manifest['sources']
    if len({s['id'] for s in sources}) != len(sources):
        raise ValueError('duplicate source IDs in manifest')
    source_text = files['SOURCES.md'].decode()
    sections = re.split(r'<a id="(r\d+)"></a>', source_text)
    source_sections = dict(zip(sections[1::2], sections[2::2]))
    if set(source_sections) != {s['id'].lower() for s in sources}:
        raise ValueError('source register IDs differ from manifest')
    for source in sources:
        if f']({source["url"]})' not in source_sections[source['id'].lower()]:
            raise ValueError(f'{source["id"]}: source URL differs from manifest')

    # Hash names and each file's content, excluding this generated report itself.
    digest = hashlib.sha256()
    for name, content in sorted(files.items()):
        if name != REPORT:
            digest.update(name.encode() + b'\0' + hashlib.sha256(content).digest())
    checks = {
        'file_count': len(files),
        'markdown_files': len(docs),
        'markdown_internal_links_resolved': links,
        'markdown_code_fences_balanced': True,
        'json_files_parse': len(data),
        'prompt_files_indexed': len(prompts),
        'source_records_consistent': len(sources),
        'readme_manifest_version_consistent': True,
    }
    if write_report:
        report = {
            'checked_at': datetime.now(timezone.utc).isoformat(timespec='seconds'),
            'package_version': manifest['version'],
            'scope': 'Offline local documentation integrity; no external or runtime validation.',
            'content_sha256': digest.hexdigest(),
            'digest_excludes': [REPORT],
            'checks': checks,
            'not_performed': [
                'External URL or factual validation by this checker',
                'JSON Schema validation or enforcement of completion gates',
                'Secret scanning or legal review',
                'Coding-agent installation, benchmarks or application deployment',
                'Remote GitHub verification by this checker',
            ],
        }
        (ROOT / REPORT).write_text(json.dumps(report, indent=2) + '\n')
    else:
        report = data[REPORT]
        if (report.get('package_version') != manifest['version']
                or report.get('content_sha256') != digest.hexdigest()
                or report.get('checks') != checks):
            raise ValueError('saved report is stale; review changes, then run with --write-report')
    print(json.dumps({'status': 'pass', 'version': manifest['version'], **checks}, indent=2))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write-report', action='store_true', help='refresh the saved report after checks pass')
    args = parser.parse_args()
    try:
        check(args.write_report)
    except (ValueError, KeyError, OSError, subprocess.CalledProcessError) as error:
        print(f'FAIL: {error}', file=sys.stderr)
        sys.exit(1)
