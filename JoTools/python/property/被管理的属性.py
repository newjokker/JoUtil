# -*- coding: utf-8  -*-
# -*- author: jokker -*-



class Person():

    def __init__(self, name):
        self._name = name
        self.__age = 112

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        print("set name")
        self._name = value

    @name.getter
    def name(self):
        print("get name")
        return self._name

    @name.deleter
    def name(self):
        print("delete name")
        del self.__dict__["_name"]


if __name__ == "__main__":

    a = Person("jokker")

    print(a.name)

    a.name = 20

    print(a.__dict__)

    del a.name

    print(a.__dict__)







