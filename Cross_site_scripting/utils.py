import requests
from bs4 import BeautifulSoup
import time

def check_succes(soup):
    if 'Congratulations, you solved the lab!' in soup.text:
        return 'Exploit successful'
    return f'{soup.text} Something went wrong'

def parse_html(response):
    return BeautifulSoup(response.content,'html.parser')

def get_csrf(session,url):
    response=session.get(url)
    soup=parse_html(response)
    token = soup.find('input', {'name': 'csrf'})["value"]
    return token


