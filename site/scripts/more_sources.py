from fetch_sources import country
from concurrent.futures import ThreadPoolExecutor
jobs={
'UA-more':[('lviv-region1','https://loda.gov.ua/documents/111759','html'),('lviv-mirror','https://www.loda.gov.ua/documents/111760','html')],
'KZ-more':[('almaty-amend','https://old.adilet.zan.kz/rus/docs/V19R0001523','html')],
'IN-more':[('kartavya-pib','https://www.pib.gov.in/PressReleasePage.aspx?PRID=1857900&lang=2&reg=48','html'),('delhi2017','https://ndmc.gov.in/council/Resolutions%202007/year%20wise/2017/Council%20Meeting%20No%2015-2016-2017-V-I.pdf','pdf')],
'VN-more':[('danang','https://thuvienphapluat.vn/van-ban/xay-dung-do-thi/nghi-quyet-66-2024-nq-hdnd-doi-ten-mot-so-duong-cong-trinh-cong-cong-da-nang-636192.aspx','html')]
}
with ThreadPoolExecutor(max_workers=6) as pool:
 for r in pool.map(lambda x:country(*x),jobs.items()):print(r,flush=True)
