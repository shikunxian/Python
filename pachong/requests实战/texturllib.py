# encoding:utf-8
# 引入requests模块

import requests
if __name__ == '__main__':
    #step 1.指定URL
    url = 'https://www.sogo.com/'
    #step 2.发起请求
    #get方法会返回一个响应对象
    response = requests.get(url=url)
    #step 3.获取响应数据.  text返回的是字符串形式的响应数据
    page_text = response.text
    print(page_text)

    #step 4.持久化存储
    with open('sogou.html', 'w', encoding='utf-8') as file:
        file.write(page_text)
    print('爬取数据结束!!!')