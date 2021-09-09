

import requests
import json
if __name__ == '__main__':
    id_list = []#存储企业id
    all_data_list = []#存储所有的企业详情数据
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'
    }
    url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList'

    for page in range(1, 6):
        page = str(page)
        data = {
            'on': 'true',
            'page': page,#第一页
            'pageSize': '15',#第一页有15条数据
            'productName':'',
            'conditionType': '1',
            'applyname':'',
            'applysn':''
        }

        json_ids = requests.post(url=url, headers=headers, data=data).json()

        for dic in json_ids['list']:#从字典中遍历list列表(json格式化效验)
            id_list.append(dic['ID'])

    #获取企业详情信息
    post_url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList'
    for id in id_list:
        data = {
             'id':id
        }
        datail_json = requests.post(url=post_url, headers=headers, data=data).json()
        all_data_list.append(datail_json)

    #持久化存储
    fp = open('./企业id.json', 'w', encoding='utf-8')
    json.dump(all_data_list, fp=fp, ensure_ascii=False)
    print('结束')