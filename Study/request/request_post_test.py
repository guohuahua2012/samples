# -*- coding: utf-8 -*-

import requests
import json

url = 'http://v.juhe.cn/weixin/query'

params = {
    'pno': "",
    'ps' :"",
    'dtype': "",
    'key': "62c68a3f8f640246909eb9fdfffd5cc2"
}

r = requests.post(url,data=params)

print("post请求获取的响应结果json类型",r.text)
print("post请求获取响应状态码",r.status_code)
print("post请求获取响应头",r.headers['Content-Type'])

r_json = r.json()
print(r_json)