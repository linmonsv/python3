#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'hina'

def foo(s):
    n = int(s)
    # 凡是用print()来辅助查看的地方，都可以用断言（assert）来替代
    assert n != 0, "n is zero!"
    return 10 / n

def main():
    foo("0")

#main()

# 启动Python解释器时可以用-O参数来关闭assert

import logging

# 这就是logging的好处，它允许你指定记录信息的级别，
# 有debug，info，warning，error等几个级别，
# 当我们指定level=INFO时，logging.debug就不起作用了。
# 同理，指定level=WARNING后，debug和info就不起作用了。
# 这样一来，你可以放心地输出不同级别的信息，也不用删除，
# 最后统一控制输出哪个级别的信息。
logging.basicConfig(level = logging.INFO)

s = "0"
n = int(s)
logging.info("n = %d" % n)
print(10 / n)
