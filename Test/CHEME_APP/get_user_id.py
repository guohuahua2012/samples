#coding=utf-8

import requests
import csv

def get_csv_data():
    data_list = []
    with open(r'D:\360MoveData\Users\ChunhuaGuo\Desktop\CM\unblock\4-4\No1.csv', 'r') as f:
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

def get_user_id(mobile):
    url = "https://v5.chemi.ren/140afc8537f80b7d/user/index"

    headers = {
        "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
        "token":"ca01882cd15e1cdcf60fbcc1f0012e92"
    }

    data = {
        "mobile":mobile
    }

    res = requests.post(url, headers=headers, data=data, verify=False)
    # print(res.json())
    # print(res.json()['data']['data'][0]['id'])
    return res.json()['data']['data'][0]['id']


data_list = get_csv_data()
for i in data_list:
    user_id = get_user_id(i)
    # print(user_id)
    with open(r'D:\360MoveData\Users\ChunhuaGuo\Desktop\CM\unblock\4-4\No1_uid.csv', 'a') as data:
        print(user_id, file=data)
# user_id = get_user_id(18021946159)
# print(user_id)