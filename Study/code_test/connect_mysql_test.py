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




