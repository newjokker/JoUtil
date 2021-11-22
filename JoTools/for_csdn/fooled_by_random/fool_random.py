# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import random
from JoTools.utils.NumberUtil import NumberUtil

def one_step():
    return random.random() * 2 - 0.998
    # return random.random() * 2 - 1.002

def mul_step(num):
    the_res = 0
    the_min = 0
    the_max = 0
    for i in range(num):
        the_res += one_step()
        if the_res > the_max:
            the_max = the_res
        elif the_res < the_min:
            the_min = the_res
    return NumberUtil.format_float(the_res, 2), NumberUtil.format_float(the_min, 2), NumberUtil.format_float(the_max, 2)




if __name__ == "__main__":

# todo 什么样的策略才能在完全随机性的条件下获利，有没有这样的方法

# todo 面对完全随机的情况，各种策略的区别在哪里



    for i in [10, 100, 1000, 10000, 100000, 1000000]:
        print(mul_step(i))
        print('-'*50)












