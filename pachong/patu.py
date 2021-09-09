#思路问题

# 0.导入库（框架，模块）  pip  install xxxxxx
import requests
import re

# 1.确定网址
url = 'https://www.doutula.com/photo/list/'
# 1.5 添加ua    字典{key:value
ua = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36'}

# 2.发起请求(requests)  文本，字符串（text）   视频  音频  图片（content）
html_str = requests.get(url,headers=ua).text

# 3.筛选数据  正则：用特殊符号代替特殊意义的
image_urls = re.findall('data-original="(.*?)"',html_str)

for image_url in image_urls:
    image=requests.get(image_url,headers=ua).content
    image_name=image_url.split('/')[-1]
#    file = open('tupian.jpg','wb')
#    file.write(image)
#   file.close()
# 4.保存数据
    with open('./pachong/%s'%image_name,'wb') as file:
        file.write(image)