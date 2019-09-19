# -*- coding: utf-8 -*-
import mysql.connector

config = {
    'host': "localhost",
    'user': "root",
    'passwd': "mysqldbpassword",
    'port': 3306,
    'database': "test2_db",
    'charset': "utf8",
    'auth_plugin': "mysql_native_password"
}

try:
    db = mysql.connector.connect(**config)

except mysql.connector.Error as e:
    print("连接数据库失败！",str(e))

cursor = db.cursor(buffered=True)
try:
    sql_del = "delete from test where name=%s and url=%s"
    data_del = [
        ("xiao","url1"),
        ("xian","url2"),
        ("rourou","url3")
    ]
    cursor.executemany(sql_del,data_del)
    db.commit()
except mysql.connector.Error as e:
    print("删除数据失败！",str(e))
finally:
    cursor.close()
    db.close()