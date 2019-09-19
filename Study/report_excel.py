#coding=utf-8
import xlrd

class ExcelUtil():
    def __init__(self, excelPath, sheetName):
        self.data = xlrd.open_workbook(excelPath)
        self.table = self.data.sheet_by_name(sheetName)
        # 获取第一行数据作为key值
        self.keys = self.table.row_values(0)
        # 获取总行数
        self.rowNum = self.table.nrows
        # 获取总列数
        self.colNum = self.table.ncols



    def dict_data(self):
        if self.rowNum <= 1:
            print("总行数小于1")
        else:
            r = []
            j = 1
            # 内容行数 = 总行数 - 标题行
            for i in range(self.rowNum - 1):
                s = {}
                # 从第二行取对应values值
                values = self.table.row_values(j)
                for x in range(self.colNum):
                    s[self.keys[x]] = values[x]
                r.append(s)
                j += 1
        return r

if __name__ == '__main__':
    filepath = 'C:/Users/ChunhuaGuo/Desktop/进出场播报规则.xlsx'
    sheetName = 'Sheet2'
    data = ExcelUtil(filepath, sheetName)
    print(data.dict_data())
    print(data.dict_data()[0])
    print(data.dict_data()[0]['username'])
    print(data.dict_data()[0]['password'])