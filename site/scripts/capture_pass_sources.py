"""Capture public source responses separately from the deterministic import.
Usage: python scripts/capture_pass_sources.py pass-number sources.json
sources.json: [{id,url,country, ...optional provenance fields}]
Never automatically publishes downloaded mappings.
"""
import concurrent.futures
import datetime
import hashlib
import json
import sys
from pathlib import Path
import requests
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1] / 'data/sources'

def capture(item):
    entry = dict(item, retrievedAt=datetime.datetime.now(datetime.timezone.utc).isoformat(),
                 reuseTerms='Factual mappings only; capture retained for source audit, not served publicly.')
    try:
        response = requests.get(item['url'], timeout=25)
        response.raise_for_status()
        suffix = '.pdf' if response.content.startswith(b'%PDF') else '.zip' if response.content.startswith(b'PK') else '.html'
        target = ROOT / (item['id']+suffix)
        target.write_bytes(response.content)
        entry.update(file=target.name, sha256=hashlib.sha256(response.content).hexdigest(), status='downloaded')
        if suffix == '.html':
            text = BeautifulSoup(response.content,'html.parser').get_text('\n',strip=True)
        elif suffix == '.zip':
            return entry
        else:
            from pypdf import PdfReader
            text = '\n'.join(page.extract_text() or '' for page in PdfReader(target).pages)
        textfile = ROOT / (item['id']+'.txt')
        textfile.write_text(text)
        entry['textFile'] = textfile.name
    except Exception as exc:
        entry.update(status='failed',error=str(exc))
    return entry

if __name__ == '__main__':
    number, config = sys.argv[1:]
    target = ROOT / f'pass-{number}-manifest.json'
    previous = json.loads(target.read_text()) if target.exists() else []
    items = json.loads(Path(config).read_text())
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
        result = list(pool.map(capture,items))
    ids = {i['id'] for i in result}
    target.write_text(json.dumps([i for i in previous if i['id'] not in ids]+result,ensure_ascii=False,indent=2)+'\n')
    print([(r['id'],r['status']) for r in result])
