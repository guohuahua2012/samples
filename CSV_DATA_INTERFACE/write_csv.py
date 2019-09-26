# -*- coding: utf-8 -*-
import csv
import requests

#组合请求接口
url = 'https://www.juhe.cn/box/newtest'
params = {
    'requesttypesel':'GET',
    'params':'{"fid":""}',
    'apiid':170
}
headers = {
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'acw_tc=76b20ffe15669044054942006e3baeed424b7bd43a3983c18c2cb10b318e03; JuheChannel=jHwww-juhe-cn; hasReg=reged; aliyungf_tc=AQAAAIcJ820JRAUAgUh5bxdtXG9O+nyh; Hm_lvt_5d12e2b4eed3b554ae941c0ac43c330a=1568945232,1569292498,1569383724,1569458299; PHPSESSID=l2q8d7gccirva84poqab59cfv5; XSRF-TOKEN=eyJpdiI6IkkycG91ckhQWFZ3dnRuXC9VYW9Tc3hRPT0iLCJ2YWx1ZSI6IkdJZENtdWpBeGdIMExTNTdzSjY5M0V2aXREenZnb2xxajJSak05RW1wdVwvNmxsXC9qYVVDOVR0N3daTFgrQnRiRllSeTRkK1hENm5XXC95VEpKV1l2d25nPT0iLCJtYWMiOiIwMGY4NmRkZjE4OGFjYjQ2YTJmNDA2ZGEyNzE4NDFhYmNkMWU1NzM3NTNkMjRjMGJhNzY5NTYyOTg3OTM2Njk0In0%3D; juhe_cn_session=eyJpdiI6IlwvY0J4ZXhXZCswcllUMHdybGlQa2l3PT0iLCJ2YWx1ZSI6ImRKektXRVNJa3dxcUl3cHJvSjhhcnVvVXRaK3h2VXNkS3FMRW1pT1E1M2ZFZm1KZCt1c3VGTWpJWFo5NXZDVmRhNUJuM2loOEo1eThHTWZMcHVNZUdBPT0iLCJtYWMiOiI2YmI2NGRkMjNjOWFmOWFjMTk4YWVhOWEzYmQ5NjVjMzRjOTUyMmJkZWFmNzc5ODQ1YjczNWRlNjViMTI2NWJmIn0%3D; Hm_lpvt_5d12e2b4eed3b554ae941c0ac43c330a=1569467077'
}
r = requests.post(url,data=params,headers=headers)
r_content = r.content.decode('utf-8') #以content的格式返回数据
r_content_dict = eval(r_content) #使用eval()函数将字符串转换为dict格式
r_content_dict_response = r_content_dict['data']['response'] # 获取dict字典key的data下response的values值
#使用字符串str的replace()方法，替换掉转义字符'\r\n\t'、'&quot'和分号';'
r_content_dict_response_dict = r_content_dict_response.replace('\r\n\t','')
r_content_dict_response_dict = r_content_dict_response_dict.replace('&quot','')
r_content_dict_response_dict = r_content_dict_response_dict.replace(';','"')
r_content_dict_response_dict = eval(r_content_dict_response_dict)

#写文件
file = open('C:/Users/ChunhuaGuo/Desktop/test2.csv', 'w+', newline='', encoding='utf-8')
#设置文件的标题，表头
headers = ['id','name','fid']
#以Dictwriter的方式写文件
writer = csv.DictWriter(file, fieldnames=headers)
#写表头
writer.writeheader()
#获取response返回字典数据中，key为'result'的values值，作为写入文档的值

tt = r_content_dict_response_dict['result']
print(tt)
print(type(tt))
for item in tt:
    writer.writerow(item)

file.close()

