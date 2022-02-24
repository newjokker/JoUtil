# -*- coding: utf-8  -*-
# -*- author: jokker -*-

"""
* 类是元类的实例，所以在创建一个普通类时，其实会走元类的 __new__
"""

# # 注意要从type继承
class BaseClass(type):
    def __new__(cls, *args, **kwargs):
        print("in BaseClass")
        return super().__new__(cls, *args, **kwargs)

class User(metaclass=BaseClass):
    def __init__(self, name):
        print("in User")
        self.name = name

user = User("wangbm")


