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
    oldnames={norm(r['formerName']) for r in items}
    seen=set()
    for r in items:
        old,new=r['formerName'],r['currentName'];identity=(r['city'],r.get('district'),norm(old))
        why=r.pop('holdReason',None)
        if not old or not new:why='Missing name'
        elif norm(old)==norm(new):why='Unchanged name'
        elif len(targets[identity])>1:why='Conflicting destinations for the same old name and locality'
        elif identity in seen:why='Duplicate source identity'
        elif norm(new) in oldnames:why='Intermediate-name or reused-name chain needs independent reconciliation'
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
if __name__=='__main__':
    if sys.argv[1]=='6':tashkent()
