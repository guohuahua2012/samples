#coding=utf-8

import requests
import bs4
import csv

def get_csv_data():
    data_list = []
    with open(r'D:\360MoveData\Users\ChunhuaGuo\Desktop\CM\unblock\4-4\No1.csv', 'r') as f:
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

def remov_blacklist(No_id):
    url = "http://192.168.1.191:9113/move/{0}".format(No_id)
    res = requests.get(url)
    return res
def get_No(mobile):
    res = requests.get("http://192.168.1.191:9113/index/1?mobile={0}".format(mobile))

    soup = bs4.BeautifulSoup(res.text, "html.parser")
    targets = soup.find_all("table", class_="table")
    for each in targets:
        no_id = each.td.text
        if no_id == '暂无数据':
            continue
        else:
            print(no_id)
        # return no_id


mobile = get_csv_data()
for i_mobile in mobile:
    no_id = get_No(i_mobile)
    print(no_id)




