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
        assert r['district']==clean(raw['DISTRICT_UA'])+' район · '+clean(raw['REGION_UA'])+' область'
        assert r['streetType'] in TYPES
        assert norm(r['formerName'])!=norm(raw['STREET_UA'])
        assert r['events'][0]['date'] is None and r['events'][0]['datePrecision']=='unknown'
        assert r['events'][0]['sourceUrl']==source['url']
        assert r['sourceStreetId'] in r['events'][0]['locator']
        assert r['geometry'] is None and r['houseNumbersVerified'] is False
        count+=1
print('Validated',count,'postal mappings against their captured fields and source hashes.')

# Identical city names must never silently select a different region.
from postal_coverage import resolve_city,curate
homonyms=[dict(CITY_UA='Миколаїв',CITYTYPE_UA='місто',REGION_UA=region,CITY_ID=str(i)) for i,region in enumerate(['Львівська','Миколаївська'])]
try:
    resolve_city(homonyms,'Миколаїв')
    raise AssertionError('Ambiguous city was silently selected')
except ValueError:
    pass
assert resolve_city(homonyms,'Миколаїв::Миколаївська')['CITY_ID']=='1'

# Same street names in two genuinely distinct source regions remain separate.
raw=[]
for i,c in enumerate(homonyms):
    raw.append((c|dict(STREET_ID=str(i),STREETTYPE_UA='вулиця',OLDSTREET_UA='Стара',STREET_UA='Нова',DISTRICT_UA='Район'),'example'))
approved,_=curate(raw,[])
assert len(approved)==2 and approved[0]['district']!=approved[1]['district']

places=json.loads((ROOT/'data/places.json').read_text())
place_count=0
for path in S.glob('pass-*-places.json'):
    review=json.loads(path.with_name(path.stem+'-review.json').read_text())
    items=json.loads(path.read_text());assert len(items)==review['approved']
    for item in items:
        m=manifest[item['source']];data=(S/m['file']).read_bytes()
        assert hashlib.sha256(data).hexdigest()==m['sha256']
        raw,=[r for r in entries(json.loads(data)) if r['CITY_ID']==item['sourceCityId']]
        r,=[p for p in places if p.get('kind')=='city' and p['country']=='UA' and p['formerName']==item['formerName'] and p['district']==item['district']]
        assert raw['CITYTYPE_UA']=='місто'
        assert r['formerName']==clean(raw['OLDCITY_UA']) and r['currentName']==clean(raw['CITY_UA'])
        assert clean(raw['REGION_UA']) in r['district']
        assert r['events'][0]['date'] is None and r['events'][0]['sourceUrl']==m['url']
        assert raw['CITY_ID'] in r['events'][0]['locator']
        place_count+=1
print('Validated',place_count,'additional city mappings; homonymous cities require explicit regions.')
