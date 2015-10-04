#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#import time

print("Hello World!")
#print(time.ctime())
#print(2**1000000)
#print(time.ctime())

#print(234*2432)

#Python代码运行助手源码

print('The quick brown fox', 'jumps over', 'the lazy dog')

#name = input()
#name = input('please input your name:')
#print(name)

print('I realy like "python"!')

print("I\'m ok")
print("I'm ok")
print('I\'m learning\nPython')
print('\\\n\\')
print('\\\t\\')
print(r'\\\t\\')
print('''line1
line2
line3''')
print(r'''line1
line2
line3''')
print(True)
print(3 > 2)
print(True and False)
print(not True)

a = 'ABC'
b = a
a = 'XYZ'
print(b)

print(10/3)
print(9/3)
print(10//3)
print(10%3)

#Python的整数没有大小限制

print('包含中文的str')

print(ord('A'))
print(ord('中'))
print(chr(66))
print(chr(25991))

print('\u4e2d\u6587')

x = b'ABC'

print(b'ABC'.decode('ascii'))
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))

print(len('ABC'))
print(len('中文'))

print(len(b'ABC'))
print(len(b'\xe4\xb8\xad\xe6\x96\x87'))

print("Hello, %s" % "world")

print("Hi, %s, you have $%d" % ("Michael", 1000000))

print("%2d-%02d" % (3,1))

print("%.2f" %3.1415926)

print("Age: %s. Gender: %s" % (25, True))

print("growh rate: %d %%" % 7)

s1 = 72
s2 = 85
r = s2 * 100 / s1
print("growth rate : %s %%" % (r - 100))
print("growth rate : %f %%" % (r - 100))
print("growth rate : %.1f %%" % (r - 100))

classmates = ["Michael", "Bob", "Tracy"]
print(classmates)
print(len(classmates))
print(classmates[0])
print(classmates[-1])
classmates.insert(1, "Jack")
print(classmates)
classmates.pop()
print(classmates)
classmates.pop(1)
print(classmates)
classmates[1] = "Sarah"
print(classmates)

L = ["Apple", 123, True]
print(L)

s = ["python", "java", ["asp", "php"], "scheme"]
print(len(s))

print(s[2][1])

L = []
print(len(L))

#tuple一旦初始化就不能修改
classmates = ("Michael", "Bob", "Tracy")
print(classmates)

#只有1个元素的tuple定义时必须加一个逗号,，来消除歧义
t = (1,)
print(t)

#
t = ("a", "b", ["A", "B"])
print(t)
t[2][0] = "X"
t[2][1] = "Y"
print(t)

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
print(L[0][0])
print(L[1][1])
print(L[2][2])

height = 1.75
weight = 80.5
bmi = weight / (height ** 2)
if bmi < 18.5:
    print("过轻")
elif 18.5 <= bmi and bmi <25:
    print("正常")
elif 25 <= bmi and bmi <28:
    print("过重")
elif 28 <= bmi and bmi <32:
    print("肥胖")
else:
    print("严重肥胖")

names = ["Michael", "Bob", "Tracy"]
for name in names:
    print(name)

sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + x
print(sum)

print(list(range(5)))

sum = 0
for x in range(101):
    sum = sum + x
print(sum)

sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n- 2
print(sum)

L = ["Bart", "Lisa", "Adam"]
for l in L:
    print("Hello, %s!" % l)

d = {"Michael" : 95, "Bob" : 75, "Tracy" : 85}
print(d["Michael"])
d["Jack"] = 67
print(d["Jack"])

print("Toomas" in d)
print(d.get("Toomas"))
print(d.get("Toomas", -1))

d.pop("Bob")
print(d)

#要创建一个set，需要提供一个list作为输入集合
s = set([1, 2, 3])
print(s)
#重复元素在set中自动被过滤
s = set([1, 1, 2, 2, 3, 3])
print(s)
#可以重复添加，但不会有效果
s.add(4)
print(s)
s.add(4)
print(s)
s.remove(4)
print(s)
#set可以看成数学意义上的无序和无重复元素的集合

a = ['c', 'b', 'a']
print(a)
a.sort()
print(a)

a = "abc"
print(a.replace('a', 'A'))
print(a)


















