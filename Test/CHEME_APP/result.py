#coding=utf-8

import csv
import requests
import time

def get_csv_data():
    data_list = []
    with open(r'D:\360MoveData\Users\ChunhuaGuo\Desktop\data\del\jy_del\4-3\13263626246\13263626246_18_qc.csv', 'r') as f:
        reader = csv.reader(f)
        # print(type(reader))

        for row in reader:
            # print(row)
            data_to_str = str(row)
            # print(data_str)
            # # print(type(data_str))
            data_str = data_to_str.strip('[]')
            data_str = data_str.strip("'")
            data_list.append(data_str)
    return data_list

def post_url(page=0):
    url = "https://v5.chemi.ren/140afc8537f80b7d/deal/index"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "token": "a3a6e7d749dbc18990bb4a3b226d03cd"
    }
    data = {
        "page":page,
        "buy_uid":i,
        "status":3
    }
    res = requests.post(url, headers=headers, data=data, verify=False)
    return res.json()

t = get_csv_data()
# print(t)
# print(len(t))

for i in t:
    time.sleep(0.5)
    ll = post_url()
    last_page = ll['data']['last_page']
    # print(type(last_page))
    if last_page != 0:
        for j in range(1,last_page + 1):
            # print(j)
            time.sleep(0.5)
            jj = post_url(j)
            data_id = jj['data']['data']
            for j in data_id:
                time.sleep(0.5)
                data_list = j['user_id']
                with open(r'D:\360MoveData\Users\ChunhuaGuo\Desktop\data\del\jy_del\4-3\13263626246\13263626246_19.csv', 'a') as data:
                    print(data_list, file=data)

    else:
        continue




