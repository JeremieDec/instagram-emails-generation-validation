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
import time

from datetime import datetime

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

USER_AGENTS = (
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:11.0) Gecko/20100101 Firefox/11.0',
        'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100 101 Firefox/22.0',
        'Mozilla/5.0 (Windows NT 6.1; rv:11.0) Gecko/20100101 Firefox/11.0',
        ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_4) AppleWebKit/536.5 (KHTML, like Gecko) '
         'Chrome/19.0.1084.46 Safari/536.5'),
        ('Mozilla/5.0 (Windows; Windows NT 6.1) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.46'
         'Safari/536.5')
    )

already_processed_path = list()
already_processed = list()
already_indexes = list()
current_cwd = os.getcwd()

def already():
    global current_cwd, already_indexes, already_processed
    already_processed_path = current_cwd +'//'+'processed'+'//'+'processed_df.csv'
    print('la %s' %already_processed_path)
    already_processed = pd.read_csv(already_processed_path, error_bad_lines=False, warn_bad_lines=False)
    already_processed = already_processed.set_index(['username'])
    already_indexes = [str(already_processed.index[i]) for i in range(0,len(already_processed))]

requests_speed_historic = pd.DataFrame()

ua = UserAgent()
y = list()
requests_speed = list()
current_time = list()
x = list()
payload = list()
processed_data = pd.DataFrame()
unique_id = round(random.uniform(1.0, 1.9),4)

df1 = pd.DataFrame(columns=['num', 'is_verified'])
domains = ['gmail.com', 'gmail.com_reversed','gmail.com_stickform', 'gmail.com_reversed_stickform']

url = 'website form to query'

proxies = {
    "http": # rotating proxy advised (slow mode)
    "https": # rotating proxy advised (slow mode)
}

#
def scrapp():
    global datas
    global df1
    global y
    global processed_data
    global subset_datas
    global payload
    global requests_speed_historic
    current_cwd = os.getcwd()
    f= args.file_path_fichier
    datas = pd.read_csv(f)
    datas = datas.sample(frac=1)
    datas = datas.set_index(['username']) # inutile 
  
    for num in range(0, 70): #len(datas)
        requests_to_do = (len(domains)*len(datas))-(num*len(domains))
        print('remaining requests : %d' %(requests_to_do))
# if datas.index[num] in already_indexes:
            #print('existe deja')
        #    continue

        for domain in domains:
            myobj = {'controller':'authentication',
                     'SubmitCreate':'1',
                     'ajax':'true',
                     'email_create': datas.iloc[num][domain],
                     'back' : 'my-account',
                     'token':'1ec4149f47531dd4fdbe68f485670d7c'
                    }

            headers = {'User-Agent': UserAgent().random}
            print('currently testing %s' %datas.iloc[num][domain])

            try:
                x = requests.post(url, proxies=proxies, headers={'User-Agent': random.choice(USER_AGENTS)}, data = myobj, verify=False)
                y.append(x)
                print('request num %d' %(len(y)))
                if x.status_code !=200:
                    print('statuscode: 200, redemarre le try')
                    pass
            except (ProxyError, SSLError, Timeout, UnboundLocalError, JSONDecodeError):
                print('erreur excpt post')
                print('total queries deja effectuees : %d' %(len(y)))
                pass

            try:
                if x.json()['hasError']:
                    if 'Un compte est déjà enregistré avec cet e-mail' in str(x.json()['errors']):
                        print('bon')
                        print(num)
                        print(datas.iloc[num][domain])
                        valuestoappend = [num, datas.iloc[num][domain]]
                        df1 = df1.append(pd.Series(valuestoappend, index = ['num', 'is_verified']), ignore_index = True)
# if len(df1) % 1 == 0:
                        filename = current_cwd+'//'+'result'+'\\'+str(random.uniform(1.5, 1.9))+'_'+str(num)+'.csv'
                        df1.to_csv(filename, index=False)
                        df1 = pd.DataFrame(columns=['num', 'is_verified'])
            except Exception as e:
                print(e)

            if len(y) != 0:
                if len(y) % 5 == 0:
                    print('20 requests effectuees!')
                    now = datetime.now()
                    current_time.append(now)
                    print("Current Time =", current_time[-1])
                    print('nb de resultats : %d' %(len(df1)/3))
                    if len(current_time)>1:
                        requests_speed.append(current_time[-1] - current_time[-2])
                        requests_speed_historic = requests_speed_historic.append(requests_speed)
                        print("20 requests_speed is %s"  %str(requests_speed[-1]))
                        print('rq speed histo :')
                        print(requests_speed_historic)
                        filename_requests_speed_historic = current_cwd+'\\'+'process_speed'+'\\'+'speed.csv'
                        requests_speed_historic.to_csv(filename_requests_speed_historic, index=False)
                        requests_speed_historic = pd.DataFrame()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='A test program.')
    parser.add_argument("-in", "--file_path_fichier", help="Root cwd")
    args = parser.parse_args()
    scrapp()