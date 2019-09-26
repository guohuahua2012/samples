#coding:utf-8
import re
import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
import json

#新建session
s = requests.session()
#登录地址
login_url = "https://www.juhe.cn/login"

def get_cookies(login_url):
    #启动浏览器获取浏览器cookies
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(login_url)
    driver.find_element_by_xpath('//*[@id="username"]').send_keys("18198247429")
    driver.find_element_by_xpath('//*[@id="password"]').send_keys("Gwx123456")
    driver.find_element_by_xpath('//*[@id="loginBtn"]').click()
    time.sleep(3)
    cookie = driver.get_cookies() #获取浏览器cookies
    driver.quit()
    return cookie

def add_cookies(cookie):
    #往session添加cookies
    c = requests.cookies.RequestsCookieJar()
    for i in cookie:
        c.set(i['name'],i['value'])
    s.cookies.update(c) #更新session里的cookie
    return s

def read_csv(filename):
    datas = []
    try:
        with open(filename,'r') as csvfile:
            #从文件里读取到数据转换成字典列表
            reader = csv.DictReader(csvfile)
            for i in reader:
                data = {}
                data['caseid'] = i['caseid']
                data['method'] = i['method']
                data['url'] = i['url']
                data['params'] = i['params']
                data['headers'] = i['headers']
                data['expect'] = json.dumps(i['expect']) \
                if isinstance(i['expect'],dict) \
                else i['expect']
                datas.append(data)
            return datas
    except FileNotFoundError:
        print("文件不存在",filename)
        return datas

def post_request(url,params,headers):
    r = s.post(url,data=params,headers=headers)
    return r


if __name__ == '__main__':
    cookie = get_cookies(login_url)
    add_cookies(cookie)
    #文件路径
    file_path = "C:/Users/ChunhuaGuo/Desktop/api.csv"
    #获取参数url、params、headers
    url = read_csv(file_path)[0]['url']
    file_params = read_csv(file_path)[0]['params']
    file_headers = read_csv(file_path)[0]['headers']
    #将参数格式转换成dict
    params = eval(file_params)
    headers = eval(file_headers)

    result = post_request(url,params,headers)
    print(result.text)
