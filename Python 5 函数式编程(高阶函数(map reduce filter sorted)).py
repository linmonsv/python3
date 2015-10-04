#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#变量可以指向函数
f = abs
print(f(-10))

#函数名也是变量
abs = 10
print(abs)
abs = f
print(abs(-10))

#一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数
def add(x, y, f):
    return f(x) + f(y)
x = -7
y = 6
f = abs
print(add(x, y, f))

#map()函数接收两个参数，一个是函数，一个是Iterable，
#map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回
def f(x):
    return x * x
r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(list(r))

print(list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])))

#reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，
#这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
from functools import reduce
def add(x, y):
    return x + y
print(reduce(add, [1, 3, 5, 7, 9]))

def str2int(s):
    def fn(x, y):
        return x * 10 + y
    #print(reduce(fn, [1, 3, 5, 7, 9]))
    def char2num(s):
        return {"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9}[s]
    return reduce(fn, map(char2num, s))
print(str2int("12345"))

def str2int_2(s):
    def char2num(s):
        return {"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9}[s]
    return reduce(lambda x, y : x * 10 + y, map(char2num, s))
print(str2int_2("12345"))

def normalize(name):
    return name.capitalize()
L1 = ["adam", "LISA", "barT"]
L2 = list(map(normalize, L1))
print(L2)

def prod(L):
    return reduce(lambda x, y : x * y, L)
print("3 * 5 * 7 * 9 = ", prod([3, 5, 7, 9]))

def str2float(s):
    def fn(x, y):
        return x * 10 + y
    str1, str2 = s.split(".")
    return reduce(fn, map(int, str1)) + reduce(fn, map(int, str2)) / 10 ** len(str2)
    pass
print("str2float(\"123.456\") = ", str2float("123.456"))

#和map()类似，filter()也接收一个函数和一个序列。
#和map()不同的时，filter()把传入的函数依次作用于每个元素，
#然后根据返回值是True还是False决定保留还是丢弃该元素。
def is_odd(n):
    return n % 2 == 1
print(list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])))

def not_empty(s):
    return s and s.strip()
#strip
#删除s字符串中开头、结尾处，位于 rm删除序列的字符;
#当rm为空时，默认删除空白符（包括'\n', '\r',  '\t',  ' ')
print(list(filter(not_empty, ['A', '', 'B', None, 'C', ' '])))

def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n
def _not_divisible(n):
    return lambda x : x % n > 0
def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)
for n in primes():
    if n < 100:
        print(n)
    else:
        break
print("is_palindrome filter test start")

def is_palindrome(n):
    s = str(n)
    sL = s[ : int((len(s)) / 2)]
    sR = s[int((len(s) + 1) / 2) : ]
    list(sR).reverse()
    return (list(sL)) == (list(sR))
output = filter(is_palindrome, range(1, 1000))
print(list(output))

def is_palindrome2(n):
    return str(n) == str(n)[ : : -1]
output = filter(is_palindrome2, range(1, 1000))
print(list(output))

#Python内置的sorted()函数就可以对list进行排序
print(sorted([36, 5, -12, 9, -21]))
print(sorted([36, 5, -12, 9, -21], key = abs))
print(sorted([36, 5, -12, 9, -21], key = abs, reverse = True))
print(sorted(["bob", "about", "Zoo", "Credit"]))
print(sorted(["bob", "about", "Zoo", "Credit"], key = str.lower))#都转化成小写排序

#sorted()排序的关键在于实现一个映射函数。
L = [("Bob", 75), ("Adm", 92), ("Bart", 66), ("Lisa", 88)]
def by_name(t):
    key, value = t[0], t[1]
    return key.lower()
def by_score(t):
    return t[1]
L2 = sorted(L, key = by_name)
print(L2)
L2 = sorted(L, key = by_score, reverse = True)
print(L2)




















