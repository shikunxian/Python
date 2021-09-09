# — 爬虫
# 分析数据
# https://s.askci.com/stock/a/0-0?reportTime=2021-03-31&pageNum=3#QueryCondition
# https://s.askci.com/stock/a/0-0?reportTime=2021-03-31&pageNum=2#QueryCondition
# - 页码
# - 时间


# 思路
# 1. 获取网页源代码
# 2. 提取网页源代码数据
# 3. 保存数据


# 导入
import requests


def get_one_html(page):

    url = 'https://s.askci.com/stock/a/0-0?reportTime=2021-03-31&pageNum={}'.format(page)
    # 发送请求 接收响应
    response = requests.get(url)
    html = response.text
    print(html)

get_one_html(1)
# 数据分析


# web开发