# -*- coding: utf-8  -*-
# -*- author: jokker -*-


# 类型，等效于 type() ?


from JoTools.txkjRes.deteRes import DeteRes

a = DeteRes()

print(DeteRes.__class__)

print("123".__class__)

print(a.__class__)

print(type(DeteRes))

print(type("123"))

print(type(a))

