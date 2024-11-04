# -*- coding: utf-8  -*-
# -*- author: jokker -*-


# 设置属性的时候执行

# 注意在 __init__ 中设置属性额时候也会执行


class Info():

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __getattr__(self, item):
        print("getattr, item : {0}".format(item))

    def __delattr__(self, item):
        print("删除属性 : {0}".format(item))
        del self.__dict__[item]

    def __setattr__(self, key, value):
        print("设置属性 : {0} --> {1}".format(key, value))
        self.__dict__[key] = value


if __name__ == "__main__":


    a = Info('jokker', 30)

    del a.age

    a.hehe = 'good hehe'



