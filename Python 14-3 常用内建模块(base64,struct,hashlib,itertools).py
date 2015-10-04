#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'hina'

# Base64是一种用64个字符来表示任意二进制数据的方法
import base64
print(base64.b64encode(b"binary\x00string"))
print(base64.b64decode(b"YmluYXJ5AHN0cmluZw=="))

# 由于标准的Base64编码后可能出现字符+和/，在URL中就不能直接作为参数，
# 所以又有一种"url safe"的base64编码，其实就是把字符+和/分别变成-和_：
print(base64.b64encode(b'i\xb7\x1d\xfb\xef\xff'))
print(base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff'))
print(base64.urlsafe_b64decode('abcd--__'))

# 由于=字符也可能出现在Base64编码中，但=用在URL、Cookie里面会造成歧义，所以，很多Base64编码后会把=去掉

# Base64是一种任意二进制到文本字符串的编码方法，常用于在URL、Cookie、网页中传输少量二进制数据。

def safe_base64_decode(s):
    a = (-len(s)) % 4
    if isinstance(s, str):
        s = s + "=" * a
        return base64.b64decode(s.encode("utf-8"))
    else:
        s = s + b"=" * a
        return base64.b64decode(s)

assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA')
print('Pass')

# struct模块来解决bytes和其他二进制数据类型的转换
import struct
# >表示字节顺序是big-endian，也就是网络序，I表示4字节无符号整数
print(struct.pack(">I", 10240099))
# 后面的bytes依次变为  I：4字节无符号整数和  H：2字节无符号整数
print(struct.unpack(">IH", b"\xf0\xf0\xf0\xf0\x80\x80"))

# 所以，尽管Python不适合编写底层操作字节流的代码，但在对性能要求不高的地方，利用struct就方便多了。

s = b'\x42\x4d\x38\x8c\x0a\x00\x00\x00\x00\x00\x36\x00\x00\x00\x28\x00\x00\x00\x80\x02\x00\x00\x68\x01\x00\x00\x01\x00\x18\x00'
print(struct.unpack("<ccIIIIIIHH", s))
"""
BMP格式采用小端方式存储数据，文件头的结构按顺序如下：

两个字节：'BM'表示Windows位图，'BA'表示OS/2位图；
一个4字节整数：表示位图大小；
一个4字节整数：保留位，始终为0；
一个4字节整数：实际图像的偏移量；
一个4字节整数：Header的字节数；
一个4字节整数：图像宽度；
一个4字节整数：图像高度；
一个2字节整数：始终为1；
一个2字节整数：颜色数。
"""
# (b'B', b'M', 691256, 0, 54, 40, 640, 360, 1, 24)
# b'B'、b'M'说明是Windows位图，位图大小为640x360，颜色数为24。

import hashlib

# MD5是最常见的摘要算法，速度很快，生成结果是固定的128 bit字节，通常用一个32位的16进制字符串表示。
md5 = hashlib.md5()
md5.update("how to use md5 in python hashlib?".encode("utf-8"))
print(md5.hexdigest())

md5 = hashlib.md5()
md5.update("how to use md5 in ".encode("utf-8"))
md5.update("python hashlib?".encode("utf-8"))
print(md5.hexdigest())

# SHA1的结果是160 bit字节，通常用一个40位的16进制字符串表示
sha1 = hashlib.sha1()
sha1.update("how to use sha1 in ".encode("utf-8"))
sha1.update("python hashlib?".encode("utf-8"))
print(sha1.hexdigest())

# 比SHA1更安全的算法是SHA256和SHA512，不过越安全的算法不仅越慢，而且摘要长度更长

# 由于常用口令的MD5值很容易被计算出来，
# 所以，要确保存储的用户口令不是那些已经被计算出来的常用口令的MD5，
# 这一方法通过对原始口令加一个复杂字符串来实现，俗称“加盐”

import itertools
"""
# 创建一个无限的迭代器，所以上述代码会打印出自然数序列，根本停不下来
natuals = itertools.count(1)
for n in natuals:
    print(n)
"""
"""
# cycle()会把传入的一个序列无限重复下去
cs = itertools.cycle("ABC")
for c in cs:
    print(c)
"""
# repeat()负责把一个元素无限重复下去，不过如果提供第二个参数就可以限定重复次数
ns = itertools.repeat('A', 3)
for n in ns:
    print(n)

# 无限序列只有在for迭代时才会无限地迭代下去，
# 如果只是创建了一个迭代对象，它不会事先把无限个元素生成出来，
# 事实上也不可能在内存中创建无限多个元素

# 无限序列虽然可以无限迭代下去，
# 但是通常我们会通过takewhile()等函数根据条件判断来截取出一个有限的序列：
natuals = itertools.count(1)
ns = itertools.takewhile(lambda x : x <= 10, natuals)
print(list(ns))

# chain()可以把一组迭代对象串联起来，形成一个更大的迭代器
for c in itertools.chain("ABC", "XYZ"):
    print(c)

# groupby()把迭代器中相邻的重复元素挑出来放在一起
for key, group in itertools.groupby("AAABBBCCAAA"):
    print(key, list(group))

for key, group in itertools.groupby("AaaBBbcCAAa"):
    print(key, list(group))

for key, group in itertools.groupby("AaaBBbcCAAa", lambda c:c.upper()):
    print(key, list(group))

# itertools模块提供的全部是处理迭代功能的函数，
# 它们的返回值不是list，而是Iterator，只有用for循环迭代的时候才真正计算
