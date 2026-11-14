"""Explicitly reviewed factual mappings, replayed by the deterministic importer."""
import json


def extend_reviewed(country, rows, record, sources, source):
    additions = json.loads((sources / 'reviewed-additions.json').read_text())
    identities = {(r['city'], r['district'], r['formerName'], r['segment']) for r in rows}
    for item in additions:
        if item['country'] != country:
            continue
        identity = (item['city'], item.get('district'), item['formerName'], item.get('segment'))
        if identity in identities:
            raise ValueError(f'Duplicate reviewed mapping: {identity}')
        identities.add(identity)
        r = record(country, item['city'], item['formerName'], item['currentName'], item['source'], item['locator'],
                   district=item.get('district'), segment=item.get('segment'), status=item.get('status', 'verified'),
                   document=item.get('documentNumber'))
        r['aliases'] = item.get('aliases', [])
        if item.get('streetType'):
            r['streetType'] = item['streetType']
        if item.get('year'):
            r['events'][0]['date'] = item['year']
            r['events'][0]['datePrecision'] = 'year'
        if item.get('extraSource'):
            r['sources'].append(source(item['extraSource']))
        for field in ['decisionDate', 'ceremonyDate']:
            if item.get(field):
                r['events'][0][field] = item[field]
        if item.get('reviewReason'):
            r['reviewReason'] = item['reviewReason']
        rows.append(r)
    return rows
