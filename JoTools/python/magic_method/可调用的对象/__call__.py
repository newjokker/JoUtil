# -*- coding: utf-8  -*-
# -*- author: jokker -*-

# 代码逻辑很复杂时，不适合写成一个函数内，会封装成类，调用该类对象时，我们直接使用实例作为函数引用，更方便简洁.
# 通过call 实现类装饰器. (还有一种思路，cookboook p341)

# torch 中的各个 model 就是实现的 __call__ 方法，才能 model(ndarry) 这样使用


class Bar1:
    def __call__(self, assign_str="123"):
        print('i am instance method : {0}'.format(assign_str))

class Bar2:

    def __init__(self, p1):
        self.p1 = p1

    def __call__(self, func):
        def wrapper():
            print("Starting", func.__name__)
            print("p1=", self.p1)
            func()
            print("Ending", func.__name__)
        return wrapper


@Bar2("foo bar")
def hello():
    print("Hello")



if __name__ == "__main__":

    b = Bar1()              # 实例化
    b('jokker')             # 实例对象b 可以作为函数调用 等同于b.__call__ 使用


    hello()
