#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'hina'

from enum import Enum, unique

Month = Enum("Month", ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"))
print(Month.Jan.value)
# value属性则是自动赋给成员的int常量，默认从1开始计数
for name, member in Month.__members__.items():
    print(name, "=>", member, ",", member.value)

# 如果需要更精确地控制枚举类型，可以从Enum派生出自定义类
@unique
#@unique装饰器可以帮助我们检查保证没有重复值
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

day1 = Weekday.Mon
print(day1)
print(Weekday.Tue)
print(Weekday["Tue"])
print(Weekday.Tue.value)
print(day1 == Weekday.Mon)
print(day1 == Weekday.Tue)
print(Weekday(1))
print(day1 == Weekday(1))
print(Weekday(7))
