# -*- coding: utf-8  -*-
# -*- author: jokker -*-


from JoTools.txkjRes.deteRes import DeteRes


def hello():
    print("i'm new method")

DeteRes.__dict__["hello"] = hello


print(DeteRes.__dict__)


DeteRes.hello()






