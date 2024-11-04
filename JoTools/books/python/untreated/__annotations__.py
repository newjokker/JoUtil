# -*- coding: utf-8  -*-
# -*- author: jokker -*-


# 在Python中，函数会维护一个特殊属性__annotations__，这是一个字典，其中的“键”是被注解的形参名，“值”为注解的内容。
# refer : https://www.cnblogs.com/blitheG/p/14662918.html




def add(a:int, b:float):
    return a + b


jokker:float


print(add.__annotations__)

print(__annotations__)


