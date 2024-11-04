# -*- coding: utf-8  -*-
# -*- author: jokker -*-

# refer : https://zhuanlan.zhihu.com/p/269012792

# 准备一个基类（父类）
class BaseClass:
    def talk(self):
        print("i am people")

# 准备一个方法
def say(self):
    print("hello")

# 使用type来创建User类
User = type("User", (BaseClass, ), {"name":"user", "say":say})

a = User()


print(a.name)

a.say()







