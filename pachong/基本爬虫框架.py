# encoding:utf-8

import requests
import re

if __name__ == '__main__':
    url = 'https://pic.netbian.com/4kfengjing/'
    ua = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'}
#    cookie = {'cookie': '__yjs_duid=1_ff717f58c6c8033a78fe30a971ef70481630849007919; zkhanecookieclassrecord=%2C53%2C54%2C55%2C; PHPSESSID=pl4cd7hpcc3s1rtlkvpientv43; Hm_lvt_526caf4e20c21f06a4e9209712d6a20e=1630849012,1630850909,1630850921,1630851086; zkhanmlusername=%BA%CD%BC%D1%BC%D1%D3%D0%C1%CB%CE%B4%C0%B4; zkhanmluserid=5383795; zkhanmlgroupid=1; zkhanmlrnd=768vTOvGZOyG37l390JQ; zkhanmlauth=2ee097969d3caa2a7572efebdbfdd2aa; Hm_lpvt_526caf4e20c21f06a4e9209712d6a20e=1630851117'}
    img_text = requests.get(url=url, headers=ua).text

    ex = '<div class="slist">.*?<img src="(.*?)" alt.*?</div>'
    img_src_list = re.findall(ex, img_text, re.S)
    print(img_src_list)

#    for scr in img_src_list:
#        src = 'https:' + src
#        img_data = requests.get(url=src, headers=ua).content
#        img_name = src.split('/')[-1]
#        imgpath = './tuku_img/' + img_name
#        with open(imgpath, 'wb') as file:
#            file.write(img_data)