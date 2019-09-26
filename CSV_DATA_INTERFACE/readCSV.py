# -*- coding: utf-8 -*-
import csv
import json
import requests
import time
import unittest

class ReadCSV():

    #reader_CSV函数代码示例
    def readCSV(self,filename):
        '''
        :param filenam :需要读取的数据文件
        :return :[{data1},{data2}...]
        '''
        datas = []
        try:
            #以DictReader的方式读取数据文件，方便与json互做转换
            with open(filename, 'r') as csvfile:
                #从文件里读取到数据转换成字典列表的格式
                reader = csv.DictReader(csvfile)
                for i in reader:
                    data = {}
                    data['id'] = i['id']
                    data['url'] = i['url']
                    data['params'] = i['params']
                    data['expect'] = json.dumps(i['expect']) \
                    if isinstance(i['expect'], dict) \
                    else i['expect'] #如果expect读取出来不是json则取其原值，否则转为json格式保存到result
                    datas.append(data)
                return datas
        except FileNotFoundError:
            print("文件不存在", filename)
            return datas

    #request_get函数示例
    def get_request(self,url,params):
        '''
        通过的调用GET接口方法
        :param url: string 接口路径
        :param params: {"":"","":""} 需要传入的参数
        :return: response响应体
        '''
        print("调用API...")
        r = requests.get(url,params=json.loads(params))
        print(r.json())
        return r

    #request_post函数示例
    def post_request(self,url,params):
        '''
        通过调用POST接口方法
        :param url: string 接口路径
        :param params: {"":"","":""}需要传入的参数
        :return: response响应体
        '''
        print("调用API...")
        headers = {
            'Cookie':'acw_tc=76b20ffe15669044054942006e3baeed424b7bd43a3983c18c2cb10b318e03; JuheChannel=jHwww-juhe-cn; hasReg=reged; aliyungf_tc=AQAAAAPyZho+jQsAqUV5b/i4OhaEpAhz; Hm_lvt_5d12e2b4eed3b554ae941c0ac43c330a=1566904407,1566953413,1568945232,1569292498; PHPSESSID=l9ij31g42dncqs8b39p4u9pv46; Hm_lpvt_5d12e2b4eed3b554ae941c0ac43c330a=1569322490; XSRF-TOKEN=eyJpdiI6ImNRQkVTWEpUTzluYnNKOWtSTmVJNHc9PSIsInZhbHVlIjoiaGIrRUFPMDRkanpscDZadHdXOGVuUVlCVENrT0xUSUE2QStmRUhvbDlYOUxlQWRlZ3BneCtxVDhyeFgyRHRnRVZic1k4T0FwN25RanQwaVRDMWMyK3c9PSIsIm1hYyI6ImE1MWRiZjM1OGUzMDFkNWIwNzI4ODkyMGI3YjY4NDA1Njc5MGE0OTkzMGNjMGU4ZjY5NGY4Njk2NWQ0NTQzYzIifQ%3D%3D; juhe_cn_session=eyJpdiI6IjNWWkJwQUdvY0dwNFwvM0VcL3RpTXNGQT09IiwidmFsdWUiOiJjYjBHT3dqRXZ4aFhKVG5CNGYyMGo3eGRuVjR3eEs5amhjTlBsRmNmSWxMYW8xTlMwSXNuQXZ2a3pIOUtGMnBwMjJZYzBFOXd5MHBiakNyRkFuWXBNQT09IiwibWFjIjoiZTM3YmUxOTEyMmZjNTdjMTY0MjM5M2E5YTg2MDMzZTg1YjJlNWNjMDkzNjNjODM2ZGI5OTMyYmU0NzY2OGViMSJ9',
            'Content-Type':"application/x-www-form-urlencoded; charset=UTF-8"
        }
        r = requests.post(url,data=json.loads(params),headers=headers) #post的方法必须使用json.dumps()转化成json格式
        print(r.text)
        return r

    #assert_Result函数示例
    def assertResult(self,expect_value,real_value):
        '''
        校验样本字符串中是否包含指定字符串
        :param expect_value: string 指定字符串
        :param real_value: string 样本字符串
        :return: Boolean 样本中包含指定字符串返回True,否则返回False
        '''
        ifsuccess = expect_value in str(real_value)
        return ifsuccess

    #write_CSV函数示例
    def writeCSV(self,filename,results):
        '''
        写入csv文件指定内容
        :param filename: string 需要写入的文件名称
        :param results: [{data1},{data2},...] 写入的内容
        :return: 无
        '''
        print("写文件:",filename)
        #以DictWriter的方式写文件
        with open(filename,'w+') as csvfile:
            headers = "id,url,params,expect,real_value,assert_value".split('.')
            write = csv.DictWriter(csvfile,fieldnames=headers)
            #写表头
            write.writeheader()
            #写数据
            if results.__len__() > 0:
                for result in results:
                    write.writerow(result)
            csvfile.close()

    #test_interface 函数示例
    def test_interface(self):

        #指定读取的数据文件名称
        data_file = 'C:/Users/ChunhuaGuo/Desktop/test.csv'

        #指定最终结果生成的数据文件名称
        result_file = '../data/result_{}.csv'.format(str(time.time()).split('.')[0])

        #读取文件指定的数据
        datas =self.readCSV(data_file)

        #数据文件有内容则调用接口，否则直接测试结束
        if datas.__len__() > 0:
            results = []

        #获取数据文件里的每一行
        for testcase in datas:
            result = {}
            result['id'] = testcase['id']
            result['url'] = testcase['id']
            result['token'] = testcase['id']
            result['mobile'] = testcase['id']



tt = ReadCSV()
test_file = 'C:/Users/ChunhuaGuo/Desktop/test.csv'
a = tt.readCSV(test_file)


#b = tt.get_request(a[0]['url'],a[0]['params'])
c = tt.post_request(a[1]['url'],a[1]['params'])
print(c)