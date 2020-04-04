#coding=utf-8

import requests
import time

for i in range(1,2):
    # data_list = []
    url = "https://v5.chemi.ren/140afc8537f80b7d/deal/index"
    headers = {
        "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
        "token":"a3a6e7d749dbc18990bb4a3b226d03cd"
    }

    data = {
        "page":i,
        "buy_uid":3413078,
        "status":3
    }
    time.sleep(3)
    res = requests.post(url, headers=headers, data=data, verify=False)
    data_json = res.json()
    data_id = data_json['data']['data']
    # print(data_id)
    for j in data_id:
        data_list = j['user_id']
        # data_list.append(j['user_id'])

        with open(r'D:\360MoveData\Users\ChunhuaGuo\Desktop\data\del\jy_del\4-3\13263626246_1.csv', 'a') as data:
            print(data_list, file=data)
