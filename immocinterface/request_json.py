#coding=utf-8
import requests
import json

url1 = "http://www.kuaidi.com/"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36",
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "X-Requested-With": "XMLHttpRequest"

}

s = requests.session()
r1 = s.get(url1, headers=header, verify=False)
#追加cookie
c = requests.cookies.RequestsCookieJar()
c.set('lang','zh-cn')
c.set('theme','default')
c.set('sid','n8f5n8ks3l9tbbsna8nra4v370')
c.set('UM_distinctid','16ca38a83921d0-006b86709b167d-c343162-1fa400-16ca38a8393912')
c.set('CNZZDATA1254194234','707768770-1566109166-%7C1566109166')
s.cookies.update(c)


url2 = "http://www.kuaidi.com/index-ajaxselectinfo-1202247993797.html"

r2 = s.get(url2, headers=header, verify=False)
result = r2.json()
print(type(result))

print(result['9']['name'])
print(result['9']['exname'])
print(result['9']['ico'])
print(result['9']['url'])
print(result['9']['phone'])