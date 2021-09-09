#encoding=utf-8
import requests
import re
import os
if __name__ == '__main__':
    #创建一个文件夹，保存所有图片
    if not os.path.exists('./qiutuLibs'):
        os.mkdir('./qiutuLibs')#如果文件夹不存在就自动创建一个
    url = 'https://www.qiushibaike.com/imgrank/'
    ua = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'}
    page_text = requests.get(url=url, headers=ua).text
    #使用正则提取数据
    ex = '<div class="thumb">.*?<img src="(.*?)" alt.*?</div>'
    img_src_list = re.findall(ex, page_text, re.S)
    print(img_src_list)

    for src in img_src_list:
        src = 'https:'+src
        #拼接出一个完整的图片url（网址）
        img_data = requests.get(url=src, headers=ua).content
        #生成图片名称
        img_name = src.split('/')[-1]
        imgpath = './qiutuLibs/'+img_name
        with open(imgpath, 'wb') as file:
            file.write(img_data)