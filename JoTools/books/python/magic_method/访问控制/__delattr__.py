# -*- coding: utf-8  -*-
# -*- author: jokker -*-

# 删除属性的时候执行


class Info():

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __getattr__(self, item):
        print("getattr, item : {0}".format(item))

    def __delattr__(self, item):
        print("删除属性 : {0}".format(item))
        del self.__dict__[item]

if __name__ == "__main__":


    a = Info('jokker', 30)

    del a.age

    print(a.age)



