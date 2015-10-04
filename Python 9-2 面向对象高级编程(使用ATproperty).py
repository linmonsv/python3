#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'hina'

class Student(object):
    def get_score(self):
        return self._score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError("score must be an integer!")
        if value < 0 or value > 100:
            raise ValueError("score must between 0 ~ 100:")
        self._score = value


s = Student()
s.set_score(60)
print(s.get_score())


# s.set_score(9999)

class Student2(object):
    # Python内置的@property装饰器就是负责把一个方法变成属性调用的
    @property
    def score(self):
        return self._score

    # 另一个装饰器@score.setter，负责把一个setter方法变成属性赋值
    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError("score must be an integer!")
        if value < 0 or value > 100:
            raise ValueError("score must between 0 ~ 100:")
        self._score = value

    # 还可以定义只读属性，只定义getter方法，不定义setter方法就是一个只读属性
    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2015 - self._birth


s2 = Student2()
s2.score = 60
print(s2.score)
# s2.score = 9999

s2.birth = 1999
print(s2.age)

#@property广泛应用在类的定义中，可以让调用者写出简短的代码，
# 同时保证对参数进行必要的检查，这样，程序运行时就减少了出错的可能性
