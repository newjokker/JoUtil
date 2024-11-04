# -*- coding: utf-8  -*-
# -*- author: jokker -*-

"""
__annotations__     : 在Python中，函数会维护一个特殊属性__annotations__，这是一个字典，其中的“键”是被注解的形参名，“值”为注解的内容。 refer : https://www.cnblogs.com/blitheG/p/14662918.html
__builtins__        : 内建函数
__cached__          : 没看懂，refer : https://docs.python.org/zh-cn/3/reference/import.html
__doc__             : 类的注释
__file__            :
__loader__          :
__name__            :
__package__         :
__spec__            : 没看懂 , refer : https://docs.python.org/zh-cn/3/reference/import.html#main-spec
"""





#  列出当前定义的名称
# dir() 不会列出内置函数和变量的名称。这些内容的定义在标准模块 builtins 里
for each in dir():
    print(each, " : ", eval(each))





