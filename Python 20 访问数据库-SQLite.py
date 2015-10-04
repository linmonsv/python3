#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'hina'

import os, sqlite3

db_file = os.path.join(os.path.dirname(__file__), 'test.db')
if os.path.isfile(db_file):
    os.remove(db_file)

conn = sqlite3.connect(db_file)

cursor = conn.cursor()
cursor.execute("create table user(id varchar(20) primary key, name varchar(2))")
cursor.execute("insert into user(id, name) values(\"1\", \"Michael\")")
print(cursor.rowcount)
cursor.close()
conn.commit()

conn.close()

conn = sqlite3.connect("test.db")
cursor = conn.cursor()
cursor.execute("select * from user where id=?", "1")
values = cursor.fetchall()
print(values)
cursor.close()
conn.close()

import os, sqlite3

db_file = os.path.join(os.path.dirname(__file__), 'test2.db')
if os.path.isfile(db_file):
    os.remove(db_file)

# 初始数据:
conn = sqlite3.connect(db_file)
cursor = conn.cursor()
cursor.execute('create table user(id varchar(20) primary key, name varchar(20), score int)')
cursor.execute(r"insert into user values ('A-001', 'Adam', 95)")
cursor.execute(r"insert into user values ('A-002', 'Bart', 62)")
cursor.execute(r"insert into user values ('A-003', 'Lisa', 78)")
cursor.close()
conn.commit()
conn.close()

def get_score_in(low, high):
    ' 返回指定分数区间的名字，按分数从低到高排序 '
    with sqlite3.connect(db_file) as conn:
        cursor = conn.cursor()
        cursor.execute("select name from user where score between %s and %s order by score" % (str(low), str(high)))
        values = cursor.fetchall()
        print(values)

        l = []
        for data in values:
            l.append(data[0])
        return l

        #return map(lambda x : x[0], values)

assert get_score_in(80, 95) == ['Adam'],get_score_in(80, 95)
assert get_score_in(60, 80) == ['Bart', 'Lisa'],get_score_in(60, 80)
assert get_score_in(60, 100) == ['Bart', 'Lisa', 'Adam'],get_score_in(60, 100)

print('Pass')
