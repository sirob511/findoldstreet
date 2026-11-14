"""Curate explicitly renamed cities from the public postal classifier.
Usage: python scripts/postal_places.py PASS CURRENT_CITY [CURRENT_CITY ...]
Only entries typed as cities, matching the requested current name and carrying
an explicit distinct former name, can be approved. Dates remain unknown.
"""
import hashlib
import json
import re
import sys
from postal_coverage import ROOT,S,fetch,clean,norm

def main():
    number,*cities=sys.argv[1:]
    existing=json.loads((ROOT/'data/places.json').read_text())
    approved=[];decisions=[];seen=set()
    for city in cities:
        key='postal-p'+number+'-place-'+hashlib.sha256(city.encode()).hexdigest()[:10]
        found=fetch(number,key,dict(method='get_city_by_region_id_and_district_id_and_city_ua',city_ua=city),f'Ukrposhta city address classifier: {city}')
        for r in found:
            if r.get('CITYTYPE_UA')!='місто' or r.get('CITY_UA')!=city:continue
            old,new=clean(r.get('OLDCITY_UA')),clean(r.get('CITY_UA'))
            if not old:continue
            outcome=dict(source=key,sourceCityId=r['CITY_ID'],formerName=old,currentName=new)
            identity=(r['REGION_ID'],norm(old),norm(new))
            if norm(old)==norm(new) or re.search(r'[,;/()]',old+new):
                decisions.append(outcome|dict(outcome='held',reason='No distinct unambiguous old/current pair.'));continue
            if identity in seen:
                decisions.append(outcome|dict(outcome='held',reason='Duplicate locality mapping.'));continue
            seen.add(identity)
            if any(p['country']=='UA' and p.get('kind')=='city' and any(norm(n) in {norm(old),norm(new)} for n in [p['formerName'],p['currentName'],*p.get('aliases',[])]) for p in existing):
                decisions.append(outcome|dict(outcome='held',reason='Overlaps an existing city record; retain its stable route.'));continue
            item=dict(country='UA',kind='city',formerName=old,currentName=new,
                      district=clean(r['DISTRICT_UA'])+' район · '+clean(r['REGION_UA'])+' область',
                      source=key,sourceCityId=r['CITY_ID'],aliases=[clean(r['CITY_EN'])] if clean(r.get('CITY_EN')) else [],
                      locator=f"Entry with CITY_ID={r['CITY_ID']}; OLDCITY_UA → CITY_UA; CITYTYPE_UA=місто",
                      nameNote='Previous and current city names recorded by Ukrposhta’s address classifier at retrieval. The source does not provide the effective rename date or legal instrument. Administrative labels follow the captured postal record; historical boundaries are not verified.')
            approved.append(item);decisions.append(outcome|dict(outcome='approved',reason='Explicit former/current city fields and city classification, with region retained.'))
        print(city,flush=True)
    (S/f'pass-{number}-places.json').write_text(json.dumps(approved,ensure_ascii=False,indent=2)+'\n')
    (S/f'pass-{number}-places-review.json').write_text(json.dumps(dict(approved=len(approved),decisions=decisions),ensure_ascii=False,indent=2)+'\n')
    print('Approved city mappings:',len(approved))

if __name__=='__main__':main()
