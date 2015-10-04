#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'hina'

# 我们来编写一个Dict类，这个类的行为和dict一致，但是可以通过属性来访问
class Dict(dict):
    def __init__(self, **kw):
        super().__init__(self, **kw)
    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)
    def __setattr__(self, key, value):
        self[key] = value
