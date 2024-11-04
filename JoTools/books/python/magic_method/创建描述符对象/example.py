# -*- coding: utf-8  -*-
# -*- author: jokker -*-


# 人的性格描述，悲观的？开朗的？敏感的？多疑的？活泼的？等等
class CharacterDescriptor:
    def __init__(self, value):
        self.value = value

    def __get__(self, instance, owner):
        print("访问性格属性")
        return self.value

    def __set__(self, instance, value):
        print("设置性格属性值")
        self.value = value


# 人的体重描述，超重？过重？肥胖？微胖？合适？偏轻？太瘦？等等
class WeightDescriptor:
    def __init__(self, value):
        self.value = value

    def __get__(self, instance, owner):
        print("访问体重属性")
        return self.value

    def __set__(self, instance, value):
        print("设置体重属性值")
        self.value = value


class Person:
    character = CharacterDescriptor('乐观的')
    weight = WeightDescriptor(150)


p = Person()
p2 = Person()

p2.weight = 300

print(p.character)
print(p.weight)




