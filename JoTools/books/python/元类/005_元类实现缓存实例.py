# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import weakref

class Cached(type):

    def __init__(self, *args, **kwargs):
        super(Cached, self).__init__(*args, **kwargs)
        self.__cache = weakref.WeakValueDictionary()

    def __call__(cls, *args):
        if args in cls.__cache:
            return cls.__cache[args]
        else:
            obj = super().__call__(*args)
            cls.__cache[args] = obj
            return obj


class Spam(metaclass=Cached):
    def __init__(self, name):
        print("Creating Spam {0}".format(name))



if __name__ == "__main__":

    a = Spam("jokker_001")
    b = Spam("jokker_002")
    c = Spam("jokker_001")
    d = Spam("jokker_004")

    print(a is b)
    print(a is c)


















