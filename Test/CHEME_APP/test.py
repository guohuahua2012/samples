#coding=utf-8

import requests

def res_json(user_id):
    url = "https://v5.chemi.ren/140afc8537f80b7d/user/user_tree"
    headers = {
        "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
        "token":"4bd5e676738371a562f291575fbf343a"
    }
    data = {
        "id":user_id,
        "type":1
    }
    res = requests.post(url, headers=headers, data=data, verify=False)
    return res.json()

# print(res_json(673996))

def check_children(res):
    children = res.json()
    return children

tt = res_json(673996)
yy = check_children(tt)








