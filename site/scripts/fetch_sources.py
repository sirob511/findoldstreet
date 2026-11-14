import concurrent.futures,json,pathlib,hashlib,datetime,requests
from pypdf import PdfReader
from bs4 import BeautifulSoup
from openpyxl import load_workbook
ROOT=pathlib.Path(__file__).resolve().parents[1]; D=ROOT/'data'/'sources'; D.mkdir(parents=True,exist_ok=True)
SOURCES={
'UA':[('kyiv','https://minio.kyivcity.gov.ua/kyivcity/sites/21/uploaded-files/Perelik%20pereimenovanykh%20u%202014-2025%20rokakh%20vulyts%20mista%20Kyieva.pdf','pdf')],
'PL':[('warsaw2','https://warszawa19115.pl/documents/20184/17793521/Wykaz%20nr%202%20Dekomunizacja%20%2818%2C4%20kB%29.xlsx','xlsx'),('warsaw1','https://warszawa19115.pl/documents/20184/17793521/Wykaz%20nr%201%20-%20Rada%20Miasta%206%20ulic%20%289%2C7%20kB%29.xlsx','xlsx')],
'ZA':[('durban','https://visitdurban.travel/storage/Destination%20Durban%20Visitor%20Guide%202025%20web.pdf','pdf')],
'IN':[('delhi','https://ndmc.gov.in/council/Resolutions%202007/year%20wise/2017/ITEM%20No%2001%20%28T-04%29-2017.pdf','pdf')],
'VN':[('hcmc','https://ttbc-hcm.gov.vn/tphcm-doi-ten-xa-lo-ha-noi-thanh-duong-vo-nguyen-giap-1003536.html','html')],
'KZ':[('almaty','https://old.adilet.zan.kz/rus/docs/V24R0002332','html'),('almaty2019','https://zan.gov.kz/api/documents/127684/rus/download/pdf','pdf')]
}
def country(c,items):
 out=[]
 for key,url,ext in items:
  meta={'id':key,'country':c,'url':url,'retrievedAt':datetime.datetime.now(datetime.timezone.utc).isoformat(),'reuseTerms':'No explicit reuse licence established; factual name mappings only; source documents retained for audit, not served publicly.'}
  try:
   r=requests.get(url,timeout=45);r.raise_for_status();p=D/(key+'.'+ext);p.write_bytes(r.content);meta['sha256']=hashlib.sha256(r.content).hexdigest()
   if ext=='pdf': t='\n'.join(f'\n--- PAGE {i+1} ---\n'+page.extract_text(extraction_mode='layout') for i,page in enumerate(PdfReader(p).pages))
   elif ext=='xlsx':
    w=load_workbook(p,data_only=True);t='\n'.join(f'{s.title} ROW {i}: '+json.dumps(list(row),ensure_ascii=False,default=str) for s in w for i,row in enumerate(s.values,1))
   else: t=BeautifulSoup(r.content,'html.parser').get_text(' ',strip=True)
   (D/(key+'.txt')).write_text(t);meta['status']='downloaded';meta['textFile']=key+'.txt'
  except Exception as e:meta.update(status='failed',error=str(e))
  out.append(meta)
 (D/(c+'-manifest.json')).write_text(json.dumps(out,ensure_ascii=False,indent=2));return c,[(x['id'],x['status']) for x in out]
if __name__=='__main__':
 with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
  for r in pool.map(lambda x:country(*x),SOURCES.items()): print(r,flush=True)
