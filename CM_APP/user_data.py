#coding=utf-8

import csv
import requests


token = "6c0a7ca80453839e7c463dfbe452476d"
headers = {
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "token": token
}

# 获取用户数据
def read_csv(csv_path):
    # 获取用户user_id
    user_id_data = []
    with open('{}'.format(csv_path), 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            user_id = str(row).strip('[]').strip("'") #格式化数据为str
            user_id_data.append(user_id)
    return user_id_data

data = read_csv(r'D:\360MoveData\Users\ChunhuaGuo\Desktop\data\del\data\new\test.csv')
print(data)
