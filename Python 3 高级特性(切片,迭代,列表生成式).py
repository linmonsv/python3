#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import Iterable

L = []
n = 1
while n <= 100:
    L.append(n)
    n = n + 1
print(L)
#前10个数，每两个取一个
print(L[:10:2])

L = ["Michael", "Sarah", "Tracy", "Bob", "Jack"]
print(L[0 : 3])
print(L[  : 3])
print(L[1 : 3])
print(L[-2:  ])
print(L[-2 : -1])

print("ABCDEFG"[ : 3])
print("ABCDEFG"[::2])

d = {'a':1, 'b':2, 'c':3}
for key in d:
    print(key)
for value in d.values():
    print(value)
for key, val in d.items():
    print(key, val)

for ch in "ABC":
    print(ch)
#如何判断一个对象是可迭代对象呢？方法是通过collections模块的Iterable类型判断
print(isinstance("abc", Iterable))
print(isinstance([1,2,3], Iterable))
print(isinstance(123, Iterable))

#如果要对list实现类似Java那样的下标循环怎么办
#Python内置的enumerate函数可以把一个list变成索引-元素对
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)

#列表生成式即List Comprehensions，是Python内置的非常简单却强大的可以用来创建list的生成式
print(list(range(1, 11)))

L = []
for x in range(1, 11):
    L.append(x * x)
print(L)

L = [x * x for x in range(1, 11)]
print(L)

L = [x * x for x in range(1, 11) if x % 2 == 0]
print(L)

L = [m + n for m in "ABC" for n in "XYZ"]
print(L)

import os
L = [d for d in os.listdir(".")]
print(L)

d = {'x':'A', 'y':'B', 'z':'C'}
for k, v in d.items():
    print(k, '=', v)
L = [k + '=' + v for k, v in d.items()]
print(L)

L = ["Hello", "World", "IBM", "Apple"]
print([s.lower() for s in L])

L1 = ["Hello", "World", 18, "Apple", None]
L2 = [s.lower() for s in L1 if isinstance(s, str)]
print(L2)

