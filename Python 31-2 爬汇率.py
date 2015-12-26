#encoding:UTF-8
import urllib.request
import re
import os
import sqlite3
from datetime import *
import time

main_page = "http://www.icbc.com.cn/ICBCDynamicSite/Optimize/Quotation/ForeignExchangeNew.aspx"
data_html = urllib.request.urlopen(main_page).read().decode("utf-8")

reg = re.compile(r'<span id="lbData"><tr><td>美元</td><td><span>(.+?)</span></td><td><span>(.+?)</span></td></tr><tr><td>欧元</td><td><span>(.+?)</span></td><td><span>(.+?)</span></td></tr><tr><td>日元</td><td><span>(.+?)</span></td><td><span>(.+?)</span></td></tr><tr><td>澳大利亚元</td><td><span>(.+?)</span></td><td><span>(.+?)</span></td></tr></span>')
table_rates = re.findall(reg, data_html)
rate = table_rates[0]

dt = datetime.now()
cur_data = dt.strftime('%Y%m%d')
cur_time = dt.strftime('%H%M%S')
print(dt.strftime('%Y-%m-%d %H:%M:%S %f') )
print("货币名称\t现汇买入价\t现钞买入价")
print("美元\t\t%s\t\t%s" % (rate[0], rate[1]))
print("欧元\t\t%s\t\t%s" % (rate[2], rate[3]))
print("日元\t\t%s\t\t%s" % (rate[4], rate[5]))
print("澳大利亚元\t%s\t\t%s" % (rate[6], rate[7]))

if os.path.exists(r'rate.db'):
    pass
else:
    conn = sqlite3.connect("rate.db")
    cursor = conn.cursor()
    cursor.execute('create table t_rate (id INTEGER PRIMARY KEY AUTOINCREMENT, \
                    cur_data varchar(20), cur_time varchar(20), \
                    us_spot varchar(20), us_oof varchar(20), \
                    eu_spot varchar(20), eu_oof varchar(20), \
                    jp_spot varchar(20), jp_oof varchar(20), \
                    au_spot varchar(20), au_oof varchar(20) \
                  )')
    cursor.close()
    conn.commit()
    conn.close()
conn = sqlite3.connect("rate.db")
cursor = conn.cursor()
cursor.execute('insert into t_rate (id, cur_data, cur_time, us_spot, us_oof, eu_spot , eu_oof , jp_spot , jp_oof , au_spot , au_oof  ) \
                values (NULL, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)' \
                % (cur_data, cur_time, rate[0], rate[1], rate[2], rate[3], rate[4], rate[5], rate[6], rate[7]))
cursor.close()
conn.commit()
conn.close()

conn = sqlite3.connect("rate.db")
cursor = conn.cursor()
cursor.execute('select * from t_rate')
values = cursor.fetchall()
print("\nID\t\t日期\t时间\t美汇\t美钞\t欧汇\t欧钞\t日汇\t日钞\t澳汇\t澳钞")
for item in values:
    for element in item:
        print(element, end="")
        print("\t", end="")
    print("")
cursor.close()
conn.close()
