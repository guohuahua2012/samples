# -*- coding: utf-8 -*-
import os
import xlrd

class ReadExcel():

    def read_excel(self, cls_name):
        '''
        :cls_name: Excel文件名称
        :return: cls = [{data1}{data2}...]
        '''
        cls_path = os.path.split(os.path.realpath(__file__))[0]
        file_path = os.path.join(cls_path,"testFile", "case", cls_name)
        data = xlrd.open_workbook(file_path)
        table = data.sheet_by_name('Sheet1')

        keys = table.row_values(0)  # 获取第一行的标题
        nrows = table.nrows  # 获取总行数
        ncols = table.ncols  # 获取总列数
        cls = []

        for i in range(nrows):  # 迭代循环依次取行数 ，共nrows行
            data = {}
            if i == 0:
                continue
            values = table.row_values(i)  # 只取数据行，去除标题行

            for x in range(ncols):  # 迭代循环依次取列数 0,1
                # print("第'{0}'行时,keys的值为'{1}',values的值为'{2}'".format(i+1,keys[x],values[x])) # 迭代循环依次取列数
                data[keys[x]] = values[x]  # 定义字典的k=v值
            cls.append(data)  # 将每次迭代的结果s值，追加到列表r中
        return cls

if __name__ == '__main__': #我们执行该文件测试一下是否可以正确获取Excel中的值
    print(ReadExcel().read_excel('test01.xlsx'))
    print(ReadExcel().read_excel('test01.xlsx')[0])
    print(ReadExcel().read_excel('test01.xlsx')[0]['case_name'])
    print(ReadExcel().read_excel('test01.xlsx')[0]['path'])
    print(ReadExcel().read_excel('test01.xlsx')[0]['query'])
    print(ReadExcel().read_excel('test01.xlsx')[0]['method'])
