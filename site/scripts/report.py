import pathlib,json,collections,datetime
R=pathlib.Path(__file__).resolve().parents[1];D=R/'data';rows=sum([json.loads((D/f'{c}.json').read_text()) for c in ['UA','PL','ZA','VN','KZ','IN']],[])
names={'UA':'Ukraine','PL':'Poland','ZA':'South Africa','VN':'Vietnam','KZ':'Kazakhstan','IN':'India'}
gaps={
'UA':['Current national directory and Kyiv street register not reconciled; Kharkiv coverage limited to the 48 street entries of order 513 В (26 July 2024), not the full city register','Coverage outside Kyiv and the captured Lviv-region appendix remains unimported: Odesa, Dnipro, Zaporizhzhia, Mykolaiv, Poltava, Vinnytsia, Chernihiv, Sumy, Zhytomyr, Rivne and other municipalities','Lviv appendix 2 recovered: 118 published mappings; 10 Lviv/Briukhovychi rows held for municipal-decision reconciliation'],
'PL':['TERYT/ULIC current-register comparison not completed; Łódź has 151 reviewed mappings, including historical chains and current-register checks for the 46 additions; not its full historical inventory','Wrocław, Poznań, Gdańsk, Szczecin, Katowice, Lublin, Białystok and other municipalities not imported'],
'ZA':['No municipal GIS geometry imported; Cape Town coverage is limited to eight unambiguous mappings; conflicting Lansdowne segments held for review; Pretoria includes the visitor map table with Church Street segments preserved','Ekurhuleni, Mangaung, Msunduzi, Buffalo City, Nelson Mandela Bay and other municipalities remain gaps','Durban combined streets and suspicious spellings held for review'],
'VN':['Ho Chi Minh City: officially confirmed partial rename plus independently corroborated historical entries; remaining historical leads held for review','Đà Nẵng resolution 66/2024 inspected: new roads and bridge names, not genuine street renames; excluded','Hanoi source leads mostly new naming, length changes or drafts; not published as renames','Huế, Hải Phòng, Cần Thơ and other municipalities not imported; historical Saigon table not reconciled'],
'KZ':['Almaty, Astana and Shymkent decisions imported; no GIS reconciliation','Karaganda, Pavlodar, Aktobe, Kostanay, Semey, Öskemen, Taraz, Atyrau and other municipalities not imported'],
'IN':['Delhi historical decisions imported, proposals excluded; Chennai pending text verification; Kolkata has one municipal-newsletter mapping, with the partial Moore Avenue lead held for review','Mumbai, Bengaluru, Hyderabad, Pune, Ahmedabad and other municipalities not imported','British Council historical table not imported; newer municipal registers not systematically compared']}
city=[];countries=[]
for c in names:
 rr=[r for r in rows if r['country']==c];verified=[r for r in rr if r['status']=='verified']
 countries.append(dict(country=c,name=names[c],verifiedStreets=len(verified),renameEvents=sum(len(r['events']) for r in verified),reviewRecords=len(rr)-len(verified),publishedLocalities=len(set(r['city'] for r in verified)),gaps=gaps[c]))
 for name in sorted(set(r['city'] for r in rr)):
  sub=[r for r in rr if r['city']==name];v=[r for r in sub if r['status']=='verified'];city.append(dict(country=c,municipality=name,verifiedStreets=len(v),renameEvents=sum(len(r['events']) for r in v),reviewRecords=len(sub)-len(v)))
sources={}
for r in rows+json.loads((D/'places.json').read_text()):
 for s in r['sources']:sources[s['url']]=s
attempts=[]
for p in sorted((D/'sources').glob('*manifest.json')):attempts+=json.loads(p.read_text())
places=json.loads((D/'places.json').read_text())
published=[r for r in rows+places if r['status']=='verified']
summary={'records':len(published),'streets':sum(not r.get('kind') for r in published),'cities':sum(r.get('kind')=='city' for r in published),'countryNames':sum(r.get('kind')=='country' for r in published),'countriesRepresented':len({r['country'] for r in published})}
report=dict(publishedSummary=summary,placeRenamings=places,placeCoverage={'cities':sum(r['kind']=='city' for r in places),'countries':sum(r['kind']=='country' for r in places),'scope':'Selected documented city and country mappings; street counts below exclude these records.'},asOf='2026-11-14',scope='Initial, incomplete source-backed release. Verified means the rename is supported by cited evidence, not current-live-register or geometry verification.',languages=list(json.loads((R/'src/i18n.json').read_text())),countries=countries,municipalities=city,importedSources=list(sources.values()),sourceAttempts=attempts,reviewRecords=[{'id':r['id'],'country':r['country'],'city':r['city'],'formerName':r['formerName'],'reason':r.get('reviewReason')} for r in rows if r['status']!='verified'],limitations=['No exhaustive national coverage claim.','Map links are name searches, not verified geometries or coordinates.','No house-number carryover claimed.','Current national registers and OSM object history not reconciled.','Historical district names are retained from source documents.','Interface translations generated in this run; native-speaker review pending.','OCR automation and general GIS reconciliation not implemented; unclear rows excluded.','Public deployment accessibility, custom-domain DNS and search-console ownership must be checked separately; repository SEO settings do not establish live indexing.'])
(D/'coverage-report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2));(R/'dist').mkdir(exist_ok=True);(R/'dist/coverage-report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
lines=['# FindOldStreet coverage report','', 'As of 14 November 2026. Initial, incomplete source-backed release. A verified row establishes a documented rename, not a verified present-day map identity.','',f"{summary['records']:,} published records across {summary['countriesRepresented']} countries: {summary['streets']:,} streets/segments, {summary['cities']} cities and {summary['countryNames']} country-name mappings.",'', 'The [source audit](data/source-audit.json) inventories all repository source manifests, including failures and uncited leads. It is not an exhaustive worldwide source census.','', '| Country | Published streets / segments | Rename events | Localities | Review |','|---|---:|---:|---:|---:|']
for c in countries:lines.append(f"| {c['name']} | {c['verifiedStreets']} | {c['renameEvents']} | {c['publishedLocalities']} | {c['reviewRecords']} |")
lines+=['','## City and country renamings','', 'Initial selection; the street counts above exclude these records.','']+[f"- {r['formerName']} → {r['currentName']} ({r['kind']}); [source]({r['sources'][0]['url']})." for r in places]
lines+=['','## Locality coverage','','| Country | Locality (source spelling) | Published | Events | Review |','|---|---|---:|---:|---:|']
for c in city:lines.append(f"| {names[c['country']]} | {c['municipality']} | {c['verifiedStreets']} | {c['renameEvents']} | {c['reviewRecords']} |")
lines+=['','## Sources imported','']
for s in sources.values():lines.append(f"- [{s['title']}]({s['url']}) — retrieved {s['retrievedAt']}; {s['reuseTerms']}")
lines+=['','## Gaps','']
for c in countries:
 lines.append('### '+c['name']);lines+=['- '+g for g in c['gaps']]
lines+=['','## Limits','']+['- '+x for x in report['limitations']]
lines+=['','## Languages','',', '.join(report['languages']), '', '## Sample searches','', 'Горького, Kyiv; Lecha Kaczyńskiego, Warsaw; Smith Street, Durban; Xa lo Ha Noi, Saigon; Юрия Гагарина, Алматы; Aurangzeb Road, Delhi.','', 'Machine-readable source failures and review records are in data/coverage-report.json.']
(R/'COVERAGE.md').write_text('\n'.join(lines)+'\n')
print(json.dumps(countries,ensure_ascii=False,indent=2))
