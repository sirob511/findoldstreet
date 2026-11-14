"""Replay approved, evidence-linked postal mappings without network requests."""
import json

def extend_postal(country,rows,record,sources):
    for path in sorted(sources.glob('pass-*-additions.json')):
        for item in json.loads(path.read_text()):
            if item['country']!=country:continue
            r=record(country,item['city'],item['formerName'],item['currentName'],item['source'],item['locator'],district=item['district'])
            r.update(id='postal-ua-'+item['sourceStreetId'],sourceStreetId=item['sourceStreetId'],
                     aliases=item.get('aliases',[]),locationAliases=item.get('locationAliases',[]),
                     streetType=item['streetType'],nameNote=item['nameNote'])
            rows.append(r)
    return rows
