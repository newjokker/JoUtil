# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import ctypes
import time

# refer: https://codeantenna.com/a/46nPwiHOva

so = ctypes.cdll.LoadLibrary('./_py_go.so')
fib = so.PrintRes
result = fib(b"../")
print(result)




