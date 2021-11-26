


# -*- coding: utf-8 -*-
import pandas as pd
import requests
import os
from requests.exceptions import ProxyError, SSLError, Timeout
import requests.exceptions as exs
import urllib3
import argparse
import random
from fake_useragent import UserAgent
from json.decoder import JSONDecodeError
import csv


import requests


ssnOne = requests.Session()
ssnOne.get(url)
ssnOne.cookies.get_dict()

ssnOne.get(url, proxies=proxies, headers={'User-Agent': random.choice(USER_AGENTS)}, verify=False)

x = ssnOne.post(url, proxies=proxies, headers={'User-Agent': random.choice(USER_AGENTS)}, data = myobj, verify=False)

url = 'https://www.mapetitemercerie.com/'
myobj = {'controller':'authentication',
                     'SubmitCreate':'1',
                     'ajax':'true',
                     'email_create': 'dyeg@gmail.com',
                     'back' : 'my-account',
                     'token':'1ec4149f47531dd4fdbe68f485670d7c'
                    }

USER_AGENTS = (
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:11.0) Gecko/20100101 Firefox/11.0',
        'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100 101 Firefox/22.0',
        'Mozilla/5.0 (Windows NT 6.1; rv:11.0) Gecko/20100101 Firefox/11.0',
        ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_4) AppleWebKit/536.5 (KHTML, like Gecko) '
         'Chrome/19.0.1084.46 Safari/536.5'),
        ('Mozilla/5.0 (Windows; Windows NT 6.1) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.46'
         'Safari/536.5')
    )

proxies = {
    "http": "http://roulod78.hotmail.fr:8jv4ts@gate2.proxyfuel.com:2000",
    "https": "http://roulod78.hotmail.fr:8jv4ts@gate2.proxyfuel.com:2000",
}


:: fullheaders à verifier, pourl les sites capricieux



headers={'User-Agent': random.choice(USER_AGENTS),'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'Accept-encoding':'gzip, deflate, br', 'Accept-language':'en-US, en;q=0.9', 'Host':'','Referer':'https://www.mondialtissus.fr/', 'SEC-FETCH-DEST':'document', 'SEC-FETCH-MODE':'navigate', 'SEC-FETCH-SITE':
'cross-site', 'SEC-FETCH-USER': '?1', 'SEC-GPC'=1, 'UPGRADE-INSECURE-REQUESTS':'1' })
    
    