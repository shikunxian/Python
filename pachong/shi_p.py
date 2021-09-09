import requests
from lxml import etree# lxml是XML和HTML的解析器，其主要功能是解析和提取XML和HTML中的数据
import re#引用正则表达式

# 1.确定网址
url = 'https://maoyan.com/news?showTab=3'

# 有反爬，添加User-Agent(用户代理人)
ua = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'}

cookie = {'Cookie': 'uuid_n_v=v1; _lxsdk_cuid=17ba0ae242cc8-0fe070f7cfdec3-a7d193d-e1000-17ba0ae242cc8; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; uuid=D85A66500B1311ECA0A0A7D672FC3854D409C27BC2EC4A3F83E9187421674B84; _csrf=ab45702e6a4345ceefcda35231d27839e61bd3d00538ba1df71bb54dc6d147c4; lt=WW0Ow90ELkUkeamXUAGCu_9eFEcAAAAAbg4AAJlmzL763eIEdCF7KEpMwjWgYyza15ma_yi3SX66RJ1K1A-aFZrVH0ZamH7EuqKlhg; lt.sig=NrmRcJWmYeWLoig06MCKEH4bD64; uid=2723224492; uid.sig=vBj36TFEkh3LYNQYYQZwfbN365A; _lxsdk=D85A66500B1311ECA0A0A7D672FC3854D409C27BC2EC4A3F83E9187421674B84; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1630488372,1630493050,1630494041; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1630496489; __mta=146595339.1630488372456.1630494188101.1630496488879.13; _lxsdk_s=17ba129f9a4-fba-0be-5fa%7C2723224492%7C4'}

# 2.发送请求
html_str = requests.get(url,headers=ua).text
dom = etree.HTML(html_str)
mp4_urls = dom.xpath('//h4/a/@href')#xpath是一门在XML文档中查找信息的语言。xpath可用来在XML文档中对元素和属性进行遍历。
mp4_names = dom.xpath('//h4/a/text()')


# 3.筛选数据
for mp4_url,mp4_name in zip(mp4_urls, mp4_names):
    mp4_string = requests.get(mp4_url, headers=ua, cookies=cookie).text
    mp4_str_res = re.search('<source src="(.*?)"', mp4_string).group(1)
#    print(mp4_url)#打印的是网址
    print(mp4_name)#打印的是文字标题
#    print(mp4_str_res)
#    mp4 = requests.get(mp4_str_res).content
# 4.下载数据,保存数据
#    with open('./shipin/%s.mp4'%mp4_name, 'wb') as file:
#        file.write(mp4)
