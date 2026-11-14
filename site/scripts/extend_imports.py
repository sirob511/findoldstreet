"""Additional audited adapters; invoked by import_data.py for each country."""
import re,json,hashlib,pathlib
from bs4 import BeautifulSoup

def extend(c,out,record,MAN,S,source):
 if c=='UA':
  p=S/'lviv-browser.txt';text=p.read_text()
  if 'L107:' in text:
   MAN['lviv-browser']={'url':'https://loda.gov.ua/documents/111759','retrievedAt':'2026-11-14T05:39:00+00:00','reuseTerms':'CC BY 4.0, as stated in the official page footer. Attribution: Lviv Regional Military Administration.','sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'status':'downloaded','id':'lviv-browser'}
   for line in text.splitlines():
    m=re.match(r'L\d+: (\d+)\..*?\|\s*(.*?)\s*\|\s*(.*?)\s*\|\s*(.*?)\s*$',line)
    if not m:continue
    n,place,old,new=m.groups();place=' '.join(place.split());split=re.split(r'\s+(?=[А-ЯІЇЄ][а-яіїє’]+(?:ського|цького) район)',place,maxsplit=1)
    city=re.sub(r'^(село|місто|селище|м\.)\s+','',split[0]);district=split[1] if len(split)>1 else None
    r=record(c,city,old,new,'lviv-browser',f'Appendix 1, table row {n}',district,document='700/0/5-24ВА');r['events'][0]['decisionDate']='2024-07-26';out.append(r)
 if c=='ZA' and MAN.get('johannesburg',{}).get('status')=='downloaded':
  if 'William Nicol Drive re-' in (S/'johannesburg.txt').read_text():
   r=record(c,'Johannesburg','William Nicol Drive','Winnie Mandela Drive','johannesburg','Integrated Annual Report 2023/24, event table: William Nicol Drive re-named');r['events'][0]['ceremonyDate']='2023-09-26';out.append(r)
 if c=='IN':
  if MAN.get('kartavya-pib',{}).get('status')=='downloaded':
   r=record(c,'New Delhi','Rajpath','Kartavya Path','kartavya-pib','PIB release 1857900, opening paragraph');r['events'][0]['ceremonyDate']='2022-09-08';r['aliases']=['Kingsway'];out.append(r)
  if MAN.get('delhi2017',{}).get('status')=='downloaded':
   txt=(S/'delhi2017.txt').read_text();
   if 'Dalhousie Road' in txt and 'Dara Shukoh Road' in txt:
    r=record(c,'New Delhi','Dalhousie Road','Dara Shukoh Road','delhi2017','Printed page 43, section 3.1.1, row (vi)');r['events'][0]['decisionDate']='2017-02-06';r['aliases']=['Dara Shikoh Road'];out.append(r)
 if c=='KZ' and MAN.get('almaty2018',{}).get('status')=='downloaded':
  soup=BeautifulSoup((S/'almaty2018.html').read_text(),'html.parser');district=None;n=0
  for el in soup.select('p'):
   text=el.get_text(' ',strip=True)
   if text.startswith('по '):district=text.rstrip(':')
   m=re.fullmatch(r'улицу (.+?) [–-] в (улицу|проспект) (.+?)[;.]?',text)
   if not m:continue
   n+=1;old='улица '+m[1];new=('улица' if m[2]=='улицу' else 'проспект')+' '+m[3].rstrip(';.')
   r=record(c,'Алматы',old,new,'almaty2018',f'Clause 1, rename paragraph {n}',district,document='4/605; 300 (amended 31 January 2019)');r['events'][0]['decisionDate']='2018-12-29';out.append(r)
 if c=='PL' and MAN.get('krakow-law',{}).get('status')=='downloaded':
  pairs=[('Emila Dziedzica','Marka Eminowicza'),('Franciszka Kajty','prof. Henryka Wereszyckiego'),('Zygmunta Młynarskiego','Marka Nawary'),('Lucjana Szenwalda','Majora Pilota Stefana Janusa'),('Janka Szumca','Wiktora Zina'),('Jana Szwai','prof. Władysława Konopczyńskiego')]
  for i,(old,new) in enumerate(pairs,1):
   r=record(c,'Kraków','ul. '+old,'ul. '+new,'krakow-law',f'PDF page 1, §1 item {i}',date='2017-09-21',document='LXXXI/1957/17');out.append(r)
 if c=='IN':
  for r in out:
   if r['city']=='Chennai':
    r['status']='review';r['reviewReason']='Source search indexed Mount Road (Anna Salai), but downloaded PDF extraction did not retain the exact paired entry; awaiting visual review.'
    if MAN.get('chennai-sbi',{}).get('status')=='downloaded':
     txt=(S/'chennai-sbi.txt').read_text()
     if 'Mount Road (Anna Salai)' in txt:
      r['status']='verified';r.pop('reviewReason',None);r['sources'].append(source('chennai-sbi'));r['events'][0]['sourceUrl']=MAN['chennai-sbi']['url'];r['events'][0]['locator']='Mount Road Madras section, opening sentence'
 if c=='VN' and MAN.get('dalat-history',{}).get('status')=='downloaded':
  # Split geometry is unresolved: retain historical lead for review, never publish whole-street equivalence.
  r=record(c,'Đà Lạt','Trương Vĩnh Ký','Nam Kỳ Khởi Nghĩa','dalat-history','Article on historic Đà Lạt streets, 1976 rename and 2002 split',date='1976',segment='The source reports a 2002 split into Nam Kỳ Khởi Nghĩa and Phan Như Thạch; exact segment boundaries unresolved.',status='review');r['events'][0]['datePrecision']='year';r['reviewReason']='2002 split requires segment identity and current-name confirmation.';out.append(r)
 if c=='VN' and MAN.get('saigon-dongkhoi',{}).get('status')=='downloaded':
  facts=json.loads((S/'saigon-transcription.json').read_text())
  current=(S/'saigon-current.txt').read_text() if (S/'saigon-current.txt').exists() else ''
  for pair in facts['pairs']:
   confirmed=pair['current'] in current
   r=record(c,'Hồ Chí Minh City',pair['former'],pair['current'],'saigon-dongkhoi',pair['locator'],district=pair.get('district'),status='verified' if confirmed else 'review')
   if confirmed:r['sources'].append(source('saigon-current'))
   else:r['reviewReason']='Historical mapping found; independent current-name confirmation not completed.'
   out.append(r)
 return out
