# encoding:utf-8
import requests
import json
if __name__ == '__main__':
    #1.指定URl
    post_url = 'https://fanyi.baidu.com/sug'
    #2.进行UA伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'
    }
    #3.post请求处理(同get请求一致）
    word = input('enter a word:')
    data = {
        'kw':word
    }
    #请求发送
    response = requests.post(url=post_url, data=data ,headers=headers)
    #获取响应数据:json()返回的是obj（如果确认响应数据是json类型的，才可以使用json()）
    dic_obj = response.json()

    #长久化存储
    fp = open('./百度翻译.json','w',encoding='utf-8')
    json.dump(dic_obj, fp=fp, ensure_ascii=False)

    print('over!!')