"""Check approved postal mappings against captured response fields, never inferred names."""
import hashlib
import json
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
from postal_coverage import entries,clean,norm,TYPES
S=ROOT/'data/sources'
manifest={r['id']:r for f in S.glob('pass-*-manifest.json') for r in json.loads(f.read_text())}
rows={r['id']:r for r in json.loads((ROOT/'data/UA.json').read_text())}
count=0
for path in S.glob('pass-*-additions.json'):
    items=json.loads(path.read_text());review=json.loads(path.with_name(path.name.replace('-additions','-review')).read_text())
    assert len(items)==review['approved']
    approved={(r['source'],r['sourceStreetId']) for r in review['decisions'] if r['outcome']=='approved'}
    assert approved=={(r['source'],r['sourceStreetId']) for r in items}
    cache={}
    for item in items:
        source=manifest[item['source']]
        if source['id'] not in cache:
            data=(S/source['file']).read_bytes()
            assert hashlib.sha256(data).hexdigest()==source['sha256']
            cache[source['id']]={r['STREET_ID']:r for r in entries(json.loads(data))}
        raw=cache[source['id']][item['sourceStreetId']]
        r=rows['postal-ua-'+raw['STREET_ID']]
        assert r['formerName']==clean(raw['OLDSTREET_UA'])
        assert r['currentName']==clean(raw['STREETTYPE_UA'])+' '+clean(raw['STREET_UA'])
        assert r['city']==clean(raw['CITY_UA'])
        assert r['streetType'] in TYPES
        assert norm(r['formerName'])!=norm(raw['STREET_UA'])
        assert r['events'][0]['date'] is None and r['events'][0]['datePrecision']=='unknown'
        assert r['events'][0]['sourceUrl']==source['url']
        assert r['sourceStreetId'] in r['events'][0]['locator']
        assert r['geometry'] is None and r['houseNumbersVerified'] is False
        count+=1
print('Validated',count,'postal mappings against their captured fields and source hashes.')
