# -*- coding: utf-8 -*-

import csv
import json

def readCSV(filename):
    datas = []
    try:
        with open(filename, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for i in reader:
                data = {}
                data['id'] = i['id']
                data['url'] = i['url']
                data['mobile'] = i['mobile']
                data['token'] = i['token']
                data['expect'] = json.dumps(i['expect'])\
                if isinstance(i['expect'],dict)\
                else i['expect']
                datas.append(data)
            print(datas)
            return datas
    except FileNotFoundError:
        print("文件不存在",filename)
        return datas

file_path = 'C:/Users/ChunhuaGuo/Desktop/data.csv'
readCSV(file_path)