# // find_idz Fbeh ...
# 
# // khusus link-profile lite or m.fbeh

import requests
from bs4 import BeautifulSoup
import re

class Finder:
    def __init__(
            self,
            link_profile : str, 
        ):
        self.link_profile = link_profile

        headers = {
            'hostname':'facebook.com',
            'port' : '443',
            'path': self.link_profile,
            'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36',
            'Accept-Language': 'en-GB,en-US;q=0.8,en;q=0.6',
            'accept': 'text/html,application/json,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            }
        resp = requests.Session().get(
                self.link_profile,
                headers = headers,
            )
        self.parser = BeautifulSoup(resp.content,features="html.parser")
        self.par = self.parser.find_all('a')[2:3]
        self.content = self.parser.find_all('a')

    def __repr__(self):
        for parser in self.par:
            return parser['href'].split('=')[4].replace('&refid','')

if __name__ == "__main__":
    pass
