#coding=utf-8
import sqlite3 # 导入sqlite3模块

db = sqlite3.connect(r'D:/SQLdb/main.db') # 连接数据库，指定数据库的路径
course = db.cursor() # 创建游标
course.execute('select * from accounts;') # 执行sql语句
res = course.fetchall() # 获取sql执行结果
print(res)

course.close() #关闭游标
db.commit() #提交数据库事务
db.close() #关闭数据库连接



