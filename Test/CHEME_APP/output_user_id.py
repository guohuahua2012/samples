#coding=utf-8

import requests
import csv

def get_csv_data():
    data_list = []
    with open(r'D:\360MoveData\Users\ChunhuaGuo\Desktop\data\data\14.csv', 'r') as f:
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

def get_classify_num(user_id):
    '''
    任务包产出量
    :param user_id: 用户ID
    :return: 返回该user_id任务包产出的数量
    '''
    url = "https://v5.chemi.ren/140afc8537f80b7d/classify/order"

    headers = {
        "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
        "token":"fa6e8cfef57bb990b74aec30deb22a2d"
    }

    data = {
        "user_id":user_id
    }

    res = requests.post(url, headers=headers, data=data, verify=False)
    # print(res.json())
    output_yj_str = res.json()['data']['data'][0]['output_yj']
    output_yj = float(output_yj_str)
    # print(output_yj)
    return output_yj


def requests_url(user_id, page=0):
    '''
    交易订单接口
    :param user_id:
    :param page: 默认第一页
    :return:
    '''
    url = "https://v5.chemi.ren/140afc8537f80b7d/deal/index"
    headers = {
        "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
        "token":"fa6e8cfef57bb990b74aec30deb22a2d"
    }
    data = {
        "page": page,
        "user_id": user_id,
        "status": 3
    }

    res = requests.post(url, headers=headers, data=data, verify=False)
    return res.json()

def get_transaction_sell(res):
    res = res
    # print(res)
    user_id = res['data']['data'][0]['user_id']
    last_page = res['data']['last_page']
    sell_sum = 0
    if last_page == 1:
        print('只有一页')
        r = requests_url(user_id)
        # print(r)
        data_list = r['data']['data']
        # print(data_list)
        for j in data_list:
            # print(j)
            sell_sum += j['num']
        return sell_sum
    else:
        print('只有n页')
        #请求页面

        for i in range(1, last_page + 1):
            data_list_dict = requests_url(user_id, i)
            # print(data_list_dict)
            # print(type(data_list_dict))
            data_list = data_list_dict['data']['data']
            for j in data_list:
                # print(j)
                sell_sum += j['num']

            return sell_sum
        return sell_sum



def for_data(data):
    for i in data:
        # print(i)
        classify_num = get_classify_num(i)

        res = requests_url(i)
        # print(res)
        # print(res['data']['last_page'])
        #
        if res['data']['last_page'] == 0:
            continue
        else:
            sell_all = get_transaction_sell(res)

        if classify_num < sell_all:
            id = res['data']['data'][0]['user_id']
            with open(r'D:\360MoveData\Users\ChunhuaGuo\Desktop\data\data\14_new.csv', 'a') as data_list:
                print(id, file=data_list)




data = get_csv_data()
for_data(data)




