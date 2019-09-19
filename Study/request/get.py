#coding=utf-8
import requests

url = "http://japi.juhe.cn/qqevaluate/qq"
data = {
    "qq": "371118530",
    "key": "dea9434b9ff25e9d17835d25f7beb24c"
}
r = requests.get(url, params=data)
res = r.json()
print(res)
print(res['result']['data']['conclusion'])
print(res['result']['data']['analysis'])