"""Deterministic country imports and reviewed international mappings from captured sources.
Run fetch_sources.py / expand_sources.py to refresh; review differences before publishing.
"""
import pathlib,json,re,hashlib,concurrent.futures,datetime
from openpyxl import load_workbook
from unidecode import unidecode
D=pathlib.Path(__file__).resolve().parents[1]/'data'; S=D/'sources'
MAN={}
for f in sorted(S.glob('*manifest.json'),key=lambda p:('browser' in p.name,p.name)):
 for s in json.loads(f.read_text()): MAN[s['id']]=s
LANG={'UA':'uk','PL':'pl','ZA':'en','VN':'vi','KZ':'ru','IN':'en','UZ':'ru','EE':'et','LT':'lt','LV':'lv','DE':'de','MD':'ro','CZ':'cs'}
def source(key):
 m=MAN[key];return {k:m.get(k) for k in ['url','retrievedAt','reuseTerms','sha256']}|{'title':m.get('title',key),'id':key}
def record(c,city,old,new,key,locator,district=None,date=None,segment=None,status='verified',document=None):
 old=' '.join(old.split());new=' '.join(new.split());sid=hashlib.sha256(f'{c}|{city}|{district}|{old}|{segment}'.encode()).hexdigest()[:16]
 ev={'formerName':old,'currentName':new,'date':date,'datePrecision':'day' if date else 'unknown','status':'effective' if status=='verified' else 'review','segment':segment,'sourceUrl':MAN[key]['url'],'documentNumber':document,'locator':locator}
 return dict(id=sid,country=c,city=city,district=district,streetType=old.split()[0] if c in ['UA','PL'] else 'street',formerName=old,currentName=new,language=LANG[c],script='Cyrillic' if c in ['UA','KZ','UZ'] else 'Latin',aliases=[],transliterations=list(dict.fromkeys(unidecode(n) for n in [old,new] if unidecode(n)!=n)),events=[ev],sources=[source(key)],mapQuery=f'{new}, {city}',status=status,currentStatusNote='Latest name supported by the cited source; live register/geometry reconciliation is not complete.',houseNumbersVerified=False,segment=segment)
def ukraine():
 text=(S/'kyiv.txt').read_text(); rows=[];district=None;page=0;active=None
 for line in text.splitlines():
  if line.startswith('--- PAGE'):page=int(re.search(r'\d+',line)[0]);active=None;continue
  if 'район:' in line:district=line.strip().replace(':','');active=None;continue
  m=re.match(r'^\s*(\d+)\.\s+(.+?)\s{3,}(.+?)\s*$',line)
  if m:
   active={'old':m[2],'new':m[3],'page':page,'row':m[1],'district':district};rows.append(active)
  elif active and line.strip() and not line.strip().isdigit() and 'Стара назва' not in line:
   # continuation columns are consistently separated at column 54 in this official PDF
   if len(line)-len(line.lstrip())>=45:active['new']+=' '+line.strip()
   elif len(line)-len(line.lstrip())>=8:
    cells=re.split(r'\s{3,}',line.strip())
    if len(cells)==2:active['old']+=' '+cells[0];active['new']+=' '+cells[1]
    elif line.strip().startswith(('вулиц','№','Перелік')):active=None
    else:active['old']+=' '+line.strip()
 out=[]
 for r in rows:
  status='review' if ' та ' in r['old'] or 'частин' in r['old'].lower() else 'verified'
  out.append(record('UA','Київ',r['old'],r['new'],'kyiv',f"PDF page {r['page']}, row {r['row']}",r['district'],status=status))
 # reconcile exact later replacements within a district without collapsing duplicate names across districts
 by_old={(r['district'],r['formerName']):r for r in out}
 remove=set()
 for r in out:
  seen={r['id']}
  while (r['district'],r['currentName']) in by_old:
   nxt=by_old[(r['district'],r['currentName'])]
   if nxt['id'] in seen:break
   seen.add(nxt['id']);r['events']+=nxt['events'];r['currentName']=nxt['currentName'];r['transliterations']+=nxt['transliterations'];remove.add(nxt['id'])
 return [r for r in out if r['id'] not in remove]
