#coding=utf-8
import xlrd # 导入操作excel表格的xlrd模块

data = xlrd.open_workbook("E:/samples/excelddtdriver/common/debug_api.xlsx") # 将打开的excel文件，进行数据提取
table = data.sheet_by_name("Sheet1") # 打开表格名称页签

keys = table.row_values(0) # 获取表格中的第一行数据，一般为表格字段的名称
print(keys)
rowNum = table.nrows # 获取表格总行数
colNum = table.ncols # 获取表格总列数
r = [] # 定义空列表

for i in range(rowNum): # 循环迭代，依次获取每一行数据
    s = {} # 定义空字典
    if i == 0: # 判断当行数为第一行时
        continue # 跳过本次循环，直接进入下一下循环
    values = table.row_values(i) # 获取数据内容行信息

    for j in range(colNum):
        s[keys[j]] = values[j]
    r.append(s)
print(r)
