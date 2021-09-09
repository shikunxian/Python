# encoding:utf-8

import requests
import json

if __name__ == '__main__':
    url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'
    }
    kw = input('查询:')
    param ={
          'cname':'',
            'pid':'',
        'keyword': kw,
      'pageIndex': '1',
       'pageSize': '10'
    }
    resposes = requests.get(url=url, params=param, headers=headers)
    dic_data = resposes.text

    with open('./肯德基.json', 'w', encoding='utf-8') as file:
        file.write(dic_data)