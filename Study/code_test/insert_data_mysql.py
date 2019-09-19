# -*- coding: utf-8 -*-
import mysql.connector

config = {
    'host': "localhost",
    'user': "root",
    'passwd': "mysqldbpassword",
    'port': 3306,
    'db': "test2_db",
    'charset': "utf8",
    'auth_plugin': "mysql_native_password"

}

try:
    db = mysql.connector.connect(**config)
except mysql.connector.Error as e:
    print("连接数据库失败！",str(e))

cursor = db.cursor(buffered=True)
try:
    sql_insert = "insert into test (name, url) values (%s, %s)"
    data = [
        ("xiao","url1"),
        ("xian","url2"),
        ("rourou","url3"),
        ("juju","url4"),
    ]
    cursor.executemany(sql_insert,data)
    db.commit()

except mysql.connector.Error as e:
    print("插入失败！", str(e))

finally:
    cursor.close()
    db.close()
