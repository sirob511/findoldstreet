from fetch_sources import country
from concurrent.futures import ThreadPoolExecutor
items=[('saigon-study','https://viet-studies.com/kinhte/ChangingStreetNames_2013.pdf','pdf'),('saigon-current','https://vietnam.travel/places-to-go/southern-vietnam/ho-chi-minh-city/','html'),('saigon-dongkhoi','https://vnexpress.net/tp-hcm-xua-va-nay-qua-cac-dia-diem-lich-su-nam-1975-4881143.html','html')]
with ThreadPoolExecutor(max_workers=3) as p:
 for x in p.map(lambda item:country('VN-'+item[0],[item]),items):print(x,flush=True)
