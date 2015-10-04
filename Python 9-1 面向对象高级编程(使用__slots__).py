__author__ = 'hina'


# -*- coding: utf-8 -*-

class Student(object):
    pass


s = Student()
# 给实例绑定一个属性
s.name = "Michael"
print(s.name)


def set_age(self, age):
    self.age = age


from types import MethodType
# 给实例绑定一个方法
s.set_age = MethodType(set_age, s)
s.set_age(25)
print(s.age)

s2 = Student()


# 给一个实例绑定的方法，对另一个实例是不起作用的
# s2.set_age(25)

def set_score(self, score):
    self.score = score


# 为了给所有实例都绑定方法，可以给class绑定方法
Student.set_score = MethodType(set_score, Student)

# 给class绑定方法后，所有实例均可调用
s.set_score(100)
print(s.score)

s2.set_score(99)
print(s2.score)


# 通常情况下，上面的set_score方法可以直接定义在class中，
# 但动态绑定允许我们在程序运行的过程中动态给class加上功能，这在静态语言中很难实现

# 如果我们想要限制实例的属性怎么办？比如，只允许对Student实例添加name和age属性

# 为了达到限制的目的，Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性

class Student2(object):
    __slots__ = ("name", "age")  # 用tuple定义允许绑定的属性名称


s22 = Student2()
s22.name = "Michael"
s22.age = 25


# s22.score = 99 这句会挂掉，因为有限制了

# 使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的

class GraduateStudent2(Student):
    pass


g = GraduateStudent2()
g.score = 99
# 除非在子类中也定义__slots__，这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__
