
# In[3]:

#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import emoji
import unidecode
import requests
import unidecode
import os
from requests.exceptions import ProxyError
import requests.exceptions as exs
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import argparse
import emoji

# In[5]:

def remove_emoji(string):
    return emoji.get_emoji_regexp().sub(u'', string)

# In[8]:
def cleaning():
    data = pd.read_csv(args.file_path)
    data = data.drop_duplicates()
    data = data.reset_index()
    data['fullname_with_points'] = [str(data['fullName'][i]).replace(" ",".") for i in range(0,len(data))]
    data['fullname_with_points2'] = [remove_emoji(data['fullname_with_points'][i]) for i in range(0,len(data))]

    data['fullname_with_points3'] = [unidecode.unidecode(data['fullname_with_points2'][i]) for i in range(0,len(data))]

    data['fullname_with_points4'] = [data['fullname_with_points3'][i].lower() for i in range(0,len(data))]

    data_clean = [data['fullname_with_points4'][i].count('.')==1 for i in range(0,len(data))]

    data_c = data[data_clean]

    data_cl = [data_c['fullname_with_points4'][i].split(".") for i in data_c.index]
    data_cl1 = [data_cl[i][::-1] for i in range(0,len(data_cl))]
    data_cl1 = [data_cl[i][::-1] for i in range(0, len(data_cl))]

    data_c['fullnames_reversed'] = ['.'.join(data_cl1[i]) for i in range(0,len(data_cl1))]
    data_c = data_c.reset_index()

    data_c['fullnames_reversed_stickform'] = [data_c['fullnames_reversed'][i].replace('.','') for i in range(0, len(data_c))]
    data_c['fullname_with_points4_stickform'] = [data_c['fullname_with_points4'][i].replace('.','') for i in range(0, len(data_c))]

    # Generate adresses :

    data_c['gmail.com_reversed']=data_c['fullnames_reversed']+"@gmail.com"
    data_c['hotmail.fr_reversed']=data_c['fullnames_reversed']+"@hotmail.fr"
    data_c['orange.fr_reversed']=data_c['fullnames_reversed']+"@orange.fr"
    data_c['sfr.fr_reversed']=data_c['fullnames_reversed']+"@sfr.fr"
    data_c['free.fr_reversed']=data_c['fullnames_reversed']+"@free.fr"
    data_c['outlook.fr_reversed']=data_c['fullnames_reversed']+"@outlook.fr"
    data_c['icloud.fr_reversed']=data_c['fullnames_reversed']+"@icloud.fr"
    data_c['icloud.com_reversed']=data_c['fullnames_reversed']+"@icloud.com"


    data_c['gmail.com']=data_c['fullname_with_points4']+"@gmail.com"
    data_c['hotmail.fr']=data_c['fullname_with_points4']+"@hotmail.fr"
    data_c['orange.fr']=data_c['fullname_with_points4']+"@orange.fr"
    data_c['sfr.fr']=data_c['fullname_with_points4']+"@sfr.fr"
    data_c['free.fr']=data_c['fullname_with_points4']+"@free.fr"
    data_c['outlook.fr']=data_c['fullname_with_points4']+"@outlook.fr"
    data_c['icloud.fr']=data_c['fullname_with_points4']+"@icloud.fr"
    data_c['icloud.com']=data_c['fullname_with_points4']+"@icloud.com"

    # Stickform

    data_c['fullnames_reversed_stickform'] = [data_c['fullnames_reversed_stickform'][i].replace('.','') for i in range(0, len(data_c))]
    data_c['fullname_with_points4_stickform'] = [data_c['fullname_with_points4_stickform'][i].replace('.','') for i in range(0, len(data_c))]
    data_c['gmail.com_reversed_stickform']=data_c['fullnames_reversed_stickform']+"@gmail.com"
    data_c['hotmail.fr_reversed_stickform']=data_c['fullnames_reversed_stickform']+"@hotmail.fr"
    data_c['orange.fr_reversed_stickform']=data_c['fullnames_reversed_stickform']+"@orange.fr"
    data_c['sfr.fr_reversed_stickform']=data_c['fullnames_reversed_stickform']+"@sfr.fr"
    data_c['free.fr_reversed_stickform']=data_c['fullnames_reversed_stickform']+"@free.fr"
    data_c['outlook.fr_reversed_stickform']=data_c['fullnames_reversed_stickform']+"@outlook.fr"
    data_c['icloud.fr_reversed_stickform']=data_c['fullnames_reversed_stickform']+"@icloud.fr"
    data_c['icloud.com_reversed_stickform']=data_c['fullnames_reversed_stickform']+"@icloud.com"

    data_c['gmail.com_stickform']=data_c['fullname_with_points4_stickform']+"@gmail.com"
    data_c['hotmail.fr_stickform']=data_c['fullname_with_points4_stickform']+"@hotmail.fr"
    data_c['orange.fr_stickform']=data_c['fullname_with_points4_stickform']+"@orange.fr"
    data_c['sfr.fr_stickform']=data_c['fullname_with_points4_stickform']+"@sfr.fr"
    data_c['free.fr_stickform']=data_c['fullname_with_points4_stickform']+"@free.fr"
    data_c['outlook.fr_stickform']=data_c['fullname_with_points4_stickform']+"@outlook.fr"
    data_c['icloud.fr_stickform']=data_c['fullname_with_points4_stickform']+"@icloud.fr"
    data_c['icloud.com_stickform']=data_c['fullname_with_points4_stickform']+"@icloud.com"
    return data_c.to_csv(args.file_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='A test program.')
    parser.add_argument("-fp", "--file_path", help="Prints the supplied argument.")
    #parser.add_argument("-o", "--output_name", help="Prints the supplied argument.")
    args = parser.parse_args()
    cleaning()
