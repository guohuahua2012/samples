# -*- coding: utf-8 -*-
import requests

def get(url,params,headers=None):
    try:
        r = requests.get(url,params=params,headers=headers)
        print("获取返回状态码",r.status_code)
        r_json = r.json()
        print("json类型转化成python数据类型",r_json)
    except BaseException as e:
        print("请求失败！",str(e))

def post(url,params,headers=None):
    try:
        r = requests.post(url,params=params,headers=headers)
        print("获取返回状态码",r.status_code)
        r_json = r.json()
        print("json类型转化成python数据类型",r_json)

    except BaseException as e:
        print("请求失败！",str(e))

url = 'http://v.juhe.cn/weixin/query'
params = {
    'pno': "",
    'ps': "",
    'dtype': "",
    'key': "62c68a3f8f640246909eb9fdfffd5cc2"
}

get(url,params)
post(url,params)
