#coding=utf-8

import os
import csv
'''
    读取文件夹下的csv文件
'''
def readAllFiles(filePath):
    file_list = []
    fileList = os.listdir(filePath)
    for file in fileList:
        path = os.path.join(filePath, file)
        if os.path.isfile(path):
            file = open(path, 'r' , encoding='utf-8')
            file_list.append(path)
        else:
            continue
    return file_list


tt = readAllFiles(r'D:\360MoveData\Users\ChunhuaGuo\Desktop\CM\kick\team\1681357\6')

def get_csv_data(csv_path):
    csv_path_list = csv_path
    for i in csv_path_list:
        # print(i)
        with open(r'{0}'.format(i), 'r') as f:
            reader = csv.reader(f)
            # print(type(reader))
    #
            for row in reader:
                # print(row)
                data_to_str = str(row)
                # print(data_to_str)
                # print(type(data_to_str))
                data_str = data_to_str.strip('[]')
                data_str = data_str.strip("'")
                # print(data_str)
                with open(r'D:\360MoveData\Users\ChunhuaGuo\Desktop\CM\kick\team\1681357\6\del-6.csv', 'a') as data:
                    print(data_str, file=data)

    # return data_list
get_csv_data(tt)