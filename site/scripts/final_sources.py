from fetch_sources import country
from concurrent.futures import ThreadPoolExecutor
jobs={
'VN-final':[('dalat-history','https://lamdongdost.gov.vn/bitstream/handle/123456789/354316/KHCN%2003%20%28in%29.pdf?isAllowed=y&sequence=1','pdf')],
'IN-final':[('chennai-sbi','https://home.sbi.bank.in/documents/13958/14399/SBI%2BS%2BLIVING%2BHERITAGE%2BABHIK%2BRAY%2B2.pdf/SBI%20S%20LIVING%20HERITAGE%20ABHIK%20RAY%2023782.pdf?t=1765274394633','pdf')]
}
with ThreadPoolExecutor(max_workers=6) as p:
 for x in p.map(lambda x:country(*x),jobs.items()):print(x,flush=True)
