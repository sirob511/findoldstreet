"""Capture and curate Ukrposhta's public previous/current address-name pairs.
The source documents OLDSTREET_UA as the previous Ukrainian street name.
No rename date, legal act, geometry, street segment or house correspondence is inferred.
Usage: python scripts/postal_coverage.py PASS CITY [CITY ...]
Review the per-pass decision file before importing.
"""
import collections
import datetime
import hashlib
import json
import re
import sys
import unicodedata
from pathlib import Path
from urllib.parse import urlencode
import requests

ROOT = Path(__file__).resolve().parents[1]
S = ROOT / 'data/sources'
BASE = 'https://index.ukrposhta.ua/endpoints-for-apps/index.php'
TYPES = {'вулиця','провулок','тупик','проспект','узвіз','площа','бульвар','проїзд','шосе','набережна','дорога','в’їзд',"в'їзд"}
PREFIX = r'^(?:вул(?:иця)?\.?|пров(?:улок)?\.?|просп(?:ект)?\.?|пр-т|пл(?:оща)?\.?|бульвар|бул\.?|узвіз|тупик|проїзд|шосе|набережна|наб\.?|в[’\x27]їзд)\s+'

def clean(value):
    return ' '.join(value.split()) if isinstance(value,str) else ''

def norm(value):
    value=unicodedata.normalize('NFKC',clean(value)).lower().replace('’',"'").replace('`',"'").replace('ʼ',"'")
    value=re.sub(PREFIX,'',value)
    return re.sub(r'[^\w\s-]','',value).strip()

def entries(payload):
    data=payload.get('Entries',payload).get('Entry',[])
    return [data] if isinstance(data,dict) else data

def fetch(pass_number,key,params,title):
    url=BASE+'?'+urlencode(params)
    response=requests.get(url,timeout=30)
    response.raise_for_status()
    data=response.json()
    filename=key+'.json'
    # Preserve the exact JSON response bytes, not a reconstructed payload.
    (S/filename).write_bytes(response.content)
    entry=dict(id=key,country='UA',title=title,url=url,file=filename,
               sha256=hashlib.sha256(response.content).hexdigest(),status='downloaded',
               retrievedAt=datetime.datetime.now(datetime.timezone.utc).isoformat(),
               reuseTerms='Factual address-name mappings only; source response retained for audit, not served publicly.',
               retrievalMethod='Public read-only endpoint used by index.ukrposhta.ua; no authentication required.')
    path=S/f'pass-{pass_number}-manifest.json'
    manifest=json.loads(path.read_text()) if path.exists() else []
    manifest=[m for m in manifest if m['id']!=key]+[entry]
    path.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
    return entries(data)

