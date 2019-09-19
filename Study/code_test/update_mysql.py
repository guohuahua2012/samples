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
    sql_update = "update test set url = 'http://www.baidu.com' where name='juju'"
    cursor.execute(sql_update)
    db.commit()
except mysql.connector.Error as e:
    print("修改数据失败！",str(e))

finally:
    cursor.close()
    db.close()