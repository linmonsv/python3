#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'hina'


class Student(object):
    def __init__(self, name):
        self.name = name

    # __str__()返回用户看到的字符串
    def __str__(self):
        return "Student object (name : %s)" % self.name

    # __repr__()返回程序开发者看到的字符串，也就是说，__repr__()是为调试服务的
    __repr__ = __str__


print(Student("Michael"))
s = Student("Michael")
print(s)


# 如果一个类想被用于for ... in循环，
# 类似list或tuple那样，就必须实现一个__iter__()方法，该方法返回一个迭代对象

class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100000:
            raise StopIteration()
        return self.a

    # 要表现得像list那样按照下标取出元素，需要实现__getitem__()方法
    def __getitem__(self, n):
        if isinstance(n, int):  # n是索引
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):  # n是切片
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L


for n in Fib():
    print(n)

f = Fib()
print(f[0])
print(f[1])
print(f[2])
print(f[3])
print(f[10])
print(f[100])

print(f[0:5])


# 但是没有对step参数作处理
# 也没有对负数作处理
# 所以，要正确实现一个__getitem__()还是有很多工作要做的

# 如果把对象看成dict，__getitem__()的参数也可能是一个可以作key的object
# 与之对应的是__setitem__()方法，把对象视作list或dict来对集合赋值。最后，
# 还有一个__delitem__()方法，用于删除某个元素

# 当我们调用类的方法或属性时，如果不存在，就会报错
# 要避免这个错误，除了可以加上一个score属性外，Python还有另一个机制，那就是写一个__getattr__()方法，动态返回一个属性
class Student2(object):
    def __init__(self):
        self.name = "Michale"

    def __getattr__(self, attr):
        if attr == "score":
            return 99
        if attr == "age":
            return lambda: 25
        return AttributeError("\"Student\" object has no attribute \"%s\"" % attr)


s2 = Student2()
print(s2.name)
# 调用不存在的属性时，比如score，Python解释器会试图调用__getattr__(self, 'score')来尝试获得属性
print(s2.score)
print(s2.age())


class Chain(object):
    def __init__(self, path=""):
        self._path = path

    def __getattr__(self, path):
        return Chain("%s/%s" % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__


print(Chain().status.user.timeline.list)


# 一个对象实例可以有自己的属性和方法，当我们调用实例方法时，我们用instance.method()来调用

class Student3(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print("My name is %s:" % self.name)


s3 = Student3("Michael")
s3()

# __call__()还可以定义参数。对实例进行直接调用就好比对一个函数进行调用一样，
# 所以你完全可以把对象看成函数，把函数看成对象

#怎么判断一个变量是对象还是函数呢
print(callable(Student3()))
print(callable(max))
print(callable([1,2,3]))
print(callable(None))
print(callable("str"))

