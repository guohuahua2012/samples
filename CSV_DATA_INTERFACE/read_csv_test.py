# -*- coding: utf-8 -*-

import csv
import json
datas = []
try:
    file_path = 'C:/Users/ChunhuaGuo/Desktop/data.csv'
    with open(file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for line in reader:
            data = {}
            data['id'] = line['id']
            data['url'] = line['url']
            data['mobile'] = line['mobile']
            data['token'] = line['token']
            data['expect'] = json.dumps(line['expect'])\
            if isinstance(line['expect'],dict)\
            else line['expect']
            datas.append(data)
        print(datas)
except FileNotFoundError:
    print('文件不存在')