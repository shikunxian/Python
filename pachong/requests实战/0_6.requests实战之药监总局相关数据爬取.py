# encoding:utf-8

import requests

if __name__ == '__main__':
    url = 'http://scxk.nmpa.gov.cn:81/xk/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'
    }
    page_text = requests.get(url=url, headers=headers).text

    with open('./化妆品.html', 'w', encoding='utf-8') as file:
        file.write(page_text)