def dt(x):return x.strftime('%Y-%m-%d') if isinstance(x,datetime.datetime) else None
def poland():
 out=[]
 for i,v in enumerate(load_workbook(S/'warsaw1.xlsx',data_only=True).active.values,1):
  if isinstance(v[0],int):
   r=record('PL','Warszawa',v[1],v[2],'warsaw1',f'zmiany row {i}',v[4],dt(v[9]),document=v[5]);r['aliases']=[v[3]];out.append(r)
 clean=lambda s:re.sub(r'[2345]+$','',s).strip()
 for i,v in enumerate(load_workbook(S/'warsaw2.xlsx',data_only=True).active.values,1):
  if not isinstance(v[0],int):continue
  old,temp=clean(v[1]),clean(v[3]);r=record('PL','Warszawa',old,temp,'warsaw2',f'orzeczenia row {i}',v[2],dt(v[6]),document=str(v[4]))
  date=dt(v[11]) or ('2019-01-01' if 'Chmiela' in old else None)
  r['events'].append(r['events'][0]|dict(formerName=temp,currentName=old,date=date,status='reversal',documentNumber=v[10] or v[7]))
  r['formerName']=temp;r['currentName']=old
  if v[13]:
   new=clean(v[13]);r['events'].append(r['events'][0]|dict(formerName=old,currentName=new,date='2019-08-03',status='effective',documentNumber=v[14]));r['formerName']=old;r['currentName']=new
  r['aliases']=list(dict.fromkeys([old,temp]));out.append(r)
 return out
def africa():
 text=(S/'durban.txt').read_text();block=text[text.index('\nAnton Lembede'):text.index('\nSylvester Ntuli')];out=[]
 for i,line in enumerate(block.splitlines(),1):
  cells=re.split(r'\s{2,}',line.strip())
  if len(cells)!=6:continue
  for j in range(0,6,2):
   new,old=cells[j:j+2];status='review' if new in ['lngrunce','Dullar Omar'] or '+' in old or '&' in old else 'verified'
   out.append(record('ZA','Durban',old,new,'durban',f'Printed page 5, table row {i}, pair {j//2+1}',status=status))
 out.append(record('ZA','Durban','Brickhill Road','Sylvester Ntuli','durban','Printed page 5, final row'))
 if MAN.get('pretoria',{}).get('status')=='downloaded':
  for old,new in [('Proes Street','Johannes Ramokgoase Street'),('Vermeulen Street','Madiba Street'),('Schoeman Street','Francis Baard Street'),('Skinner Street','Nana Sita Street'),('Andries Street','Thabo Sehume Street'),('Prinsloo Street','Sisulu Street'),('Van der Walt Street','Lilian Ngoyi Street')]:
   out.append(record('ZA','Pretoria',old,new,'pretoria','PDF page 1, labelled central street map',district='CBD'))
 if MAN.get('johannesburg',{}).get('status')=='downloaded':
  txt=(S/'johannesburg.txt').read_text();idx=txt.find('William Nicol Drive re-named')
  if idx>=0:out.append(record('ZA','Johannesburg','William Nicol Drive','Winnie Mandela Drive','johannesburg','Integrated annual report 2023/24, William Nicol Drive re-named entry'))
 return out
def india():
 pairs=[('Connaught Circus','Indira Chowk','1996-01-12'),('Connaught Place','Rajiv Chowk','1996-01-12'),('Canning Road','Madhav Rao Scindia Marg','2002-02-26'),('Aurangzeb Road','Dr. APJ Abdul Kalam Road','2015-08-28'),('Race Course Road','Lok Kalyan Marg','2016-09-21')]
 out=[]
 for i,(o,n,d) in enumerate(pairs,1):
  r=record('IN','New Delhi',o,n,'delhi',f'PDF page 3 (printed page 1), section 3.1.1 row {i}',date=None);r['events'][0]['decisionDate']=d;out.append(r)
 if MAN.get('kartavya',{}).get('status')=='downloaded':
  r=record('IN','New Delhi','Kingsway','Kartavya Path','kartavya','Kartavya Path project description');r['events']=[r['events'][0]|dict(formerName="King’s Way",currentName='Rajpath'),r['events'][0]|dict(formerName='Rajpath',currentName='Kartavya Path')];r['aliases']=['Kingsway',"King’s Way",'Rajpath'];out.append(r)
 if MAN.get('chennai',{}).get('status')=='downloaded':
  r=record('IN','Chennai','Mount Road','Anna Salai','chennai','City Action Plan, Mount Road (Anna Salai) entry');out.append(r)
 return out
