# -*- coding: utf-8  -*-
# -*- author: jokker -*-


# 模块调用的话返回模块的父类元组，最开始的是父类，后面一个是父类的父类，等等


from JoTools.txkjRes.deteRes import DeteRes


print(DeteRes.__bases__)


print(DeteRes.__mro__)