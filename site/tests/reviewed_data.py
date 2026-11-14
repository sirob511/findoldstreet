"""Audit curated imports against their captured evidence and public records."""
import hashlib
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
sources = root / 'data/sources'
for name in ['expansion-manifest.json', 'lodz-manifest.json']:
    for entry in json.loads((sources / name).read_text()):
        assert hashlib.sha256((sources / entry['file']).read_bytes()).hexdigest() == entry['sha256'], entry['id']
rows = [r for c in ['UA','PL','ZA','IN'] for r in json.loads((root / 'data' / (c+'.json')).read_text())]
additions = json.loads((sources / 'reviewed-additions.json').read_text())
for item in additions:
    matches = [r for r in rows if (r['country'],r['city'],r['district'],r['formerName'],r['segment']) == (item['country'],item['city'],item.get('district'),item['formerName'],item.get('segment'))]
    assert len(matches) == 1, item
    r = matches[0]
    assert r['currentName'] == item['currentName']
    assert r['status'] == item.get('status','verified')
    assert r['sources'][0]['sha256'] and r['events'][0]['locator']
    assert r['houseNumbersVerified'] is False and r['geometry'] is None
    if item.get('year'):
        assert r['events'][0]['date'] == item['year']
        assert r['events'][0]['datePrecision'] == 'year'
assert len([i for i in additions if i['city']=='Łódź']) == 105
church = [r for r in rows if r['city']=='Pretoria' and r['formerName']=='Church Street']
assert len(church) == 4 and len({r['id'] for r in church}) == 4
assert all(r['segment'] for r in church)
assert len([r for r in church if r['status']=='review']) == 1
print(f"Validated {len(additions)} curated mappings and all captured-source hashes.")
