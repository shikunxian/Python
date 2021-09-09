#引入requests库
import requests
from lxml import etree
import re
import os


url = 'https://www.doutula.com/photo/list/?page=2'
ua = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'}
cookie = {'Cookie': '_agep=1630674333; _agfp=3630a66d762a14312c34678109c3b820; _agtk=0520ff749a28d87f9dfa28e48c5f1887; BAIDU_SSP_lcr=https://www.baidu.com/link?url=KFn3-Z_6X9Ixvq1RNg9o3VFCIVFJBVvEX4vwJZPkzBCQiGgq8wg0TLU1bo39ZrA9&wd=&eqid=a41663520011afe2000000066138ada5; Hm_lvt_2fc12699c699441729d4b335ce117f40=1630678772,1631019299,1631104436,1631104845; Hm_lpvt_2fc12699c699441729d4b335ce117f40=1631105210'}

html_url = requests.get(url=url,headers=ua).text

imge_urls = re.findall('data-original="(.*?)"',html_url)

for imge_url in imge_urls:
    imge = requests.get(imge_url, headers=ua).content
    imge_names = imge_url.split('/')[-1]#所以数据按照斜杠来分割,把斜杠分割之后然后变成一个列表，然后变成列表拿到列表里面的倒数第一个。


    with open('./doutula/%s'%imge_names, 'wb') as file:#‘%s’拼接
        file.write(imge)