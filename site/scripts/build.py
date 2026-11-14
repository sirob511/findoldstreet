import json,pathlib,html,shutil,os,collections,hashlib,urllib.parse
from seo import site_origin, metadata
ORIGIN=site_origin()
R=pathlib.Path(__file__).resolve().parents[1];D=R/'dist'
if D.exists():shutil.rmtree(D)
D.mkdir()
T=json.loads((R/'src/i18n.json').read_text()); ALL=sum([json.loads((R/'data'/f'{c}.json').read_text()) for c in ['UA','PL','ZA','VN','KZ','IN','international','places']],[]);DATA=[r for r in ALL if r['status']=='verified']
COUNTRIES=list(dict.fromkeys(r['country'] for r in DATA));COUNTRY_ALIASES=T['en']['countryNames']
def e(x):return html.escape(str(x or ''),quote=True)
def city_id(r):return r['country'].lower()+'-'+hashlib.sha256(r['city'].encode()).hexdigest()[:10]
def map_url(r):return 'https://www.openstreetmap.org/search?query='+urllib.parse.quote(', '.join(dict.fromkeys(filter(None,[r['currentName'],r['city'],COUNTRY_ALIASES[r['country']]]))))
def path(lang,suffix=''):return f'/{lang}/{suffix}'
def record_path(r):return ('place/' if r.get('kind') else 'street/')+r['id']+'/'
def card(r,l):
 t=T[l];url=path(l,record_path(r));kind=r.get('kind','street')
 location=' · '.join(filter(None,[t[kind+'TypeLabel'],r['city'],r['district'],t['countryNames'][r['country']]]))
 return f'<article class="answer-row"><div><div class="answer-names"><span>{e(r["formerName"])}</span><span class="answer-arrow"> → </span><strong>{e(r["currentName"])}</strong></div><p>{e(location)}{(" · "+e(t["partial"])) if r.get("segment") else ""}</p></div><a class="detail-link" href="{url}">{e(t["detail"])} →</a></article>'
def lookup(l,interactive=False):
 t=T[l]
 return f'<form {"id=searchform" if interactive else ""} class="lookup-form" action="/{l}/" method="get"><label class="sr-only" for="query">{e(t["query"])}</label><div class="lookup-controls"><input id="query" name="q" type="search" placeholder="{e(t["placeholder"])}" autocomplete="off"><button class="primary" type="submit">{e(t["submit"])}</button></div></form>'
def shell(l,suffix,title,body,app=False,noindex=False,description=None,record=None):
 description=description or (T[l]["intro"] if not suffix else title+". "+T[l]["intro"])
 seo=metadata(ORIGIN,l,suffix,title,description,record,noindex)
 t=T[l];langs=''.join(f'<option value="{k}" {"selected" if k==l else ""}>{v["name"]}</option>' for k,v in T.items());alt=''.join(f'<link rel="alternate" hreflang="{k}" href="{ORIGIN}{path(k,suffix)}">' for k in T)
 brand=f'<a class="brand" href="/{l}/"><span class="brandmark" aria-hidden="true">↱</span>FindOldStreet<em>.</em></a>'
 return f'''<!doctype html><html lang="{l}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>{e(title)} | FindOldStreet</title><meta name="description" content="{e(description)}"><link rel="canonical" href="{ORIGIN}{path(l,suffix)}">{alt}<link rel="alternate" hreflang="x-default" href="{ORIGIN}{path('en',suffix)}">{seo}<meta name="theme-color" content="#245b48"><link rel="icon" href="/favicon.svg"><link rel="stylesheet" href="/style.css"><link rel="alternate" type="application/json" href="/records.json" title="Documented place renamings"></head><body><a class="skip" href="#main">{e(t['skip'])}</a><header><div class="wrap"><div class="nav">{brand}<label class="language-label">{e(t['languages'])}<select class="language" id="locale" aria-label="{e(t['languages'])}">{langs}</select></label></div></div></header><main class="wrap" id="main">{body}<div class="sharetools"><button type="button" class="clear" id="copylink" data-copied="{e(t['copied'])}" data-failed="{e(t['copyFailed'])}" hidden>{e(t['copyLink'])}</button><span id="copystatus" role="status"></span></div><footer class="footer">{brand}<span>{e(t['footer'])}</span><a href="/{l}/coverage/">{e(t['coverage'])} ↗</a><a href="https://oddlogic.ai" target="_blank" rel="noopener">powered by oddlogic.ai</a></footer></main><script type="module" src="/app.mjs"></script></body></html>'''
