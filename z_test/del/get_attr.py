# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import functools
import types


def print_ok(cls):
    print("ok")

class Extender(type):

    def __new__(meta, classnmae, supers, classdict):
        def print_ok(cls):
            print("ok")
        classdict['hello_cls'] = print_ok
        return type.__new__(meta, classnmae, supers, classdict)

class test(metaclass=Extender):

    def __init__(self):
        self.menber = 1
        pass

    def __getattribute__(self, item):
        print(item)
        return super().__getattribute__(item)

    # def __getattr__(self, item):
    #     print(item)
    #     # self.print()
    #     return super(test, self).__getattr__(item)

    def print(self):
        print("print")


if __name__ == "__main__":


    a = test()

    test.ook = types.MethodType(print_ok, test)

    # print(a.menber)
    # a.print()

    # print(a.hello_cls)
    print(test.hello_cls)
    print(test.ook)
    print(test.print)











