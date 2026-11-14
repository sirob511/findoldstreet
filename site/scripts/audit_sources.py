"""Inventory every captured source attempt and link it to published/review records."""
import collections
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
S = ROOT / 'data/sources'
rows = [r for name in ['UA','PL','ZA','VN','KZ','IN','international','places']
        for r in json.loads((ROOT / 'data' / (name+'.json')).read_text())]
by_url = collections.defaultdict(list)
for r in rows:
    for url in {s['url'] for s in r['sources']}:
        by_url[url].append(r)
notes = {
    'postal-classifier-documentation': 'Primary API documentation establishes OLDSTREET_UA/STREET_UA and OLDCITY_UA/CITY_UA previous/current name field semantics.',
    'postal-search': 'Official public lookup client; its read-only endpoint supplies the postal classifier captures.',
    'dnipro-museum-index': '622-entry discovery index examined. Conflicting field/prose pairs found in sample articles; first-pass imports use the explicit postal classifier fields instead.',
    'india-cities-2014': 'No-objection approvals are not proof of effective renaming. Final Karnataka mappings use PCGN confirmation.',
    'ukraine-factfile': 'Background naming/transliteration policy; city mappings use the official Ukrainian renamed-cities table.',
    'lodz-street-api': 'Inspected to locate municipal search; no name mappings in this JavaScript.',
    'lodz-current-streets': 'Municipal search landing page; actual current-name evidence captured separately from public endpoint.',
    'karnataka-renames': 'PDF captured but local text extraction failed; readable web-tool capture used instead.',
}
attempts = []
for manifest in sorted(S.glob('*manifest.json')):
    for item in json.loads(manifest.read_text()):
        used = by_url[item['url']]
        entry = dict(item, manifest=manifest.name,
                     publishedRecords=sum(r['status']=='verified' for r in used),
                     reviewRecords=sum(r['status']!='verified' for r in used))
        entry['assessment'] = notes.get(item['id']) or (
            'Cited by records; only explicit, reviewed mappings published.' if used else
            'City lookup context used to resolve official city, region and district IDs for the street query.' if item['id'].startswith('postal-') and '-cities-' in item['id'] else
            'Retrieval/extraction failed; no mappings published from this attempt.' if item.get('status')=='failed' else
            'Captured lead; no approved mapping currently cites this source. Requires row-level review before import.')
        if item.get('file') and item.get('sha256'):
            entry['captureHashVerified'] = hashlib.sha256((S / item['file']).read_bytes()).hexdigest() == item['sha256']
            assert entry['captureHashVerified'], item['id']
        attempts.append(entry)
manifest_urls = {a['url'] for a in attempts}
report = dict(asOf='2026-11-14', scope='All repository source manifests inventoried; this is not an exhaustive worldwide source census.',
              attempts=attempts, additionalRecordSources=[s for url in sorted(by_url) if url not in manifest_urls for s in [next(s for r in by_url[url] for s in r['sources'] if s['url']==url)]])
(ROOT / 'data/source-audit.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(f'Audited {len(attempts)} source attempts; {len(by_url)} distinct URLs cited by records.')
