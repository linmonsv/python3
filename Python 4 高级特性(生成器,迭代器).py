#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#如果列表元素可以按照某种算法推算出来，
#那我们是否可以在循环的过程中不断推算出后续的元素呢？
#这样就不必创建完整的list，从而节省大量的空间。
#在Python中，这种一边循环一边计算的机制，称为生成器：generator

L = [x * x for x in range(10)]
print(L)

g = (x * x for x in range(10))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
for n in g:
    print(n)

#函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
#而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，
#再次执行时从上次返回的yield语句处继续执行
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        #print(b)
        yield b
        a, b = b, a + b
        n = n + 1
    return "done"

#print(fib(6))
def odd():
    print("step 1")
    yield 1
    print("step 2")
    yield 2
    print("step 3")
    yield 3
o = odd()
print(next(o))
print(next(o))
print(next(o))

for n in fib(6):
    print(n)

g = fib(6)
while True:
    try:
        x = next(g)
        print("g:", x)
    except StopIteration as e:#拿到返回值
        print("Generator return value:", e.value)
        break

def triangles():
    i = 0
    L = [1]
    while True:
        yield L
        L.append(0)
        L = [L[i] + L[i - 1] for i in range(len(L))]
    return "done"

n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break

#可以使用isinstance()判断一个对象是否是Iterable对象
from collections import Iterable
print(isinstance([], Iterable))

#集合数据类型如list、dict、str等是Iterable但不是Iterator，
#不过可以通过iter()函数获得一个Iterator对象

for x in [1, 2, 3, 4, 5]:
    print(x)

it = iter([1, 2, 3, 4, 5])
while True:
    try:
        x = next(it)
    except StopIteraation:
        break


























