# -*- coding: utf-8  -*-
# -*- author: jokker -*-

# 类的静态函数、类函数、普通函数、全局变量以及一些内置的属性都是放在类__dict__里
# python 中 一些内置的数据类型是没有__dict__属性的

# 类的 __dict__ 属性
# 类的实例的 __dict__ 属性




from JoTools.txkjRes.deteRes import DeteRes


a = DeteRes(r"C:\Users\14271\Desktop\del\del.xml")


print(DeteRes.__dict__)

print(a.__dict__)


# ------------------------ 可以用于简化代码 ---------------------------------

# Person1 和 Person2 能实现一样的功能

class Person1:
    def __init__(self,_obj):
        self.name = _obj['name']
        self.age = _obj['age']
        self.energy = _obj['energy']
        self.gender = _obj['gender']
        self.email = _obj['email']
        self.phone = _obj['phone']
        self.country = _obj['country']

class Person2:
    def __init__(self,_obj):
        self.__dict__.update(_obj)








