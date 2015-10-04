#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'hina'

def abs(n):
    """
    Function to get absolute value of number.

    Exmple:

    >>>abs(1)
    1
    >>>abs(-1)
    1
    >>>abs(0)
    0
    """
    return n if n >= 0 else (-n)

class Dict(dict):
    """
    Simple dict but also support access as x.y style

    >>> d1 = Dict()
    >>> d1['x'] = 100
    >>> d1.x
    100
    >>> d1.y = 200
    >>> d1['y']
    200
    >>> d2 = Dict(a=1, b=2, c='3')
    >>> d2.c
    '3'
    >>> d2['empty']
    Traceback (most recent call last):
        ...
    KeyError: 'empty'
    >>> d2.empty
    Traceback (most recent call last):
        ...
    AttributeError: 'Dict' object has no attribute 'empty'
    """

    def __init__(self, **kw):
        super(Dict, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)
    def __setattr__(self, key, value):
        self[key] = value

# 注意到最后3行代码。当模块正常导入时，doctest不会被执行。
# 只有在命令行直接运行时，才执行doctest。
# 所以，不必担心doctest会在非测试环境下执行。

if __name__ == "__main__":
    import doctest
    doctest.testmod()
