#!/usr/bin/env python3
# -*- coding: utf-8 -*-

std1 = {"name" : "Michael", "score" : 98}
std2 = {"name" : "Bob", "score" : 81}

def print_score(std):
    print("%s : %s" % (std["name"], std["score"]))

print_score(std1)
print_score(std2)

class Student(object):
    #__init__方法的第一个参数永远是self，表示创建的实例本身
    def __init__(self, name, score):
        #在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private）
        self.__name = name
        self.score = score
        #在Python中，变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，是特殊变量，
        #特殊变量是可以直接访问的，不是private变量
    def print_score(self):
        print("%s : %s" % (self.__name, self.score))
    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'
    def get_name(self):
        return self.__name
    def get_score(self):
        return self.score
    def set_score(self, score):
        if 0 <= score <= 100:
            self.score = score
        else:
            return ValueError("bad score")

bart = Student("Bart Simpson", 59)
lisa = Student("Lisa Simpson", 87)
bart.print_score()
lisa.print_score()
print(bart.get_grade())
print(lisa.get_grade())

bart.name = "lalala"
bart.score = 90
bart.print_score()
lisa.print_score()
print(bart.get_grade())
print(lisa.get_grade())

#一个下划线开头的实例变量名
#“虽然我可以被访问，但是，请把我视为私有变量，不要随意访问”。

#双下划线开头的实例变量
#不能直接访问__name是因为Python解释器对外把__name变量改成了_Student__name，
#所以，仍然可以通过_Student__name来访问__name变量

#不同版本的Python解释器可能会把__name改成不同的变量名。

class Animal(object):
    def run(self):
        print("Animal is running...")
class Dog(Animal):
    def run(self):
        print("Dog is running...")
    def eat(self):
        print("Eating meat...")
class Cat(Animal):
    pass
dog = Dog()
dog.run()
cat = Cat()
cat.run()

#判断一个变量是否是某个类型可以用isinstance()判断
b = Animal()
print(isinstance(b, Animal))
c = Cat()
print(isinstance(c, Cat))
print(isinstance(c, Animal))

def run_twice(animal):
    animal.run()
    animal.run()
run_twice(Animal())
run_twice(Dog())
run_twice(Cat())

class Tortoise(Animal):
    def run(self):
        print("Tortoise is running slowly...")
run_twice(Tortoise())

#著名的“开闭”原则
#对扩展开放：允许新增Animal子类；
#对修改封闭：不需要修改依赖Animal类型的run_twice()等函数。

#对于静态语言（例如Java）来说，如果需要传入Animal类型，则传入的对象必须是Animal类型或者它的子类，
#否则，将无法调用run()方法

#对于Python这样的动态语言来说，则不一定需要传入Animal类型。
#我们只需要保证传入的对象有一个run()方法就可以了：

class Timer(object):
    def run(self):
        print("Start...")
run_twice(Timer())
#这就是动态语言的“鸭子类型”，它并不要求严格的继承体系，
#一个对象只要“看起来像鸭子，走起路来像鸭子”，那它就可以被看做是鸭子。

#判断对象类型，使用type()函数
print(type(123))
print(type("str"))
print(type(None))
print(type(abs))
print(type(b))

print(type(123) == type(456))
print(type(123) == int)
print(type("abc") == str)
print(type("abc") == type(123))

#判断一个对象是否是函数
import types
def fn():
    pass
print(type(fn) == types.FunctionType)
print(type(abs) == types.BuiltinFunctionType)
print(type(lambda x : x) == types.LambdaType)
print(type((x for x in range(10))) == types.GeneratorType)

#要判断class的类型，可以使用isinstance()函数。
print(isinstance(b, Animal))
print(isinstance(c, Animal))

#能用type()判断的基本类型也可以用isinstance()判断
print(isinstance("a", str))
print(isinstance(123, int))
print(isinstance(b"a", bytes))

print(isinstance([1, 2, 3], (list, tuple)))
print(isinstance((1, 2, 3), (list, tuple)))

#如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list
print(dir("ABC"))

print(len("ABC"))
print("ABC".__len__())

class Dog2(Dog):
    def __len__(self):
        return 100
dog2 = Dog2()
print(len(dog2))

print("ABC".lower())

#可以直接操作一个对象的状态
class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x
obj = MyObject()
print(hasattr(obj, "x"))
print(obj.x)
print(hasattr(obj, "y"))
setattr(obj, "y", 19)
print(hasattr(obj, "y"))
print(getattr(obj, "y"))
print(obj.y)
print(getattr(obj, "z", 404))#获取属性，如果不存在，就返回默认值

print(hasattr(obj, "power"))
print(getattr(obj, "power"))
fn = getattr(obj, "power")
print(fn)
print(fn())

#正确用法
def readImage(fp):
    if hasattr(fp, "read"):
        return readData(fp)
    return None

print("实例属性和类属性")
#由于Python是动态语言，根据类创建的实例可以任意绑定属性

class Student2(object):
    name = "Student"
    def __init__(self, name):
        pass#self.name = name

s2 = Student2("Bob")
print(s2.name)#实例没有属性，用类属性
print(Student2.name)
s2.name = "Michael"
print(s2.name)#实例有属性，就直接用
print(Student2.name)
del s2.name
print(s2.name)

#不要把实例属性和类属性使用相同的名字，因为相同名称的实例属性将屏蔽掉类属性
#但是当你删除实例属性后，再使用相同的名称，访问到的将是类属性








