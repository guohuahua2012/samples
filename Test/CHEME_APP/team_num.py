#coding=utf-8

import requests

def get_team_data(user_id):
    url = "https://v5.chemi.ren/140afc8537f80b7d/user/user_tree"

    headers = {
        "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
        "token":"980c5d26b9f74a70ef508b16e0e7041a"
    }

    data = {
        "id":'{0}+qqq'.format(user_id),
        "type":1
    }

    res = requests.post(url, data=data, headers=headers, verify=False)
    result_res = res.json()
    user_id = result_res['data'][0]['id']
    user_text = result_res['data'][0]['text']
    print(user_id)
    print(user_text)
    print(type(user_text))
    user_team = user_text.split('用户ID')[1].split('(')[2].split(')')
    print(user_team[0])

    with open(r'D:\360MoveData\Users\ChunhuaGuo\Desktop\data\team\11.csv', 'a') as data:
        print(user_id,',',user_team[0], file=data)

get_team_data(3062023)



