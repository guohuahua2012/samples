#coding=utf-8
import requests

url = "https://zzk.cnblogs.com/s?t=b&w=python"
params = {
    "t": "b",
    "w": "python"
}
r = requests.get(url)
print(r.status_code)
print(r.content.decode('utf-8'))
