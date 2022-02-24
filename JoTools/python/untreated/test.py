# -*- coding: utf-8  -*-
# -*- author: jokker -*-


from JoTools.txkjRes.deteRes import DeteRes



def test():
    print(__name__)


a = DeteRes.__base__

b = a()

print(b)

print(DeteRes.__base__)
print(DeteRes.__bases__)
print(DeteRes.__basicsize__)

