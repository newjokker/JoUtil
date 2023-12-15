# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import ctypes
import time

# refer: https://codeantenna.com/a/46nPwiHOva
# refer: https://www.cnblogs.com/traditional/p/14781980.html

so = ctypes.cdll.LoadLibrary('./_py_go.so')
fib = so.PrintRes
fib.restype = ctypes.c_char_p
result = fib(b"../")
print(result)




