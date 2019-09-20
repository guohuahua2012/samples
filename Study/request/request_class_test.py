# -*- coding: utf-8 -*-
import requests

class WebRequest():
    def get(self,url,params,headers=None):
        try:
            r = requests.get(url,params=params,headers=headers)
            print("获取返回值的状态码",r.status_code)
            r_json = r.json()
            print("json转化成python数据类型",r_json)
        except BaseException as e:
            print("请求失败！",str(e))

    def post(self,url,params,headers=None):
        try:
            r = requests.post(url,params=params,headers=headers)
            print("获取返回数据的状态码",r.status_code)
            r_json = r.json()
            print("json转化为python数据类型",r_json)

        except BaseException as e:
            print("请求失败！",str(e))

url = 'http://v.juhe.cn/weixin/query'
params = {
    'pno': "",
    'ps': "",
    'dtype': "",
    'key': "62c68a3f8f640246909eb9fdfffd5cc2"
}

res = WebRequest()
res.get(url, params)
res.post(url,params)

