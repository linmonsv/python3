#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'hina'

import mysql.connector

conn = mysql.connector.connect(user = "root", password = "57235742", database = "test")
cursor = conn.cursor()
cursor.execute("create table user (id varchar(20) primary key, name varchar(20))")
cursor.execute("insert into user (id, name) values (%s, %s)", ["1", "Michael"])
print(cursor.rowcount)
conn.commit()
cursor.close()
cursor = conn.cursor()
cursor.execute("select * from user where id = %s", ["1"])
values = cursor.fetchall()
print(values)
cursor.close()
conn.close()

# 执行INSERT等操作后要调用commit()提交事务；
#  MySQL的SQL占位符是%s。
