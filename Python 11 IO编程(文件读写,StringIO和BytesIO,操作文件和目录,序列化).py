#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'hina'

try:
    f = open("test.txt")
    print(f.read())
finally:
    if f:
        f.close()
# 但是每次都这么写实在太繁琐，所以，Python引入了with语句来自动帮我们调用close()方法
with open("test.txt", "r") as f:
    print(f.read())

# 调用read()会一次性读取文件的全部内容
# 调用read(size)方法，每次最多读取size个字节的内容
# 调用readline()可以每次读取一行内容
# 调用readlines()一次读取所有内容并按行返回list

# 如果文件很小，read()一次性读取最方便；
# 如果不能确定文件大小，反复调用read(size)比较保险；
# 如果是配置文件，调用readlines()最方便

# 读取二进制文件
with open("test.txt", "rb") as f:
    print(f.read())

# 字符编码
with open("test.txt", "r", encoding = "gbk") as f:
    print(f.read())

# 写文件
with open("test.txt", "w") as f:
    f.write("Hello, World!")

# 在Python中，文件读写是通过open()函数打开的文件对象完成的。
# 使用with语句操作文件IO是个好习惯。

# StringIO顾名思义就是在内存中读写str。
from io import StringIO
f = StringIO("Hello!\nHi\nGoodbye!")
while True:
    s = f.readline()
    if s == "":
        break
    print(s.strip())

# StringIO操作的只能是str，如果要操作二进制数据，就需要使用BytesIO。
from io import BytesIO
f = BytesIO()
f.write("中文".encode("utf-8"))
print(f.getvalue())

f = BytesIO(b"\xe4\xb8\xad\xe6\x96\x87")
print(f.read())

import os
# 如果是posix，说明系统是Linux、Unix或Mac OS X，
# 如果是nt，就是Windows系统。
print(os.name)
# 注意uname()函数在Windows上不提供，也就是说，os模块的某些函数是跟操作系统相关的
#print(os.uname())
# 在操作系统中定义的环境变量，全部保存在os.environ这个变量
#print(os.environ())
# 要获取某个环境变量的值，可以调用os.environ.get('key')：

print(os.path.abspath("."))

# 把两个路径合成一个时，不要直接拼字符串，而要通过os.path.join()函数，
# 这样可以正确处理不同操作系统的路径分隔符
print(os.path.join(r"C:\Users\hina\PycharmProjects\untitled", "testdir"))
os.mkdir(r"C:\Users\hina\PycharmProjects\untitled\testdir")
os.rmdir(r"C:\Users\hina\PycharmProjects\untitled\testdir")

# 同样的道理，要拆分路径时，也不要直接去拆字符串，而要通过os.path.split()函数
print(os.path.split(r"C:\Users\hina\PycharmProjects\untitled"))
print(os.path.split(r"C:\Users\hina\PycharmProjects\untitled\test.py"))
print(os.path.splitext(r"C:\Users\hina\PycharmProjects\untitled\test.py"))

#os.rename('test.txt', 'test.py')
#os.remove('test.py')

# 但是复制文件的函数居然在os模块中不存在！原因是复制文件并非由操作系统提供的系统调用

# 幸运的是shutil模块提供了copyfile()的函数

print([x for x in os.listdir(".") if os.path.isdir(x)])

print([x for x in os.listdir(".") if os.path.isfile(x)])

print([x for x in os.listdir(".") if os.path.isfile(x) and os.path.splitext(x)[1] == ".py"])

# Python的os模块封装了操作系统的目录和文件操作，要注意这些函数有的在os模块中，有的在os.path模块中。

# 我们把变量从内存中变成可存储或传输的过程称之为序列化
import pickle
d = dict(name = "Bob", age = 20, score = 88)
# pickle.dumps()方法把任意对象序列化成一个bytes，然后，就可以把这个bytes写入文件。
print(pickle.dumps(d))
# 或者用另一个方法pickle.dump()直接把对象序列化后写入一个file-like Object：
f = open("dump.txt", "wb")
pickle.dump(d, f)
f.close()

f = open("dump.txt", "rb")
d2 = pickle.load(f)
f.close()
print(d2)

# Pickle的问题和所有其他编程语言特有的序列化问题一样，就是它只能用于Python，
# 并且可能不同版本的Python彼此都不兼容，
# 因此，只能用Pickle保存那些不重要的数据，不能成功地反序列化也没关系。

import json
d = dict(name = "Bob", age = 20, score = 88)
print(json.dumps(d))

json_str = '{"age": 20, "name": "Bob", "score": 88}'
print(json.loads(json_str))
# JSON标准规定JSON编码是UTF-8

class Student(object):
    def __init__(self, name ,age, score):
        self.name = name
        self.age = age
        self.score = score
s = Student("Bob", 20, 88)
#print(json.dumps(s))
print("--------------------------------------------")
def student2dict(std):
    return {
        "name" : std.name,
        "age" : std.age,
        "score" : std.score
    }

print(json.dumps(s, default = student2dict))
# 因为通常class的实例都有一个__dict__属性，它就是一个dict，用来存储实例变量。
# 也有少数例外，比如定义了__slots__的class。
print(json.dumps(s, default = lambda obj : obj.__dict__))

def dict2student(d):
    return Student(d["name"], d["age"], d["score"])
# 打印出的是反序列化的Student实例对象
print(json.loads(json_str, object_hook = dict2student))

"""
import re

if re.match(r"^-?[0-9]\d*$", "-1"):
    print("ok")
else:
    print("err")
if re.match(r"^-?[0-9]\d*$", "3"):
    print("ok")
else:
    print("err")
if re.match(r"^-?[0-9]\d*$", "a"):
    print("ok")
else:
    print("err")
"""

"""
str = input("--Enter the number---\n")
if not str.isdigit():
    print("this is a string")
elif str.isdigit():
    num = int(str)
    if num < 3:
        print("woker")
    elif num > 3:
        print("boss")
    else:
        print("luenjia")
"""