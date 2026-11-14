from fetch_sources import country
from concurrent.futures import ThreadPoolExecutor
jobs={
'UA-extra':[('lviv-region','https://loda.gov.ua/documents/111760','html')],
'PL-extra':[('krakow','https://www.krakow.pl/aktualnosci/212775,29,komunikat,dekomunizacja_nazw_ulic_w_krakowie.html','html')],
'KZ-extra':[('astana','https://old.adilet.zan.kz/rus/docs/G24ABW51124','html'),('almaty2019alt','https://law.gov.kz/api/documents/127684/rus/download/pdf','pdf')],
'ZA-extra':[('pretoria','https://www.treasury.gov.za/nt/PTA%20Central%20New%20Street%20Names.pdf','pdf'),('johannesburg','https://joburg.org.za/documents_/Documents/City-of-Johannesburg-Integrated-Annual-Report_2023.24.pdf','pdf')],
'IN-extra':[('kartavya','https://centralvista.gov.in/central-vista-avenue.php/1000','html'),('chennai','https://chennaicorporation.gov.in/gcc/images/Chennai%20U%20A%20%20City%20Action%20plan.pdf','pdf')],
'VN-extra':[('hcmc-gov','https://tphcm.chinhphu.vn/xa-lo-ha-noi-chinh-thuc-khoac-ten-moi-101230823115413686.htm','html')]
}
with ThreadPoolExecutor(max_workers=6) as pool:
 for r in pool.map(lambda x:country(*x),jobs.items()): print(r,flush=True)
