"""Conservative, reproducible extraction of international name-pair snapshots.
Each candidate is retained in a review ledger; ambiguous pairs never become records.
"""
import collections,json,re,sys,unicodedata
from pathlib import Path
from bs4 import BeautifulSoup
S=Path(__file__).resolve().parents[1]/'data/sources'
def clean(s):return ' '.join(s.split())
def norm(s):
    s=unicodedata.normalize('NFKC',s).casefold().replace('ё','е')
    s=re.sub(r'\bулица\b','ул',s)
    return re.sub(r'[^\w]+',' ',s).strip()
def table(key,index=0):
    soup=BeautifulSoup((S/(key+'.html')).read_bytes(),'html.parser')
    return [[clean(c.get_text(' ',strip=True)) for c in tr.select('td,th')] for tr in soup.select('table')[index].select('tr')]
def screen(items):
    targets=collections.defaultdict(set)
    for r in items:targets[(r['city'],r.get('district'),norm(r['formerName']))].add(norm(r['currentName']))
    oldnames={(r['city'],norm(r['formerName'])) for r in items if norm(r['formerName'])!=norm(r['currentName'])}
    seen=set()
    for r in items:
        old,new=r['formerName'],r['currentName'];identity=(r['city'],r.get('district'),norm(old))
        why=r.pop('holdReason',None)
        if not old or not new:why='Missing name'
        elif norm(old)==norm(new):why='Unchanged name'
        elif len(targets[identity])>1:why='Conflicting destinations for the same old name and locality'
        elif identity in seen:why='Duplicate source identity'
        elif (r['city'],norm(new)) in oldnames:why='Intermediate-name or reused-name chain needs independent reconciliation'
        seen.add(identity)
        r['decision']='held' if why else 'approved'
        if why:r['reason']=why
    return items
def save(number,items,scope):
    screen(items)
    approved=[{k:v for k,v in r.items() if k not in ['decision','reason']} for r in items if r['decision']=='approved']
    for r in approved:r['coveragePass']=number
    (S/f'international-pass-{number}-additions.json').write_text(json.dumps(approved,ensure_ascii=False,indent=2)+'\n')
    review=dict(passNumber=number,target=500,scope=scope,candidates=len(items),approved=len(approved),held=len(items)-len(approved),decisions=items)
    (S/f'international-pass-{number}-review.json').write_text(json.dumps(review,ensure_ascii=False,indent=2)+'\n')
    print({k:v for k,v in review.items() if k!='decisions'})
def tashkent():
    out=[]
    for i,c in enumerate(table('tashkent-goldenpages')[1:],1):
        assert len(c)==6,(i,c)
        old,new,mahalla,district,date,notes=c
        r=dict(country='UZ',city='Ташкент',district=district or None,formerName=old,currentName=new,source='tashkent-goldenpages',locator=f'Street rename table, data row {i}',evidenceRow=i,sourceCells=c,locationAliases=['Tashkent','Toshkent','Uzbekistan','Oʻzbekiston'],language='ru',script='Cyrillic',nameNote='The cited commercial directory supplies this old/new pair. District spelling is retained from that source. It does not establish a verified present-day street geometry or legal effective date.')
        if any(x in (old+' '+new).lower() for x in ['(',')',',',';','част','типик','проед ',' / ']) or re.search(r'\d+-\d+',old+' '+new):r['holdReason']='Combined, partial, annotated or malformed street label requires review'
        if not re.search(r'ул\.|улиц|проезд|тупик|проспект|туп\.',new,re.I):r['holdReason']='Missing or malformed destination object type'
        out.append(r)
    save(6,out,'Tashkent, Uzbekistan: explicit directory street pairs, conflicts and unresolved chains excluded')
def polish_key(s):
    s=re.sub(r'^(ul\.|al\.|aleja|pl\.|plac|skwer|rondo)\s*','',s,flags=re.I)
    return norm(s)
def wroclaw_register():
    import io,zipfile
    from openpyxl import load_workbook
    with zipfile.ZipFile(S/'wroclaw-emuia-streets.zip') as z:
        values=list(load_workbook(io.BytesIO(z.read(z.namelist()[0])),read_only=True,data_only=True).active.values)[1:]
    reg=collections.defaultdict(dict)
    for row in values:
        for n in [' '.join(str(x) for x in row[2:5] if x),row[5] or '']:
            reg[polish_key(n)][row[0]]=row
    return reg
