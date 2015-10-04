#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'hina'

from datetime import datetime
now = datetime.now()
print(now)
print(type(now))

dt = datetime(2015, 4, 19, 20, 20)
print(dt)

# 是一个浮点数。如果有小数位，小数位表示毫秒数
print(dt.timestamp())

t = 1429446000.0
print(datetime.fromtimestamp(t))
# 转换到UTC标准时区的时间
print(datetime.utcfromtimestamp(t))

cday = datetime.strptime("2015-6-1 18:19:59", "%Y-%m-%d %H:%M:%S")
print(cday)

print(now.strftime("%a, %b %d %H:%M"))

print("---------------------------------")

from datetime import datetime, timedelta
now = datetime.now()
print(now)
print(now + timedelta(hours = 10))
print(now - timedelta(days = 1))
print(now + timedelta(days = 2, hours = 12))

print("---------------------------------")

from datetime import datetime, timedelta, timezone
tz_utc_8 = timezone(timedelta(hours=8)) # 创建时区UTC+8:00
now = datetime.now()
print(now)
dt = now.replace(tzinfo=tz_utc_8) #  强制设置为UTC+8:00
print(dt)
# 如果系统时区恰好是UTC+8:00，那么上述代码就是正确的，否则，不能强制设置为UTC+8:00时区

import sys
print("----------------- Line No : %s --------------" % sys._getframe().f_lineno)

utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
print(utc_dt)

bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print(bj_dt)

tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt)
tokyo_dt2 = bj_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt2)

# 不是必须从UTC+0:00时区转换到其他时区，任何带时区的datetime都可以正确转换，
# 例如上述bj_dt到tokyo_dt的转换

# 如果要存储datetime，最佳方法是将其转换为timestamp再存储，因为timestamp的值与时区完全无关。

print("----------------- Line No : %s --------------" % sys._getframe().f_lineno)
import re
def to_timestamp(dt_str, tz_str):
    cday = datetime.strptime(dt_str, "%Y-%m-%d %H:%M:%S")
    tz_re = re.match(r"^UTC([+-]\d+)\:\d{2}$", tz_str)
    #print(tz_re)
    if tz_re:
        tz_hours = int(tz_re.group(1))
        result = cday.replace(tzinfo=timezone(timedelta(hours=tz_hours))).timestamp()
        #print(result)
        return result + 0

t1 = to_timestamp("2015-6-1 08:10:30", "UTC+7:00")
#print(t1)
assert t1 == 1433121030.0, t1
t2 = to_timestamp("2015-5-31 16:10:30", "UTC-09:00")
#print(t2)
assert t2 == 1433121030.0, t2
print("Pass")
