# -*- coding: utf-8 -*-
import xlrd

class ReadExecl():

    def readExcel(self, filename, sheetname):
        cls = []

        try:
            data = xlrd.open_workbook(filename)
            table = data.sheet_by_name(sheetname)
            keys = table.row_values(0)
            nrows = table.nrows
            ncols = table.ncols
            for i in range(nrows):
                datas = {}
                if i == 0:
                    continue
                values = table.row_values(i)
                for j in range(ncols):
                    datas[keys[j]] = values[j]
                cls.append(datas)
            return cls

        except FileNotFoundError:
            print("文件不存在", filename)

if __name__ == '__main__':
    xls_file = r'E:/samples/Flask/testFile/case/test01.xlsx'
    xls_sheet = 'Sheet1'
    res = ReadExecl().readExcel(xls_file, xls_sheet)
    print(res)