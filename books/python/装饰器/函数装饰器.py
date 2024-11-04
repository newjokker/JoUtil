# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import time
from functools import wraps


# 装饰器就是一个输入是函数输出是装饰后的函数的函数而已

# 如果不加 @wraps(func) 原函数的一些属性就会被覆盖掉，比如函数名等


def time_this(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        new_func = func(*args, **kwargs)
        use_time = time.time() - start_time
        print("* use time {0}".format(use_time))
        return new_func
    return wrapper


@time_this
def spend_time(n):
    time.sleep(n)


if __name__ == "__main__":


    print(spend_time.__name__)

    spend_time(1)


