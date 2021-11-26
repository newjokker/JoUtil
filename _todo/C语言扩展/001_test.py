# -*- coding: utf-8  -*-
# -*- author: jokker -*-


# 报错原因 https://blog.csdn.net/vample/article/details/88877745


import ctypes

lib = ctypes.CDLL("./test.dll")
lib.test()



