# -*- coding: utf-8 -*-
import requests
import json

class RunMain():
    # 定义一个方法，传入需要的参数url和data
    def send_post(self, url, data):
        # 参数必须按照url、data顺序传入
        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        result = requests.post(url=url, data=data, headers=headers).json() # 因为这里要封装post方法，所以这里的url和data值不能写死
        res = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2)
        return res

    def send_get(self, url, data):
        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        result = requests.get(url=url, data=data, headers=headers).json()
        res = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2)
        return res

    def run_main(self, method, url=None, data=None): #定义一个run_main函数，通过传过来的method来进行不同的get或post请求
        result = None
        if method == 'post':
            result = self.send_post(url, data)
        elif method == 'get':
            result = self.send_get(url, data)
        else:
            print("method值错误！！！")
        return result

if __name__ == '__main__':
    result = RunMain().run_main('get', 'http://127.0.0.1:8888/login', 'name=xiaoming&pwd=')
    print(result)

