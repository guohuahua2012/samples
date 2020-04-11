#coding=utf-8

import requests
import csv

def get_csv_data():
    data_list = []
    with open(r'D:\360MoveData\Users\ChunhuaGuo\Desktop\CM\replacement\real_name\4-10\3\mobile.csv', 'r') as f:
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
        "token":"6c0d7d40d88a411062d0bc0b608c3a2b"
    }

    data = {
        "mobile":mobile
    }

    res = requests.post(url, headers=headers, data=data, verify=False)
    # print(res.json())
    # print(res.json()['data']['data'][0]['id'])
    return res.json()


data_list = get_csv_data()
for i in data_list:
    user_id = get_user_id(i)
    total = user_id['data']['total']
    if total == 0:
        with open(r'D:\360MoveData\Users\ChunhuaGuo\Desktop\CM\replacement\real_name\4-10\3\mobile_id.csv', 'a', encoding='utf-8') as data:
            print(i,'手机号未注册', file=data)
        continue
    else:
        id = user_id['data']['data'][0]['id']
        with open(r'D:\360MoveData\Users\ChunhuaGuo\Desktop\CM\replacement\real_name\4-10\3\mobile_id.csv', 'a') as data:
            print(id, file=data)
# user_id = get_user_id(18021946159)
# print(user_id)