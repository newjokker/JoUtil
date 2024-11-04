# -*- coding: utf-8  -*-
# -*- author: jokker -*-


# 只定义特定集合的某些属性，使用之后类变成静态一样，没有了__dict__, 实例也不可新添加属性


class Person(object):
    __slots__ = ('name', 'age')

    def __init__(self, name):
        self.name = name


p = Person('zhiliao')

p.name = "jokker"
p.age = 30

print(p.name, p.age)

p.home = 'yanchen'
print(p.home)