def write(p,s):
 p=D/p;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(s)
for l,t in T.items():
 countries=''.join(f'<a class="countrycard" href="/{l}/?country={c}#results"><span class="countrydot">{c}</span><strong>{e(t["countryNames"][c])}</strong><b>{sum(r["country"]==c for r in DATA)}</b><br><small>{e(t["count"])}</small></a>' for c in COUNTRIES)
 body=f'''<section class="lookup-hero"><h1>{e(t['heading'])}</h1><p class="intro">{e(t['intro'])}</p>{lookup(l,True)}<div class="examples"><button class="example" type="button" data-query="Pushkinskaya, Kyiv">Pushkinskaya, Kyiv ↗</button><button class="example" type="button" data-query="Dnipropetrovsk">Dnipropetrovsk ↗</button></div><noscript><p><a href="/{l}/coverage/">{e(t['browse'])} · {e(t['coverage'])} →</a></p></noscript></section><section id="results" hidden><div class="sectiontop"><h2>{e(t['results'])} <span id="resultcount" role="status" aria-live="polite" aria-atomic="true"></span></h2><button class="clear" id="clear" hidden>{e(t['clear'])}</button></div><div id="disambiguation" hidden><p>{e(t['chooseLocation'])}</p><div class="chips" id="locations"></div></div><div class="answer-list" id="resultgrid"></div><div id="empty" class="empty" hidden>{e(t['empty'])}<p><a href="/{l}/coverage/">{e(t['coverage'])} →</a></p></div><button class="more" id="more" hidden>{e(t['loadMore'])}</button></section><section><div class="sectiontop"><h2>{e(t['browse'])}</h2><a href="/{l}/coverage/">{e(t['coverage'])} ↗</a></div><div class="countries">{countries}</div></section><section class="citybrowse"><details><summary>{e(t['browse'])} · {e(t['municipalities'])}</summary><div class="citylinks">{''.join(f'<a href="/{l}/city/{city_id(r)}/">{e(r["city"])} · {e(t["countryNames"][r["country"]])}</a>' for r in sorted({(r['country'],r['city']):r for r in DATA if r['city']}.values(),key=lambda r:r['city']))}</div></details></section><section class="method"><div><div class="eyebrow">{e(t['about'])}</div><h2>{e(t['methodTitle'])}</h2></div><div><p>{e(t['methodText'])}</p><p>{e(t['mapText'])}</p><a href="/{l}/coverage/">{e(t['scope'])} →</a></div></section>'''
 write(f'{l}/index.html',shell(l,'',t['search'],body,True))
 for r in DATA:
  history=''
  for ev in r['events']:
   dateLabel=t['date'];date=ev.get('date')
   if not date and ev.get('decisionDate'):dateLabel=t['decision'];date=ev['decisionDate']
   if not date and ev.get('ceremonyDate'):dateLabel=t['ceremony'];date=ev['ceremonyDate']
   history+=f'<li><small>{e(dateLabel)}: {e(date or t["unknown"])}</small><div class="from">{e(ev["formerName"])}</div><strong>→ {e(ev["currentName"])}</strong>{f"<span class=badge>{e(t['reversal'])}</span>" if ev['status']=='reversal' else ''}<a href="{e(ev["sourceUrl"])}" target="_blank" rel="noopener">{e(t["source"])} ↗</a><small> · {e(ev["locator"])} {e(ev.get("documentNumber"))}</small></li>'
  sources=''.join(f'<div class="sourceitem"><a href="{e(s["url"])}" target="_blank" rel="noopener">{e(urllib.parse.urlparse(s["url"]).netloc)} ↗</a><small>{e(s["retrievedAt"][:10])}</small></div>' for s in r['sources'])
  seg=f'<div class="segment"><strong>{e(t["partial"])}</strong><br>{e(r["segment"])}</div>' if r.get('segment') else ''
  body=f'''<div class="pagehead"><a class="back" href="/{l}/">← {e(t['back'])}</a><h1>{e(r['formerName'])} <span>→</span> {e(r['currentName'])}</h1><p>{e(t[r.get('kind','street')+'TypeLabel'])} · {e(' · '.join(filter(None,[r['city'],t['countryNames'][r['country']]])))} <span class="checked"> · ✓ {e(t['verified'])}</span></p></div><div class="detail-search">{lookup(l)}</div><div class="detailgrid"><div><section class="panel"><h2>{e(t['history'])}</h2><ol class="timeline">{history}</ol>{("<p class=note>"+e(r.get("nameNote"))+"</p>") if r.get("nameNote") else ""}</section><section class="panel"><h2>{e(t['evidence'])}</h2>{sources}<p>{e(t['freshness'])}</p><p>{e(t['sourceName'])}</p>{f'<details><summary>{e(t["translit"])}</summary><p>{e(" · ".join(r["transliterations"]))}</p></details>' if r['transliterations'] else ''}</section></div><aside><section class="panel"><h2>{e(t['current'])}</h2><div class="currentname">{e(r['currentName'])}</div><dl class="metadata"><div><dt>{e(t['locality'])}</dt><dd>{e(r['city'] or t['countryNames'][r['country']])}</dd></div><div><dt>{e(t['district'])}</dt><dd>{e(r['district'] or t['notRecorded'])}</dd></div></dl>{seg}<a class="primary" href="{map_url(r)}" target="_blank" rel="noopener">{e(t['map'])} ↗</a>{('<div class=note>'+e(t['streetOnly'])+'</div>') if not r.get('kind') else ''}<p>{e(t['mapText'])}</p></section></aside></div>'''
  write(f'{l}/{record_path(r)}index.html',shell(l,record_path(r),f'{r["formerName"]} → {r["currentName"]}',body,description=f'{r["formerName"]} → {r["currentName"]}. '+t['history']+'. '+t['freshness'],record=r))
 groups=collections.defaultdict(list)
 for r in DATA:
  if r['city']:groups[(r['country'],r['city'])].append(r)
 rows=''
 for (c,city),rr in sorted(groups.items()):
  rows+=f'<tr><td>{e(t["countryNames"][c])}</td><td><a href="/{l}/city/{city_id(rr[0])}/">{e(city)}</a></td><td>{len(rr)}</td><td>{sum(len(r["events"]) for r in rr)}</td><td>{sum(r["country"]==c and r["city"]==city and r["status"]!="verified" for r in ALL)}</td></tr>'
  body=f'<div class="pagehead"><a class="back" href="/{l}/coverage/">← {e(t["coverage"])}</a><h1>{e(city)}</h1><p>{len(rr)} {e(t["count"])} · {e(t["countryNames"][c])}</p></div><div class="answer-list">'+''.join(card(r,l) for r in rr)+'</div>'
  write(f'{l}/city/{city_id(rr[0])}/index.html',shell(l,'city/'+city_id(rr[0])+'/',city+' · '+t['search'],body))
 numbers=f'<div class="numbers"><div><b>{len(DATA)}</b><span>{e(t["count"])}</span></div><div><b>{len(groups)}</b><span>{e(t["municipalities"])}</span></div><div><b>{sum(len(r["events"]) for r in DATA)}</b><span>{e(t["events"])}</span></div><div><b>{len(ALL)-len(DATA)}</b><span>{e(t["review"])}</span></div></div>'
 body=f'<div class="pagehead"><div class="eyebrow">{e(t["coverage"])}</div><h1>{e(t["scope"])}</h1><p>{e(t["scopeText"])}</p>{numbers}</div><section class="panel tablewrap"><table><thead><tr><th>{e(t["all"])}</th><th>{e(t["locality"])}</th><th>{e(t["count"])}</th><th>{e(t["events"])}</th><th>{e(t["review"])}</th></tr></thead><tbody>{rows}</tbody></table></section><p>{e(t["freshness"])}</p><p>{e(t["streetOnly"])}</p><a class="primary" href="/coverage-report.json" download>{e(t["download"])} ↓</a><p>{e(t["languages"])}: {e(" · ".join(x["name"] for x in T.values()))}</p>'
 body+='<div class=answer-list>'+''.join(card(r,l) for r in DATA if r.get('kind')=='country')+'</div>'
 write(f'{l}/coverage/index.html',shell(l,'coverage/',t['coverage'],body))
 body=f'<div class="pagehead"><div class="eyebrow">{e(t["about"])}</div><h1>{e(t["methodTitle"])}</h1></div><section class="panel"><h2>{e(t["evidence"])}</h2><p>{e(t["methodText"])}</p><p>{e(t["freshness"])}</p><h2>{e(t["map"])}</h2><p>{e(t["mapText"])}</p><p>{e(t["streetOnly"])}</p><h2>{e(t["languages"])}</h2><p>{e(t["sourceName"])}</p><h2>{e(t["coverage"])}</h2><p>{e(t["scopeText"])}</p><a href="/{l}/coverage/">{e(t["coverage"])} →</a></section>'
 write(f'{l}/about/index.html',shell(l,'about/',t['about'],body))
 urls=['', 'coverage/', 'about/']+[record_path(r) for r in DATA]+['city/'+city_id(rr[0])+'/' for rr in groups.values()]
 write(f'sitemap-{l}.xml','<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join(f'<url><loc>{ORIGIN}/{l}/{u}</loc></url>' for u in urls)+'</urlset>')
write('sitemap.xml','<?xml version="1.0" encoding="UTF-8"?><sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join(f'<sitemap><loc>{ORIGIN}/sitemap-{l}.xml</loc></sitemap>' for l in T)+'</sitemapindex>')
write('robots.txt',f'User-agent: *\nAllow: /\nSitemap: {ORIGIN}/sitemap.xml\n')
# Optional machine-readable orientation; crawlable HTML and sitemaps remain primary.
write('llms.txt',f'''# FindOldStreet

> Source-backed lookup of documented place renamings. Coverage is incomplete.

## Browse
- [Search]({ORIGIN}/en/): Search former names, aliases, and localities.
- [Coverage]({ORIGIN}/en/coverage/): {len(DATA)} published records in {len(groups)} localities across {len(COUNTRIES)} countries.
- [Methodology]({ORIGIN}/en/about/): Evidence standards and limitations.
- [Sitemap]({ORIGIN}/sitemap.xml): All published locale, street, and city pages.

## Data
- [Records]({ORIGIN}/records.json): JSON with stable IDs, rename history, source URLs, dates, and verification flags.
- [Coverage report]({ORIGIN}/coverage-report.json): Coverage counts and source limitations.

## Interpretation
- A documented rename is not proof of present-day official map identity.
- House numbers and geometry are not verified. Do not infer house-number equivalence.
- Partial renamings apply only to the stated segment.
- Decision dates and ceremony dates are distinct from effective dates; unknown dates remain null.
- Cite the relevant /en/street/{{id}}/ page and its original evidence.
- Source-language names are preserved; transliterations are search aids.
- The published dataset excludes records awaiting review.
''')
write('index.html',(D/'en/index.html').read_text().replace(f'{ORIGIN}/en/"',f'{ORIGIN}/en/"'))
write('404.html',shell('en','','Page not found','<div class="pagehead"><h1>Page not found</h1><a class="primary" href="/en/">Find a street →</a></div>',noindex=True))
write('records.json',json.dumps(DATA,ensure_ascii=False,separators=(',',':')))
write('i18n.json',json.dumps(T,ensure_ascii=False))
shutil.copy(R/'data/coverage-report.json',D/'coverage-report.json')
for file in ['style.css','app.mjs','search.mjs']:shutil.copy(R/'src'/file,D/file)
write('favicon.svg','<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="13" fill="#245b48"/><path d="M23 49V28h25M38 18l10 10-10 10" fill="none" stroke="#fff" stroke-width="5"/></svg>')
print(f'Built {len(DATA)} records, {len(groups)} localities, {len(T)} locales; {len(list(D.rglob("*.html")))} HTML pages')
