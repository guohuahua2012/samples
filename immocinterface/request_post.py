#coding=utf-8
import requests

# 禅道域名
host = "http://192.168.1.26"

# 定义login函数
def login(s,username,pwd):
    '''
    :param s: s参数为请求request.session的返回内容
    :param username: 登录用户名
    :param pwd: 登录密码
    :return:
    '''
    # 定义请求url地址
    url = host + "/index.php?m=user&f=login"
    # 定义header请求头信息
    header = {
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9"
    }
    # 定义请求体 body 参数信息
    body = {
        "account": username,
        "password": pwd,
        "referer":"http://192.168.1.26/index.php?m=project&f=task&root=1&type=byModule&param=27"
    }

    r = s.post(url, data=body, headers=header) #组合拼装 post 的请求数据
    return r.content.decode('utf-8') #返回字节方式的相应体，并定义utf-8编码格式

# 定义 is_login_sucess 函数，判断登录结果
def is_login_sucess(res):
    '''
    :param res: res参数为请求登录后的数据，即login()的返回值
    :return: 定义登录结果
    '''
    if "登录失败，请检查您的用户名或密码是否填写正确。" in res:
        return "登录失败，请检查您的用户名或密码是否填写正确！"
    elif "parent.location=" in res:
        return "登录成功"
    else:
        return False

if __name__ == '__main__':
    s = requests.session()
    print(s)
    a = login(s,"guochunhua","guochunhua123456")
    print(a)
    result = is_login_sucess(a)
    print("测试结果:%s" %result )