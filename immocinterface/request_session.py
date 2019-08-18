#coding=utf-8
import requests
# 访问博客园地址
url = "https://account.cnblogs.com/signin?returnUrl="
# 配置请求头信息
header = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"
}

s = requests.session() # 获取登录前会话session值
r = s.post(url, headers=header, verify=False)
#print("旧session是：%s" %s)

# 手动登录后，添加登录后，需要的两个cookie
c = requests.cookies.RequestsCookieJar()
c.set('.Cnblogs.AspNetCore.Cookies','CfDJ8D8Q4oM3DPZMgpKI1MnYlrlyDPazke707S0Y_VzMLSEFonxdcv5TvcHU6tLWLaFtldqjHItQWEK3oo0yrFmAbgAf3L4tSp7wftMv57aSe3VIp5nZ27QKhi5upZRyFg6ftRVtTCxspJ9L8hOvNa7tcAWMij_jiEdpYE7-fjMVi5chrM268mknj42-fgZtXGSmhUgGQiPCgl8T8jdJJDaU7TC8QPYjkUvqPncJfHahN4lY6yfAhYZR1tRnZocs-b9ObkeuCD4bQZ5kUkGPySgoffqrTjudqPJIZ55mtA92EQ0lUXq-aPeKVS1aN5QcC1eUtnEjBpDOzaMd3ryXfn6aO96U_fNxzvDndLgMAG2YlQum6uSbkyUzbfUCn3yQUjI0Lr3F1vzjcFYPf7JmZW9zqW59kMieIiAFLRWvFP3EfTKTFkNRCdG-TwyNRjF7MoJEFw; domain=.cnblogs.com; path=/; httponly')
c.set('.CNBlogsCookie','E79CFE39E338F4A71D2BF8B385450599E823A2BBF347ACA6052A51D09B17C57DF75FF89DA2FAFB932930E9B77395851B84DB25A6FB7145D60F549B1B082396F4FA045F5EE0AE815CC9B2A4F14FAAF9E7AB80F18C; domain=.cnblogs.com; path=/; httponly')
c.set('SERVERID','72a9dcfa61520d2c68e0c62ba3a369c8|1566108783|1566099974;Path=/')
s.cookies.update(c)
#print("新session是：%s" %s.cookies)

# 登录成功后保存编辑内容
url1 = "https://i.cnblogs.com/EditPosts.aspx?opt=1"

r1 = s.get(url1, headers=header, verify=False)
#print(r1.content.decode('utf-8'))

url2 = "https://i.cnblogs.com/EditPosts.aspx?opt=1"
body = {
    "__VIEWSTATE": "",
    "__VIEWSTATEGENERATOR": "FE27D343",
    "Editor$Edit$txbTitle": "验证这是一个软件测试自动化测试的标题",
    "Editor$Edit$EditorBody": "<p>哈哈，每天学习一点点，进步一点点。。。</p>",
    "Editor$Edit$Advanced$ckbPublished": "on",
    "Editor$Edit$Advanced$chkDisplayHomePage": "on",
    "Editor$Edit$Advanced$chkComments": "on",
    "Editor$Edit$Advanced$chkMainSyndication": "on",
    "Editor$Edit$Advanced$txbEntryName": "",
    "Editor$Edit$Advanced$txbExcerpt": "",
    "Editor$Edit$Advanced$txbTag": "",
    "Editor$Edit$Advanced$tbEnryPassword": "",
    "Editor$Edit$lkbDraft": "存为草稿"

}

r2 = s.post(url2, data=body, verify=False)
# content 是字节数据输出
result1 = r2.content.decode('utf-8')
print(result1)
