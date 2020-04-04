#coding=utf-8

import requests

url = "https://v5.chemi.ren/140afc8537f80b7d/user/user_tree"

headers = {
    "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
    "token":"ca01882cd15e1cdcf60fbcc1f0012e92"
}

data = {
    "id":1817262,
    "type":1
}

res = requests.post(url, headers=headers, data=data, verify=False)
data_list = res.json()['data']
for data in data_list:
    id = data['id']
    if data['children'] == True:

        print('父子级id:' + str(id))
    else:
        with open(r'D:\360MoveData\Users\ChunhuaGuo\Desktop\CM\kick\team\1681357\2314051\1817262_25.csv', 'a') as data:
            print(id, file=data)

