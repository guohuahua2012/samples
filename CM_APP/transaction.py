#coding=utf-8

import requests
import csv


def read_csv(csv_path):
    # 获取用户user_id
    user_id_data = []
    with open('{}'.format(csv_path), 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            user_id = str(row).strip('[]').strip("'")  # 格式化数据为str
            user_id_data.append(user_id)
    return user_id_data


def get_data_transaction(user_id,page=0):
    url = "https://v5.chemi.ren/140afc8537f80b7d/deal/index"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "token": "ee3b4d4ddf31fc23f21a43b50be58c76"
    }

    data1 = {
        "page":page,
        "buy_uid":user_id,
        "status":3
    }

    res1 = requests.post(url, headers=headers, data=data1, verify=False) #买
    # res2 = requests.post(url, headers=headers, data=data2, verify=False) #卖
    return res1.json()

def get_data_buy(user_id, page=0):
        url = "https://v5.chemi.ren/140afc8537f80b7d/deal/index"
        headers = {
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "token": "ee3b4d4ddf31fc23f21a43b50be58c76"
        }
        data2 = {
            "page": page,
            "user_id": user_id,
            "status": 3
        }

        # res1 = requests.post(url, headers=headers, data=data1, verify=False)  # 买
        res2 = requests.post(url, headers=headers, data=data2, verify=False)  # 卖
        return res2.json()

def chuli_data(res1,res2,user_id):
    #交易数据
    data = {}
    res1_total = res1['data']['total']
    res2_total = res2['data']['total']
    res1_last_page = res1['data']['last_page']
    res2_last_page = res2['data']['last_page']
    if res1_total != 0 and res2_total != 0:
        # 取卖家数据
        trans_user_id = []
        buy_user_id = []
        if res1_last_page > 1 and res2_last_page > 1:

            for page_num in range(1, res1_last_page + 1):
                page1 = get_data_transaction(user_id, page_num)
                transaction_id_list = page1['data']['data']
                for u_id in transaction_id_list:
                    trans_user_id.append(u_id['user_id'])
                    data[user_id] = trans_user_id
                return data
            for page_num in range(1, res2_last_page + 1):
                page2 = get_data_buy(user_id, page_num)
                buy_id_list = page2['data']['data']
                for u_id in buy_id_list:
                    buy_user_id.append(u_id['buy_uid'])
                    data[user_id] = buy_user_id
                return data
            return data
        else:
            page1 = get_data_transaction(user_id)
            transaction_id_list = page1['data']['data']
            for u_id in transaction_id_list:
                trans_user_id.append(u_id['user_id'])
                data[user_id] = trans_user_id
                return data

            page2 = get_data_buy(user_id)
            buy_id_list = page2['data']['data']
            for u_id in buy_id_list:
                trans_user_id.append(u_id['buy_uid'])
                data[user_id] = trans_user_id
                return data
        return data
    else:
        print('不处理')

    return data




user_list = read_csv(r'D:\360MoveData\Users\ChunhuaGuo\Desktop\data\del\data\new\test.csv')
for u_id in user_list:
    res1 = get_data_transaction(u_id)
    res2 = get_data_buy(u_id)
    res3 = chuli_data(res1, res2, u_id)
    print(res3)











