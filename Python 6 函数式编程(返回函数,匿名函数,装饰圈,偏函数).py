#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回
def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax

def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

f = lazy_sum(1, 3, 5, 7, 9)
print(f)
print(f())

f1 = lazy_sum(1, 3, 5, 7, 9)
f2 = lazy_sum(1, 3, 5, 7, 9)
print(f1 == f2)

#当一个函数返回了一个函数后，其内部的局部变量还被新函数引用

def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i
        fs.append(f)#
    return fs

f1, f2, f3 = count()
print(f1())
print(f2())
print(f3())

#返回闭包时牢记的一点就是：返回函数不要引用任何循环变量，或者后续会发生变化的变量。

#如果一定要引用循环变量怎么办？方法是再创建一个函数，
#用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，已绑定到函数参数的值不变：

def count():
    def f(j):
        def g():
            return j * j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i))#f(i)立刻被执行，因此i的当前值被传入f()
    return fs
#缺点是代码较长，可利用lambda函数缩短代码
f1, f2, f3 = count()
print(f1())
print(f2())
print(f3())

#匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果
print(list(map(lambda x : x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])))

#匿名函数也是一个函数对象，也可以把匿名函数赋值给一个变量，再利用变量来调用该函数
f = lambda x : x * x
print(f(5))

def build(x, y):
    return lambda : x * x + y * y
print(build(1, 2)())

#通过变量也能调用该函数
def now():
    print("2015-3-25")
f = now
f()
#函数对象有一个__name__属性，可以拿到函数的名字
print(now.__name__)
print(f.__name__)

#在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）
def log(func):
    def wrapper(*args, **kw):
        print("call %s():" % func.__name__)
        return func(*args, **kw)
    return wrapper
#Python的@语法，把decorator置于函数的定义处
@log
def now2():
    print("2015-3-25")
now2()

#如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数
def log3(text):
    def decorator3(func):
        def wrapper3(*args, **kw):
            print("%s %s():" % (text, func.__name__))
            return func(*args, **kw)
        return wrapper3
    return decorator3
@log3("execute")
def now3():
    print("2015-3-25")
now3()
print(now3.__name__)
#需要把原始函数的__name__等属性复制到wrapper()函数中，
#否则，有些依赖函数签名的代码执行就会出错。
import functools

def log22(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print("call %s():" % func.__name__)
        return func(*args, **kw)
    return wrapper
@log22
def now22():
    print("2015-3-25")
now22()
print(now22.__name__)
print("---------------------------------")
def log33(text):
    def decorator33(func):
        #不需要编写wrapper.__name__ = func.__name__这样的代码
        #Python内置的functools.wraps就是干这个事的
        @functools.wraps(func)        
        def wrapper33(*args, **kw):
            print("%s %s():" % (text, func.__name__))
            return func(*args, **kw)
        return wrapper33
    return decorator33
@log33("execute")
def now33():
    print("2015-3-25")
now33()
print(now33.__name__)

print("---------------------------------")
def logf(text=None):
    def decoratorf(func):
        @functools.wraps(func)
        def wrapperf(*args, **kw):
            print("begin call")            
            func(*args, **kw)
            print("end call")
        return wrapperf
    return decoratorf

@logf()
def f():
    print("f")
f()
@logf("execute")
def f2():
    print("f2")
f2()

#通过设定参数的默认值，可以降低函数调用的难度。而偏函数也可以做到这一点
print(int("12345"))
print(int("12345", base = 8))
print(int("12345", base = 16))

def int2(x, base = 2):
    return int(x, base)
print(int2("10000000"))
print(int2("1010101"))

#functools.partial就是帮助我们创建一个偏函数的
int3 = functools.partial(int, base = 2)
print(int3("10000000"))
print(int3("1010101"))

#简单总结functools.partial的作用就是，
#把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，
#调用这个新函数会更简单











