import requests as rq
import os
from bs4 import BeautifulSoup as bs


class WebParser:
    def __init__(self,url: str):
        self.url = url

    def get_html(self):
        web_response = rq.get(url):
            if web_response.status_code == 200:
                soup = bs(web_response.text,'html.parser')
                HTML = soup.prettify()
