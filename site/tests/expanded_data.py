"""Validate expanded evidence, review exclusions and preservation of historical chains."""
import hashlib
import json
from pathlib import Path
R = Path(__file__).resolve().parents[1]
S = R / 'data/sources'
rows = [r for c in ['UA','PL','ZA','VN','KZ','IN','places'] for r in json.loads((R/'data'/f'{c}.json').read_text())]
for entry in json.loads((S/'coverage-expansion-manifest.json').read_text()):
    if entry.get('file') and entry.get('sha256'):
        assert hashlib.sha256((S/entry['file']).read_bytes()).hexdigest() == entry['sha256'], entry['id']
for item in json.loads((S/'coverage-additions.json').read_text()):
    matches = [r for r in rows if (r['country'],r['city'],r['district'],r['formerName'],r['segment']) == (item['country'],item['city'],item.get('district'),item['formerName'],item.get('segment'))]
    assert len(matches) == 1, item
    r = matches[0]
    assert r['status'] == item.get('status','verified')
    assert r['currentName'] == item['currentName']
    assert r['events'][-1]['currentName'] == r['currentName']
    for previous, following in zip(r['events'],r['events'][1:]):
        assert previous['currentName'] == following['formerName'], r['id']
for item in json.loads((S/'places-reviewed.json').read_text()):
    r, = [r for r in rows if r.get('kind')==item['kind'] and (r['country'],r['formerName'],r['district']) == (item['country'],item['formerName'],item.get('district',''))]
    assert r['currentName'] == item['currentName']
    assert r['events'][0]['date'] == item.get('date')
    assert r['sources'][0]['sha256']
    assert not r['currentStatusVerified'] and r['geometry'] is None
    if item.get('decisionDate'):
        assert r['events'][0]['decisionDate']==item['decisionDate']
        assert r['events'][0]['date'] is None, 'Decision date must not imply effective date'
for lang, text in json.loads((R/'src/i18n.json').read_text()).items():
    assert all(r['country'] in text['countryNames'] for r in rows), lang
print('Expanded mappings, event chains, date precision, source hashes and country labels validated.')
