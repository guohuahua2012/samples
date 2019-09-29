#coding=utf-8
import xlrd

data = xlrd.open_workbook('E:/samples/Flask/testFile/case/test01.xlsx')
table = data.sheet_by_name('Sheet1')

keys = table.row_values(0) # 获取第一行的标题

nrows = table.nrows # 获取总行数
ncols = table.ncols # 获取总列数

r = []

for i in range(nrows): # 迭代循环依次取行数 ，共nrows行
    s = {}
    if i == 0:
        continue
    values = table.row_values(i) # 只取数据行，去除标题行

    for x in range(ncols): #迭代循环依次取列数 0,1
        #print("第'{0}'行时,keys的值为'{1}',values的值为'{2}'".format(i+1,keys[x],values[x])) # 迭代循环依次取列数
        s[keys[x]] = values[x] # 定义字典的k=v值

    r.append(s) #将每次迭代的结果s值，追加到列表r中
print(r)