def curate(raw,existing):
    candidates=[]; decisions=[]
    for x,key in raw:
        old,new,typ=map(clean,[x.get('OLDSTREET_UA'),x.get('STREET_UA'),x.get('STREETTYPE_UA')])
        if not old:continue
        row=dict(source=key,sourceStreetId=clean(x['STREET_ID']),city=clean(x['CITY_UA']),formerName=old,currentName=typ+' '+new)
        reason=None
        if typ not in TYPES:reason='Non-street object type excluded from street lookup.'
        elif not new or norm(old)==norm(new):reason='No distinct old/current name pair.'
        elif re.search(r'[,;/()]',old+new):reason='Compound history or locality/segment qualifier requires individual review.'
        elif re.search(r'частин|колишн|без назв|не має|б/н|новий проїзд',old,re.I):reason='Partial, unnamed or descriptive previous-name field requires review.'
        if reason:
            decisions.append(row|dict(outcome='held',reason=reason));continue
        row['_raw']=x;row['_type']=typ;row['_old']=norm(old);row['_new']=norm(new)
        candidates.append(row)
    # Distinct postal IDs do not automatically establish distinct renamed streets.
    by_old=collections.defaultdict(set);by_new=collections.defaultdict(set)
    for r in candidates:
        scope=(r['city'],r['_type'])
        by_old[scope+(r['_old'],)].add(r['_new'])
        by_new[scope+(r['_new'],)].add(r['_old'])
    seen=set();approved=[]
    for row in candidates:
        scope=(row['city'],row['_type']);pair=scope+(row['_old'],row['_new']);x=row.pop('_raw')
        reason=None
        if len(by_old[scope+(row['_old'],)])>1 or len(by_new[scope+(row['_new'],)])>1:
            reason='Names collide across postal IDs; separate objects versus historical chains unresolved.'
        elif pair in seen:reason='Duplicate name mapping in the same locality and street type.'
        else:
            for r in existing:
                if r.get('kind') or r['country']!='UA' or r['city']!=row['city']:continue
                if norm(r['formerName'])==row['_old'] or norm(r['currentName'])==row['_new']:
                    reason='Overlaps an existing record; keep its stable route and individually reconcile evidence.';break
        seen.add(pair)
        if reason:
            decisions.append({k:v for k,v in row.items() if not k.startswith('_')}|dict(outcome='held',reason=reason));continue
        aliases=[clean(x.get(k)) for k in ['STREET_EN','OLDSTREET_EN'] if clean(x.get(k))]
        item=dict(country='UA',city=row['city'],district=clean(x['DISTRICT_UA'])+' район · '+clean(x['REGION_UA'])+' область',
                  formerName=row['formerName'],currentName=row['currentName'],source=row['source'],
                  sourceStreetId=row['sourceStreetId'],streetType=row['_type'],
                  locator=f"Entry with STREET_ID={row['sourceStreetId']}; OLDSTREET_UA → STREET_UA, STREETTYPE_UA; CITY_ID={x['CITY_ID']}",
                  aliases=aliases,locationAliases=[clean(x.get('CITY_EN'))],
                  nameNote='Previous and current names as recorded by Ukrposhta’s address classifier at retrieval. Rename date and legal decision are not supplied. The previous street type is retained only where explicitly present in the source. Regional/district labels follow the postal source; street geometry and house-number continuity are not verified.')
        approved.append(item)
        decisions.append({k:v for k,v in row.items() if not k.startswith('_')}|dict(outcome='approved',reason='Explicit previous/current fields; no conflicting or duplicate name mapping in this captured city response.'))
    return approved,decisions

def main():
    number,*cities=sys.argv[1:]
    existing=[r for c in ['UA','PL','ZA','VN','KZ','IN','places'] for r in json.loads((ROOT/'data'/f'{c}.json').read_text())]
    raw=[]
    for city in cities:
        slug=hashlib.sha256(city.encode()).hexdigest()[:10]
        found=fetch(number,f'postal-p{number}-cities-{slug}',dict(method='get_city_by_region_id_and_district_id_and_city_ua',city_ua=city),f'Ukrposhta city search: {city}')
        matches=[c for c in found if c['CITY_UA']==city and c['CITYTYPE_UA']=='місто']
        assert len(matches)==1,(city,len(matches))
        c=matches[0];key=f"postal-p{number}-streets-{c['CITY_ID']}"
        streets=fetch(number,key,dict(method='get_street_by_region_id_and_district_id_and_city_id_and_street_ua',region_id=c['REGION_ID'],district_id=c['DISTRICT_ID'],city_id=c['CITY_ID'],street_ua=''),f'Ukrposhta street address classifier: {city}')
        assert all(x['CITY_ID']==c['CITY_ID'] for x in streets)
        raw += [(s,key) for s in streets]
        print(city,len(streets),'streets;',sum(bool(clean(s.get('OLDSTREET_UA'))) for s in streets),'previous names',flush=True)
    approved,decisions=curate(raw,existing)
    (S/f'pass-{number}-additions.json').write_text(json.dumps(approved,ensure_ascii=False,indent=2)+'\n')
    (S/f'pass-{number}-review.json').write_text(json.dumps(dict(target=500,cities=cities,approved=len(approved),decisions=decisions),ensure_ascii=False,indent=2)+'\n')
    print('Approved',len(approved),'held',len(decisions)-len(approved))

if __name__=='__main__':main()
