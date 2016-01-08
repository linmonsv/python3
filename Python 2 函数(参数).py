#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

print(abs(100))
print(abs(-100))
print(max(1, 2))
print(max(2, 3, 1, -5))
print(int("123"))
print(int(12.34))
print(str("1.23"))
print(str(100))
print(bool(1))
print(bool(""))
n1 = 255
n2 = 1000
print(str(n1))
print(str(hex(n1)))
print(str(hex(n2)))

#位置参数
def my_abs(x):
    #数据类型检查可以用内置函数
    if not isinstance(x, (int, float)):
        raise TypeError("bad operand tyep")
    if x >= 0:
        return x
    else:
        return -x

print(my_abs(100))
print(my_abs(-100))
#Python解释器会自动检查出来
#解释器就无法帮我们检查
#print(my_abs('A'))

def move(x, y, step, angle = 0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

x, y = move(100, 100, 60, math.pi / 6)
print(x, y)

r = move(100, 100, 60, math.pi / 6)
print(r)

def quadratic(a, b, c):
    x1 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    x2 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    return x1, x2

print(quadratic(2, 3, 1))
print(quadratic(1, 3, -4))

#默认参数
def power(x, n = 2):
    return x ** n

print(power(5))
print(power(5, 2))
print(power(5, 3))

#定义默认参数要牢记一点：默认参数必须指向不变对象
def add_end(L = []):
    L.append("END")
    return L

def add_end2(L = None):
    if L is None:
        L = []
    L.append("END")
    return L

print(add_end([1, 2, 3]))
print(add_end(['x', 'y', 'z']))
print(add_end())
#Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，
#因为默认参数L也是一个变量，它指向对象[]，每次调用该函数，如果改变了L的内容，
#则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。
print(add_end())

print(add_end2())
print(add_end2())

#可变参数
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
print(calc(1, 2))
print(calc())
print(calc(1, 2, 3))

nums = [1, 2, 3]
print(calc(nums[0], nums[1], nums[2]))
#一个*号，把list或tuple的元素变成可变参数传进去
print(calc(*nums))

#关键字参数
def person(name, age, **kw):
    if "city" in kw:
        pass
    if "job" in kw:
        pass
    
    print("name:", name, "age:", age, "other", kw)

person("Michael", 30)
person("Bob", 35, city="Beijing")
person("Adam", 45, gender='M', job="Engineer")

extra = {"city":"Beijing", "job":"Engineer"}
person("Jack", 24, city=extra["city"], job=extra["job"])
person("Jack", 24, **extra)
#注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra。

#命名关键字参数
def person2(name, age, *, city = "Beijing", job):
    print(name, age, city, job)

person2("Jack", 24, city="Beijing", job="Engineer")
person2("Jack", 24, job = "Engineer")

def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)
print(fact(1))
print(fact(5))
print(fact(100))
#解决递归调用栈溢出的方法是通过尾递归优化
def fact2(n):
    return fact2_iter(n, 1)
def fact2_iter(num, product):
    if num == 1:
        return product
    return fact2_iter(num - 1, num * product)
print(fact2(100))
#尾递归调用时，如果做了优化，栈不会增长，因此，无论多少次调用也不会导致栈溢出。
#遗憾的是，大多数编程语言没有针对尾递归做优化，
#Python解释器也没有做优化，所以，即使把上面的fact(n)函数改成尾递归方式，也会导致栈溢出
#所以还是我自己写个吧，哇咔咔
def fact3(n):
    result = 1
    for i in range(n):
        result = result * (i + 1)
    return result
print(fact3(100))
#print(fact3(1000))

#n个盘子从a通过b移到c
def move(n, a, b, c):
    if n == 1:
        print("move", a, "--->", c)
        return
    move(n - 1, a, c, b)
    move(1, a, b, c)
    move(n - 1, b, a, c)

move(3, 'A', 'B', 'C')

def add(a):
    a = a + 1
    return a
aaa = 3
bbb = add(aaa)
print(aaa, bbb)




