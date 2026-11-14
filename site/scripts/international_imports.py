"""Replay reviewed international pairs; source captures are never fetched at build time."""
import json
from import_data import D, S, record, finalize, source

def build_international():
    rows=[]
    for path in sorted(S.glob('international-pass-*-additions.json')):
        for item in json.loads(path.read_text()):
            r=record(item['country'],item['city'],item['formerName'],item['currentName'],item['source'],item['locator'],district=item.get('district'),segment=item.get('segment'))
            for key in ['aliases','locationAliases','nameNote','streetType','language','script']:
                if key in item:r[key]=item[key]
            r['sources'] += [source(key) for key in item.get('extraSources',[])]
            for key in ['decisionDate','documentNumber']:
                if key in item:r['events'][0][key]=item[key]
            if item.get('date'):
                r['events'][0].update(date=item['date'],datePrecision=item['datePrecision'])
            r['evidenceRow']=item.get('evidenceRow')
            r['coveragePass']=item['coveragePass']
            rows.append(r)
    assert len({r['id'] for r in rows})==len(rows),'Duplicate international identity'
    (D/'international.json').write_text(json.dumps(finalize(rows),ensure_ascii=False,indent=2)+'\n')
    return len(rows)
