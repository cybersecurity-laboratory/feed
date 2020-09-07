#CSV Download Link : https://urlhaus.abuse.ch/downloads/csv/
#Detail : https://urlhaus.abuse.ch/api/

import pandas as pd
import re
import time
from datetime import datetime
import os
import urllib.request

starttime = datetime(2020,9,4,0,0,0)#utctime
endtime =  datetime(2020,9,6,23,59,59)#utctime
folder_path= r""#your local 'feed\emotet' folder
domain_file = ['composit_domain','latest_domain']#domain feed list
ip_file = ['composit_ip','latest_ip']#ip feed list

def get_hostname(x):
    url = x.url
    m = re.match(r'htt(p|ps)://([^/]+).*',url)
    text=re.sub(':[0-9]+$','',m.groups()[1])
    return text

def update_local_feed(filepath,df):
    if len(df) == 0: return 
    try:
        df_local_feed = pd.read_csv(filepath,header=None,names=['ioc'])
        df_new_feed = df_local_feed.append(df,ignore_index=True,sort=True).drop_duplicates('ioc')
        df_new_feed.to_csv(filepath,encoding='utf-8',index=False,header=False, columns = ['ioc'])
    except pd.io.common.EmptyDataError:
        df.to_csv(filepath,encoding='utf-8',index=False,header=False, columns = ['ioc'])


def get_urlhaus_data():
    url = 'https://urlhaus.abuse.ch/downloads/csv/'
    header =('id','dateadded','url','url_status','threat','tags','urlhaus_link','reporter')
    df = pd.read_csv(url,names=header,parse_dates=['dateadded'],engine = 'python',compression='zip',skiprows=9)
    return df

def extract(df,starttime,endtime):
    #seletect time
    df=df[df[ "dateadded"] > starttime]
    df=df[endtime > df[ "dateadded"]]
    #seletect emotet tag 
    df=df.query('tags.str.contains("emotet")', engine='python')
    #seletect not Cryptolaemus
    df=df[df.reporter != 'Cryptolaemus1']
    #url→hostname
    df['ioc'] =  df.apply(get_hostname, axis = 'columns' )
    #shaping
    df = df.drop_duplicates('ioc')
    #extract domain&ip
    df_domain = df.query('ioc.str.contains("[a-z]+$")', engine='python')
    df_ip = df.query('ioc.str.contains("[0-9]+$")', engine='python')

    return df_domain,df_ip
if __name__ == "__main__":
    df_urlhaus=get_urlhaus_data()
    df_domain,df_ip = extract(df_urlhaus,starttime,endtime)
    for file in domain_file:
        update_local_feed(folder_path+"\\"+file, df_domain)
    for file in ip_file:
        update_local_feed(folder_path+"\\"+file, df_ip)