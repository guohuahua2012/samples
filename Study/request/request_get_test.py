# -*- coding: utf-8 -*-
import requests
import json

url = 'http://japi.juhe.cn/qqevaluate/qq'

params = {
    'qq': 371118530,
    'key': "dea9434b9ff25e9d17835d25f7beb24c"
}

r = requests.get(url,params=params)
print("get请求获取的响应结果json类型",r.text)
print("get请求获取响应状态码",r.status_code)
print("get请求获取响应头",r.headers['Content-Type'])

#响应的json数据 转换为可被python识别的数据类型
json_r = r.json()
print(json_r)