#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'hina'

try:
    print("try...")
    r = 10 / 2
    #r = 10 / 0
    #r = 10 / int('a')
    print("result:", r)
except ValueError as e:
    print("ValueError:", e)
except ZeroDivisionError as e:
    print("ZeroDivisionError:", e)
else:
    print("no error!")
finally:#一定会被执行
    print("finally...")
print("END")

# Python的错误其实也是class，所有的错误类型都继承自BaseException，
# 所以在使用except时需要注意的是，它不但捕获该类型的错误，还把其子类也“一网打尽”

def foo(s):
    return 10 / int(s)

try:
    foo('a')
except ValueError as e:
    print("ValueError")
# 第二个except永远也捕获不到UnicodeError，因为UnicodeError是ValueError的子类，如果有，也被第一个except给捕获了
except UnicodeError as e:
    print("UnicodeError")

def bar(s):
    return foo(s) * 2

# 使用try...except捕获错误还有一个巨大的好处，就是可以跨越多层调用
def main():
    try:
        bar("a")
    except Exception as e:
        print("Error:", e)
    finally:
        print("finally...")

main()

print("-----------------------------------------------main2")
# 如果错误没有被捕获，它就会一直往上抛，最后被Python解释器捕获，打印一个错误信息，然后程序退出
def main2():
    bar("0")

#main2()

# 记录错误
import logging
try:
    r = 10 / 0
except Exception as e:
    logging.exception(e)# 通过配置，logging还可以把错误记录到日志文件里，方便事后排查
print("END")

class FooError(ValueError):
    pass
def foo2(s):
    n = int(s)
    if n == 0:
        # 执行，可以最后跟踪到我们自己定义的错误
        raise FooError("invalid value: %s" % s)
    return 10 / n
#foo2("0")

# 只有在必要的时候才定义我们自己的错误类型
# 如果可以选择Python已有的内置的错误类型（比如ValueError，TypeError），
# 尽量使用Python内置的错误类型。

def foo3(s):
    n = int(s)
    if n == 0:
        raise ValueError("invalid value: %s" % s)
    return 10 / n
def bar():
    try:
        foo3("0")
    except ValueError as e:
        print("ValueError!")
        # raise语句如果不带参数，就会把当前错误原样抛出
        raise
#bar()

try:
    10 / 0
except ZeroDivisionError:
    # 在except中raise一个Error，还可以把一种类型的错误转化成另一种类型
    raise ValueError("input error2!")
