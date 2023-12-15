# -*- coding: utf-8  -*-
# -*- author: jokker -*-



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


class Extender(type):

    def __new__(meta, classnmae, supers, classdict):
        classdict['hello_cls'] = hello_cls
        classdict['hello_self'] = hello_self
        classdict['hello_stastic'] = hello_stastic
        return type.__new__(meta, classnmae, supers, classdict)


class DeteRes(metaclass=Extender):

    pass



DeteRes.hello_stastic()
DeteRes.hello_cls()
#
a = DeteRes()
a.hello_cls()
a.hello_self()
a.hello_stastic()



