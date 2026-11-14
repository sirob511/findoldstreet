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
  assert set(x.get('hreflang') for x in parser.links if x.get('rel')=='alternate' and x.get('hreflang'))==set(langs+['x-default'])
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

import re
from urllib.parse import urlsplit
origin = urlsplit(ET.parse(D/'sitemap-en.xml').getroot()[0][0].text)
origin = f'{origin.scheme}://{origin.netloc}'
assert f'Sitemap: {origin}/sitemap.xml' in (D/'robots.txt').read_text()
assert 'User-agent: *\nAllow: /' in (D/'robots.txt').read_text()
assert origin + '/records.json' in (D/'llms.txt').read_text()
for lang in langs:
 for suffix in ['', 'coverage/', 'about/', f'street/{data[0]["id"]}/']:
  page=(D/lang/suffix/'index.html').read_text()
  graph=json.loads(re.search(r'<script type="application/ld\+json">(.*?)</script>',page).group(1))['@graph']
  webpage=next(x for x in graph if x['@type']=='WebPage')
  assert webpage['url']==f'{origin}/{lang}/{suffix}'
  assert webpage['inLanguage']==lang
  assert 'property="og:url"' in page and 'name="twitter:card"' in page
  if suffix.startswith('street/'):
   assert webpage['citation'] and webpage['about']['name']==data[0]['currentName']
   assert data[0]['formerName'] in webpage['description']
  if suffix=='coverage/':assert webpage['mainEntity']['distribution']['contentUrl']==origin+'/records.json'
assert 'noindex, follow' in (D/'404.html').read_text()
print('Structured data, social metadata, crawler access, and machine-readable discovery passed.')

assert json.loads((D/'coverage-report.json').read_text())
