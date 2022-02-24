# -*- coding: utf-8  -*-
# -*- author: jokker -*-

# 装饰器可以设置属性，这么来玩

# 用装饰器实现的计数器


class tracer:

    def __init__(self, func):
        self.calls = 0
        self.func = func

    def __call__(self, *args, **kwargs):
        self.calls += 1
        print("call %s to %s" % (self.calls, self.func.__name__))
        return self.func(*args, **kwargs)

@tracer
def spam(a, b, c):
    return a + b + c

@tracer
def eggs(x, y):
    return x+y


if __name__ == "__main__":

    print(spam(1, 2, 3))
    print(spam(1, 2, 3))

    print(eggs(5, 6))
    print(eggs(5, 6))










