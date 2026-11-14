"""Deterministic city/country imports from individually reviewed source mappings."""
import hashlib
import json
from pathlib import Path
from unidecode import unidecode

ROOT = Path(__file__).resolve().parents[1]
SOURCES = ROOT / 'data/sources'


def build_places():
    from import_data import source, MAN, finalize
    seeds = json.loads((SOURCES / 'places-seed.json').read_text())
    rows = list(seeds)
    items=json.loads((SOURCES / 'places-reviewed.json').read_text())
    for path in sorted(SOURCES.glob('pass-*-places.json')):
        items += json.loads(path.read_text())
    for item in items:
        kind, country = item['kind'], item['country']
        old, new = item['formerName'], item['currentName']
        date = item.get('date')
        precision = {4: 'year', 7: 'month', 10: 'day'}.get(len(date or ''), 'unknown')
        event = dict(formerName=old, currentName=new, date=date, datePrecision=precision,
                     status=item.get('eventStatus', 'effective'), sourceUrl=MAN[item['source']]['url'],
                     locator=item['locator'], documentNumber=item.get('documentNumber'))
        if item.get('decisionDate'):
            event['decisionDate'] = item['decisionDate']
        evidence = [source(item['source'])]
        if item.get('extraSource'):
            evidence.append(source(item['extraSource']))
        identity = f"{kind}|{country}|{old}|{item.get('district', '')}"
        rows.append(dict(id=kind+'-'+hashlib.sha256(identity.encode()).hexdigest()[:16],
                         kind=kind, country=country, city=new if kind == 'city' else '',
                         district=item.get('district', ''), formerName=old, currentName=new,
                         aliases=item.get('aliases', []), transliterations=list(dict.fromkeys(
                             unidecode(n) for n in [old, new] if unidecode(n) != n)),
                         status='verified', segment=None, geometry=None, houseNumbersVerified=False,
                         currentStatusVerified=False, currentStatusNote='Source-supported name mapping; historical boundaries are not verified.',
                         events=[event], sources=evidence, nameNote=item.get('nameNote', '')))
    # Keep original routes and add captured supporting evidence to the initial records.
    for r in rows:
        if r['id'] in ['city-dnipro', 'city-kamianske']:
            r['sources'].append(source('ukraine-renamed-cities'))
        if r['id'] == 'country-eswatini':
            r['sources'].append(source('un-m49'))
    ids = [r['id'] for r in rows]
    assert len(ids) == len(set(ids)), 'Duplicate place identifiers'
    rows = finalize(rows)
    (ROOT / 'data/places.json').write_text(json.dumps(rows, ensure_ascii=False, indent=2)+'\n')
    return len(rows)


if __name__ == '__main__':
    print('Places:', build_places())
