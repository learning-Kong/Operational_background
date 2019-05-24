# -*- coding:utf-8 -*-
# author: "Jack Kong"
# 2019-05-24

import pymysql

config = {
    "host": "115.159.40.122",
    "user": "zabbix",
    "password": "zabbix",
    "database": "zabbix"
}

db = pymysql.connect(**config)

cursor = db.cursor()

cursor.execute("select * from history_uint where itemid=25367 limit 100")

data = cursor.fetchall()

print(data)

cursor.close()
db.close()

