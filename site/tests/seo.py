from pathlib import Path
from html.parser import HTMLParser
import json,xml.etree.ElementTree as ET
D=Path('dist');data=json.loads((D/'records.json').read_text());langs=list(json.loads((D/'i18n.json').read_text()))
class Links(HTMLParser):
 def __init__(self):super().__init__();self.links=[]
 def handle_starttag(self,tag,attrs):
  if tag=='link':self.links.append(dict(attrs))
for lang in langs:
 for r in [data[0],data[-1]]:
  p=D/lang/'street'/r['id']/'index.html';parser=Links();parser.feed(p.read_text());c=[x for x in parser.links if x.get('rel')=='canonical'];assert len(c)==1 and c[0]['href'].endswith(f'/{lang}/street/{r["id"]}/')
  assert set(x.get('hreflang') for x in parser.links if x.get('rel')=='alternate')==set(langs+['x-default'])
 root=ET.parse(D/f'sitemap-{lang}.xml').getroot()
 for loc in root.iter('{http://www.sitemaps.org/schemas/sitemap/0.9}loc'):
  from urllib.parse import urlsplit
  assert (D/urlsplit(loc.text).path.strip('/')/'index.html').exists(),loc.text
print('Canonical, reciprocal hreflang, and every locale sitemap target passed.')

for c in ['UA','PL','ZA','VN','KZ','IN']:
 for r in json.loads((Path('data')/(c+'.json')).read_text()):
  if r['status']!='verified':
   for lang in langs:assert not (D/lang/'street'/r['id']/'index.html').exists()
print('Review records have no published detail pages.')