def vietnam():
 key='hcmc-gov' if MAN.get('hcmc-gov',{}).get('status')=='downloaded' else 'hcmc'
 if MAN.get(key,{}).get('status')!='downloaded':return []
 r=record('VN','Hồ Chí Minh City','Xa lộ Hà Nội','Võ Nguyên Giáp',key,'Article: official renaming ceremony, 23 August 2023',district='Thủ Đức (at time of decision)',segment='From cầu Sài Gòn to ngã tư Thủ Đức. The remaining Xa lộ Hà Nội is not included.');r['events'][0]['ceremonyDate']='2023-08-23';return [r]
def kazakhstan():
 out=[record('KZ','Алматы','проспект Юрия Гагарина','проспект Ермека Серкебаева','almaty','Clause 1, first paragraph',district='Бостандыкский',segment='от улицы К. Тимирязева до проспекта Аль-Фараби',document='2/332; 117'),record('KZ','Алматы','улица Юбилейная','улица Владимира Толоконникова','almaty','Clause 1, second paragraph',district='Ауэзовский',document='2/332; 117')]
 for r in out:r['events'][0]['decisionDate']='2024-05-30'
 if MAN.get('astana',{}).get('status')=='downloaded':
  t=(S/'astana.txt').read_text()
  if 'Мұзафар Әлімбаев' in t:out.append(record('KZ','Астана','улица Гейдар Әлиев','улица Мұзафар Әлімбаев','astana','Clause 2, named-street rename',document='G24ABW51124'))
 return out
def finalize(rows):
 ukmap=dict(zip('абвгґдеєжзиіїйклмнопрстуфхцчшщьюя', ['a','b','v','h','g','d','e','ie','zh','z','y','i','i','i','k','l','m','n','o','p','r','s','t','u','f','kh','ts','ch','sh','shch','','iu','ia']))
 for r in rows:
  r['mapQuery']=f"{r['currentName']}, {r['city']}"
  r['currentStatusVerified']=False
  r['geometry']=None
  locations=[r.get('city',''),r.get('district') or '']
  r['locationAliases']=list(dict.fromkeys(r.get('locationAliases',[])+[unidecode(n) for n in locations if n]))
  if r['country']=='UA':r['locationAliases']+=[''.join(ukmap.get(ch,ch) for ch in n.lower()) for n in locations if n]
  r['transliterations']=list(dict.fromkeys(r['transliterations']+[unidecode(n) for ev in r['events'] for n in [ev['formerName'],ev['currentName']] if unidecode(n)!=n]))
  if r['country']=='UA':
   r['transliterations']+=[''.join(ukmap.get(ch,ch) for ch in n.lower()) for ev in r['events'] for n in [ev['formerName'],ev['currentName']]]
  if r['status']=='review' and not r.get('reviewReason'):r['reviewReason']='Combined objects, ambiguous spelling or segment identity requires manual review.'
 return rows
JOBS={'UA':ukraine,'PL':poland,'ZA':africa,'IN':india,'VN':vietnam,'KZ':kazakhstan}
def run(item):
 c,fn=item;from extend_imports import extend;from reviewed_imports import extend_reviewed;rows=extend(c,fn(),record,MAN,S,source);rows=extend_reviewed(c,rows,record,S,source);from postal_imports import extend_postal;rows=extend_postal(c,rows,record,S);rows=finalize(rows);(D/(c+'.json')).write_text(json.dumps(rows,ensure_ascii=False,indent=2));return c,len(rows)
if __name__=='__main__':
 with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
  for result in pool.map(run,JOBS.items()):print(result)
 from import_places import build_places
 print(('places',build_places()))

 from international_imports import build_international
 print(('international',build_international()))