def wroclaw():
    reg=wroclaw_register();out=[]
    for i,c in enumerate(table('wroclaw-historical-pairs')[1:],1):
        assert len(c)==2
        old,new=c;old=re.sub(r' in Breslau$','',old)
        kind=new.split()[0];candidates=[v for v in reg.get(polish_key(new),{}).values() if v[1]==kind]
        r=dict(country='PL',city='Wrocław',streetType=kind,formerName=old,currentName=new,source='wroclaw-historical-pairs',locator=f'German/Polish street table, data row {i}',evidenceRow=i,sourceCells=c,locationAliases=['Wroclaw','Breslau'],language='de',script='Latin',extraSources=['wroclaw-emuia-streets'],nameNote='Historical pair from WroclawGuide; the Polish name and object type also match the captured municipal EMUiA street register. This checks name existence, not historical boundary continuity or house numbers. No rename date is inferred.')
        if len(candidates)!=1:r['holdReason']='No unique exact current-name and object-type match in municipal EMUiA register'
        else:r['municipalRegisterId']=candidates[0][0]
        if any(x in old+' '+new for x in [',',';','(',')',' / ']) or 'Does not exist' in new:r['holdReason']='Vanished street, combined destinations or annotated name'
        out.append(r)
    save(7,out,'Wrocław, Poland: historical German names with exact current municipal name/type matches')
def vilnius_register():
    reg=collections.defaultdict(dict)
    for p in sorted(S.glob('vilnius-road-names-*.json')):
        for f in json.loads(p.read_text())['features']:
            a=f['attributes']
            if not a['vardas'] or not a['gat_kodas']:continue
            key=norm(re.sub(r' g\.$','',a['vardas']))
            reg[key][a['gat_kodas']]=(a,p.stem)
    return reg

def vilnius():
    reg=vilnius_register();out=[]
    soup=BeautifulSoup((S/'vilnius-historical-table.html').read_bytes(),'html.parser')
    for i,tr in enumerate(soup.select('#fundsTable tr')):
        c=[clean(x.get_text(' ',strip=True)) for x in tr.find_all('td',recursive=False)]
        if len(c)!=4 or i==0:continue
        new,before,location,history=c
        district='N. Vilnios' if location.startswith('N. Vilnios.') else location.split('. ')[0]
        candidates=list(reg.get(norm(new),{}).values())
        names=[('pre-1987',before)]+[('historical',x.strip()) for x in history.split(',')]
        for field,old in names:
            if not old:continue
            r=dict(country='LT',city='Vilnius',district=district,formerName=old,currentName=new,source='vilnius-historical-table',locator=f'Historical street table fundsTable, row {i}; {field} field',evidenceRow=i,evidenceField=field,sourceCells=c,locationAliases=['Vilnius','Wilno','Вильнюс'],language='lt',script='Cyrillic' if re.search('[А-Яа-я]',old) else 'Latin',nameNote='Historical label from the cited Vilnius street-history table, cross-checked for current name existence in the Hnit-Baltic road-name inventory. The source includes names in several languages; no legal rename date, complete event chain, historical boundary continuity or house-number continuity is inferred.')
            if len(candidates)!=1:r['holdReason']='No unique exact current-name match in captured road-name inventory'
            else:
                a,key=candidates[0];r['extraSources']=[key];r['addressRegisterStreetCode']=a['gat_kodas']
            if any(x in old+' '+new for x in ['(',')',';',' - ',' – ','/','?']) or re.search(r'\bdalis\b|\bчаст',old,re.I):r['holdReason']='Partial, combined or annotated historical label'
            if not district or len(district)>45:r['holdReason']='Unclear locality scope'
            out.append(r)
    save(8,out,'Vilnius, Lithuania: pre-1987 and historical names checked against captured current road-name inventory')
if __name__=='__main__':
    {'6':tashkent,'7':wroclaw,'8':vilnius}[sys.argv[1]]()
