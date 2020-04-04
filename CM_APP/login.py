#coding=utf-8

import requests

# username = input("请输入用户名：")
# password = input("请输入密码：")
#
# url = "https://v5.chemi.ren/140afc8537f80b7d/login/login"
#
# headers = {
#     "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8"
# }
#
# data = {
#     "username": 18198247429,
#     "password": 'FH8764#785g'
# }
#
# res = requests.post(url, headers=headers, data=data, verify=False)
#
# token = res.headers['Token']
#
# print(token)

def update_coupon(user_id,update_type,update_num,remarks):
    '''

    :param user_id: 用户ID
    :param update_type: 类型：1-使用券；2-服务点；3-活跃值；
    :param update_num: 修改数量；正数为充值，负数为扣除
    :param remarks: 补发添加备注
    :return:
    '''
    url = "http://192.168.1.39/adminapi/user/charge"
    headers = {
        "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
        "token":"322d1cbd48d259cf093c048582cc9264"
    }

    data = {
        "id": user_id,
        "type": update_type,
        "num": update_num,
        "infoa": '后台充值',
        "infos": remarks
    }

    res = requests.post(url, headers=headers, data=data, verify=False)
    return res.json()['msg']



