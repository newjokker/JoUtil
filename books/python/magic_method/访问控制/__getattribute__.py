# -*- coding: utf-8  -*-
# -*- author: jokker -*-

# __getattr__ 针对未定义的属性运行

# __getattribute__ 针对所有属性运行，必须小心避免通过把属性访问传递给父类而导致的递归循环

# 存在 __getattribute__ 就不运行 __getattr__


class Info():

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __getattr__(self, item):
        print("getattr, item : {0}".format(item))

    def __getattribute__(self, item):
        print("getattribute, item : {0}".format(item))



if __name__ == "__main__":


    a = Info('jokker', 30)

    # print(a.age)

    print(a.hehe)
