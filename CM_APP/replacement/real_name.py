#coding=utf-8
# 实名认证
import csv
import requests

def read_csv(file_path):
    row_data = []
    with open(file_path, 'r', encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            row_data.append(row)
    return row_data

def real_userId(user_id,user_name,card_num):
    url = "https://v5.chemi.ren/140afc8537f80b7d/user/authentication"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "token": "6c0d7d40d88a411062d0bc0b608c3a2b"
    }
    data = {
        "id": user_id,
        "true_name": user_name,
        "id_card": card_num
    }

    res = requests.post(url, headers=headers, data=data, verify=False)
    return res.json()['msg']

data = read_csv(r'D:\360MoveData\Users\ChunhuaGuo\Desktop\CM\replacement\real_name\4-10\3\user_info_410_3.csv')
print(data)

for i_data in data:
    msg = real_userId(i_data[0],i_data[1],i_data[2])
    with open(r'D:\360MoveData\Users\ChunhuaGuo\Desktop\CM\replacement\real_name\4-10\3\user_info_410_3_res.csv', 'a', encoding='utf-8') as data:
        print(i_data[0],i_data[1],i_data[2],msg, file=data)