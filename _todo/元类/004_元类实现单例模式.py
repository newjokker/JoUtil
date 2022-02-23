# -*- coding: utf-8  -*-
# -*- author: jokker -*-


# meta __new__ --> meta __init__ --> __new__ --> __init__


class SingleMetaclass(type):

    def __init__(cls, *args, **kwargs):
        cls.__instance = None
        print("run init meta")
        super().__init__(*args, **kwargs)

    def __new__(mcs, name, bases, attrs):
        # __new__ 在 __init__ 之前运行
        # 这边可以对类进行修改
        print("run new")
        return type.__new__(mcs, name, bases, attrs)

    def __call__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__call__(*args, **kwargs)
            return cls.__instance
        else:
            return cls.__instance


class Spam(metaclass=SingleMetaclass):
    def __init__(self, name):
        self.name = name
        print("run init")
        print("create spam")


if __name__ == "__main__":

    a = Spam('jokker')
    b = Spam('homr')

    print(a is b)

    # print(abs(a))
