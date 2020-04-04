#coding=utf-8

import csv

def get_csv_data():
    data_list = []
    with open(r'D:\360MoveData\Users\ChunhuaGuo\Desktop\data\del\jy_del\4-3\13263626246\13263626246_18.csv', 'r') as f:
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

data_list = get_csv_data()
# print(tt)
# print(type(tt))
new_set = set(data_list)
new_list = list(new_set)
for i in new_list:

    with open(r'D:\360MoveData\Users\ChunhuaGuo\Desktop\data\del\jy_del\4-3\13263626246\13263626246_18_qc.csv', 'a') as data:
        print(i, file=data)