#1.导入框架   pip install xxxxxx

import requests

#2.确定网址  单引号或是双引号引导起来的就是字符串

url = 'https://img0.baidu.com/it/u=1960953056,721704904&fm=26&fmt=auto&gp=0.jpg'

#3.请求  （requests）  图片， 视频， 音频（content） ， 文本，字符串（text）

image = requests.get(url).content

# 3.保存
with open('./tuku_img/tp.jpg', 'wb') as file:
    file.write(image)