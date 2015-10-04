#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'hina'

# \d可以匹配一个数字
# \w可以匹配一个字母或数字
# .可以匹配任意字符
# *表示任意个字符（包括0个）
# +表示至少一个字符
# 用?表示0个或1个字符
# {n}表示n个字符
# {n,m}表示n-m个字符
# \s可以匹配一个空格（也包括Tab等空白符）

# \d{3}\s+\d{3,8}
# \d{3}\-\d{3,8}

# []表示范围

# [0-9a-zA-Z\_]可以匹配一个数字、字母或者下划线
# [0-9a-zA-Z\_]+可以匹配至少由一个数字、字母或者下划线组成的字符串

# [a-zA-Z\_][0-9a-zA-Z\_]*可以匹配由字母或下划线开头，
# 后接任意个由一个数字、字母或者下划线组成的字符串，也就是Python合法的变量

# [a-zA-Z\_][0-9a-zA-Z\_]{0, 19}更精确地限制了变量的长度是1-20个字符
# （前面1个字符+后面最多19个字符）

# A|B可以匹配A或B
# 所以[P|p]ython可以匹配'Python'或者'python'

# ^表示行的开头，^\d表示必须以数字开头

# $表示行的结束，\d$表示必须以数字结束

import re

s = "ABC\\-001"
# 由于Python的字符串本身也用\转义，所以要特别注意
# 因此我们强烈建议使用Python的r前缀，就不用考虑转义的问题了
s = r"ABC\-001"

print(re.match(r"\d{3}\-\d{3,8}$", "010-12345"))
print(re.match(r"\d{3}\-\d{3,8}$", "010 12345"))
# match()方法判断是否匹配，如果匹配成功，返回一个Match对象，否则返回None

test = "010-12345"
if re.match(r"\d{3}\-\d{3,8}", test):
    print("ok")
else:
    print("failed")

# 切分字符串
print("a b   c".split(" "))
print(re.split(r"\s+", "a b   c"))
print(re.split(r"[\s\,]+", "a,b,    c  d"))
print(re.split(r"[\s\,\;]+", "a, b;;   c d"))

# 分组
m = re.match(r"(\d{3})-(\d{3,8})$", "010-12345")
print(m)
print(m.group(0))
print(m.group(1))
print(m.group(2))

# 如果正则表达式中定义了组，就可以在Match对象上用group()方法提取出子串来
t = "19:05:30"
m = re.match(r"(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$", t)
print(m.groups())

# 用正则还是识别不了，或者说写出来非常困难，这时就需要程序配合识别了。

# 正则匹配默认是贪婪匹配，也就是匹配尽可能多的字符
print(re.match(r"(\d+)(0*)$", "102300").groups())
# 由于\d+采用贪婪匹配，直接把后面的0全部匹配了，结果0*只能匹配空字符串了

# 必须让\d+采用非贪婪匹配（也就是尽可能少匹配），才能把后面的0匹配出来，加个?就可以让\d+采用非贪婪匹配
print(re.match(r"(\d+?)(0*)$", "102300").groups())

# 编译
re_telephone = re.compile(r"(\d{3})-(\d{3,8}$)")
print(re_telephone.match("010-12345").groups())
print(re_telephone.match("010-8086").groups())

print(re.match(r"[a-zA-Z\_][0-9a-zA-Z\_\.]*\@[a-zA-Z\_][0-9a-zA-Z\_]*\.[a-zA-Z\_][0-9a-zA-Z\_]*", "someone@gmail.com"))
print(re.match(r"[a-zA-Z\_][0-9a-zA-Z\_\.]*\@[a-zA-Z\_][0-9a-zA-Z\_]*\.[a-zA-Z\_][0-9a-zA-Z\_]*", "bill.gates@microsoft.com"))

m = re.match(r"(\<[a-zA-Z\s]*\>)\s([a-zA-Z\_][0-9a-zA-Z\_\.]*\@[a-zA-Z\_][0-9a-zA-Z\_]*\.[a-zA-Z\_][0-9a-zA-Z\_]*)$", "<Tom Paris> tom@voyager.org")
print(m)
print(m.group(0))
print(m.group(1))
print(m.group(2))
