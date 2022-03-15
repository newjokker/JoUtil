# -*- coding: utf-8  -*-
# -*- author: jokker -*-


from JoTools.txkjRes.deteRes import DeteRes


# 类方法
@classmethod
def hello_cls(cls):
    print("cls method")

# 静态方法
@staticmethod
def hello_stastic():
    print("stastic method")

# 实例方法
def hello_self(self):
    print("self method")
    print(self.width)


# setattr(DeteRes, 'hello_cls', hello_cls)
# setattr(DeteRes, 'hello_self', hello_self)
# setattr(DeteRes, 'hello_stastic', hello_stastic)
# --------------------------------------------------------
DeteRes.hello_cls = hello_cls
DeteRes.hello_self = hello_self
DeteRes.hello_stastic = hello_stastic


DeteRes.hello_stastic()
DeteRes.hello_cls()
#
a = DeteRes()
a.hello_cls()
a.hello_self()
a.hello_stastic()



