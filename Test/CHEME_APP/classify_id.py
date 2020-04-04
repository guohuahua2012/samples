#coding=utf-8

import requests
import csv

def check_classify_id(user_id):
    # 判断用户任务包
    url = "https://v5.chemi.ren/140afc8537f80b7d/classify/order"
    headers = {
        "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
        "token":"4bd5e676738371a562f291575fbf343a"
    }
    data = {
        "user_id":user_id
    }

    res = requests.post(url, headers=headers, data=data, verify=False)
    return res.json()


def check_bicycle(res):

    # 判断有且只有一个单车任务包,讲用户id返回
    classify_name = res['data']['total'] #只有一个任务包
    classify_bicycle = res['data']['data'][0]['classify_id']    # 单车任务包
    if classify_name == 1 and classify_bicycle == 1:
        return res['data']['data'][0]['user_id']

def classify_output_num(res):
    # 求出任务包的产量
    num = res['data']['data'][0]['output_yj']
    num = float(num)
    return num

def sellout_quan(user_id):
    # 交易所买出的券综合
    url = "https://v5.chemi.ren/140afc8537f80b7d/user/quan_log"
    headers = {
        "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
        "token":"4bd5e676738371a562f291575fbf343a"
    }
    data = {
        "user_id":user_id,
        "type":5
    }
    res = requests.post(url, headers=headers, data=data, verify=False)
    num_list = res.json()['data']['data']
    total_num = 0
    for i in num_list:
        num_str1 = i['num']
        num_str2 = num_str1.strip('-')
        num_float = float(num_str2)
        total_num += num_float
    return total_num

cls_id = check_classify_id(14415)
result_user_id = check_bicycle(cls_id)
cls_out_num = classify_output_num(cls_id)
maiquan = sellout_quan(14415)
print(cls_out_num)
print(maiquan)
if cls_out_num < maiquan:
    data_list = cls_id['data']['data'][0]['user_id']
    with open(r'E:\samples\Test\CHEME_APP\data_list.csv', 'a') as data:
        print(data_list, file=data)