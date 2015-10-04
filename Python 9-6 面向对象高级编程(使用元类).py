#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'hina'

from hello import Hello

h = Hello()
h.hello()

# type()函数可以查看一个类型或变量的类型
print(type(Hello))
print(type(h))


# type()函数既可以返回一个对象的类型，又可以创建出新的类型
def fn(self, name="word"):
    print("Hello, %s." % name)


# 要创建一个class对象，type()函数依次传入3个参数：
# class的名称；
# 继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
# class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。

Hello2 = type("Hello", (object,), dict(hello=fn))  # 创建Hello2 class
h2 = Hello2()
h2.hello()
print(type(Hello2))
print(type(h2))


# type()函数也允许我们动态创建出类来，也就是说，动态语言本身支持运行期动态创建类

# 但是如果我们想创建出类呢？那就必须根据metaclass创建出类，所以：先定义metaclass，然后创建类。

class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs["add"] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)


class MyList(list, metaclass=ListMetaclass):
    pass


L = MyList()
L.add(1)
print(L)


# 动态修改有什么意义？直接在MyList定义中写上add()方法不是更简单吗？正常情况下，确实应该直接写，通过metaclass修改纯属变态

# 但是，总会遇到需要通过metaclass修改类定义的。ORM就是一个典型的例子
# ORM全称“Object Relational Mapping”，即对象-关系映射，
# 就是把关系数据库的一行映射为一个对象，也就是一个类对应一个表

# 要编写一个ORM框架，所有的类都只能动态定义，因为只有使用者才能根据表的结构定义出对应的类来

class Field(object):
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return "<%s:%s>" % (self.__class__.__name__, self.name)


class StringField(Field):
    def __init__(self, name):
        super(StringField, self).__init__(name, "varchar(100)")


class IntegerField(Field):
    def __init__(self, name):
        super(IntegerField, self).__init__(name, "bigint")


class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        if name == "Model":
            return type.__new__(cls, name, bases, attrs)
        print("Found model: %s" % name)
        mappings = dict()
        for k, v in attrs.items():
            if isinstance(v, Field):
                print("Found mapping: %s ==> %s" % (k, v))
                mappings[k] = v
        for k in mappings.keys():
            attrs.pop(k)
        attrs["__mappings__"] = mappings
        attrs["__table__"] = name
        return type.__new__(cls, name, bases, attrs)


class Model(dict, metaclass = ModelMetaclass):
    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            params.append("?")
            args.append(getattr(self, k, None))
        sql = "insert into %s (%s) values (%s)" % (self.__table__, ",".join(fields), ",".join(params))
        print("SQL: %s" % sql)
        print("ARGS: %s" % str(args))


class User(Model):
    id = IntegerField("id")
    name = StringField("username")
    email = StringField("email")
    password = StringField("password")


u = User(id=1234, name="Michael", email="test@orm.org", password="my-pwd")
u.save()
