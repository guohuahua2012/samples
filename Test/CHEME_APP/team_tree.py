#coding=utf-8

import requests
import sys
sys.setrecursionlimit(1000000)

def get_user_tree(user_id):
    # url = "http://192.168.1.39/adminapi/user/user_tree" #测试
    url = "https://v5.chemi.ren/140afc8537f80b7d/user/user_tree"
    headers = {
        "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
        "token":"ca01882cd15e1cdcf60fbcc1f0012e92"
        # "token":"ec2682bd8bbff281e6ad8b2b4eeb2871" #测试
    }

    data = {
        "id":user_id,
        "type":1
    }

    res = requests.post(url, data=data, headers=headers, verify=False)
    res_json = res.json()
    # print(res_json)
    data_json = res_json['data']
    user_tree_id = []
    for i in data_json:
        if i['children'] == True: #有下级
            user_tree_id.append(str(i['id']))
            user_tree_id.extend(get_user_tree(i['id']))

        else: #无下级
            user_tree_id.append(str(i['id']))

    return user_tree_id


def write_csv_data(userid_data_list):
    for user_id_number in userid_data_list:
        with open(r'D:\360MoveData\Users\ChunhuaGuo\Desktop\CM\kick\team\1681357\2314051\1879178_n.csv', 'a') as data:
            print(user_id_number, file=data)


team = get_user_tree(1879178)
write_csv_data(team)

