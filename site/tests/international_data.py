"""Check every published international pair against its captured evidence and ledger."""
import hashlib,json,sys
from pathlib import Path
from bs4 import BeautifulSoup
R=Path(__file__).resolve().parents[1];S=R/'data/sources'
sys.path.insert(0,str(R/'scripts'))
from international_coverage import table,clean,wroclaw_register,polish_key,vilnius_register
rows=json.loads((R/'data/international.json').read_text());by_id={r['id']:r for r in rows}
assert len(by_id)==len(rows)
man={s['id']:s for p in S.glob('*manifest.json') for s in json.loads(p.read_text())}
tables={}
digests={}
import pymupdf
from moldova_estonia_coverage import guide_inventory,destination_key,tallinn_inventory,tallinn_pairs
guide=pymupdf.open(S/'chisinau-library-guide.pdf')
guide_names=guide_inventory(guide)
eki_names=tallinn_inventory();eki_pairs=tallinn_pairs()
from brno_coverage import brno_index,profile
brno=brno_index()
register=wroclaw_register()
vilnius_names=vilnius_register()
count=0
for p in S.glob('international-pass-*-additions.json'):
    items=json.loads(p.read_text());ledger=json.loads(p.with_name(p.name.replace('additions','review')).read_text())
    assert len(items)==ledger['approved']
    assert ledger['candidates']==ledger['approved']+ledger['held']
    for item in items:
        matches=[r for r in rows if (r['country'],r['city'],r['district'],r['formerName'])==(item['country'],item['city'],item.get('district'),item['formerName'])]
        assert len(matches)==1,item
        r=matches[0];assert r['currentName']==item['currentName']
        assert r['events'][-1]['currentName']==r['currentName']
        assert r['events'][0]['date']==item.get('date')
        assert not r['currentStatusVerified'] and r['geometry'] is None and not r['houseNumbersVerified']
        for source in r['sources']:
            m=man[source['id']]
            if source['id'] not in digests:digests[source['id']]=hashlib.sha256((S/m['file']).read_bytes()).hexdigest()
            assert source['sha256']==digests[source['id']]
        if item['source']=='tashkent-goldenpages':
            if item['source'] not in tables:tables[item['source']]=table(item['source'])
            c=tables[item['source']][item['evidenceRow']]
            assert c==item['sourceCells']
            assert (r['formerName'],r['currentName'],r['district'])==(c[0],c[1],c[3] or None)
        if item['source']=='wroclaw-historical-pairs':
            if item['source'] not in tables:tables[item['source']]=table(item['source'])
            c=tables[item['source']][item['evidenceRow']]
            assert c==item['sourceCells']
            assert r['formerName']==c[0].removesuffix(' in Breslau') and r['currentName']==c[1]
            candidates=[v for v in register[polish_key(c[1])].values() if v[1]==c[1].split()[0]]
            assert len(candidates)==1 and candidates[0][0]==item['municipalRegisterId']
            assert r['streetType']==candidates[0][1]
        if item['source']=='vilnius-historical-table':
            if 'vilnius' not in tables:
                soup=BeautifulSoup((S/'vilnius-historical-table.html').read_bytes(),'html.parser')
                tables['vilnius']=[[clean(c.get_text(' ',strip=True)) for c in tr.find_all('td',recursive=False)] for tr in soup.select('#fundsTable tr')]
            c=tables['vilnius'][item['evidenceRow']];assert c==item['sourceCells']
            assert r['currentName']==c[0]
            assert r['formerName'] in ([c[1]] if item['evidenceField']=='pre-1987' else [x.strip() for x in c[3].split(',')])
            from international_coverage import norm
            assert len(vilnius_names[norm(r['currentName'])])==1
            assert item['addressRegisterStreetCode'] in vilnius_names[norm(r['currentName'])]
        if item['source'].startswith('brno-profile-'):
            sid=item['source'].removeprefix('brno-profile-')
            if sid not in tables:tables[sid]=profile(sid)
            title,district,history=tables[sid]
            assert not brno[sid]['abolished']
            assert not any(token in r['formerName'] for token in ['+',',',' – ',' — '])
            assert r['formerName']!='Samoty'
            assert title==brno[sid]['name']==r['currentName']==history[-1]['label']
            assert district==r['district'] and history==item['sourceHistory']
            assert history[item['evidenceRow']]['label']==r['formerName']
        if item['source']=='chisinau-library-guide':
            page=guide[item['evidencePage']]
            cells=[clean(page.get_text('text',clip=pymupdf.Rect(box))) for box in item['evidenceBoxes']]
            assert cells==item['sourceCells']==[r['formerName'],r['currentName']]
            assert len(guide_names[destination_key(r['currentName'])])==1
            assert r['events'][0]['date'] is None
        if item['source']=='tallinn-eki-renames':
            heading,old=eki_pairs[item['evidenceRow']]
            assert [heading,old]==item['sourceCells']
            assert r['currentName'] in eki_names and r['district']==eki_names[r['currentName']]
            import re
            assert r['formerName']==clean(re.sub(r'\[[^\]]*\]','',old))
            assert ' osa' not in r['formerName']
        count+=1
assert count==len(rows)
for locale,t in json.loads((R/'src/i18n.json').read_text()).items():
    assert all(r['country'] in t['countryNames'] for r in rows),locale


# Unchanged source rows are not intermediate rename steps.
from international_coverage import screen
sample=[dict(city='Example',formerName='Old',currentName='Current'),dict(city='Example',formerName='Current',currentName='Current')]
screen(sample)
assert sample[0]['decision']=='approved' and sample[1]['decision']=='held'

# The guide itself shows this destination is outdated; do not publish the stale index pair.
assert not any(r['country']=='MD' and r['currentName']=='Cosmonauților' for r in rows)
ledger=json.loads((S/'international-pass-10-review.json').read_text())
killustiku=next(r for r in ledger['decisions'] if r['country']=='EE' and r['formerName']=='Killustiku põik')
assert killustiku['decisionDate']=='1990-08-03'
assert killustiku['date']=='1992-01-01'
assert killustiku['decision']=='held'  # The old/current name reuse needs historical identity reconciliation.

print(f'{count} international pairs: source hashes, exact fields, ledger counts, dates and locale labels validated.')
