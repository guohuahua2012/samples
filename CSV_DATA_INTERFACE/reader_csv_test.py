# -*- coding: utf-8 -*-

import csv

with open('C:/Users/ChunhuaGuo/Desktop/test.csv', 'r+', newline='',encoding='utf-8') as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        pass
        #print(str(row))



for d in csv.DictReader(open('C:/Users/ChunhuaGuo/Desktop/test.csv','r+', newline='')):
    print(d)