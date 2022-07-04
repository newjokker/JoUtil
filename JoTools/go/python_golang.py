# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import ctypes
import time


so = ctypes.cdll.LoadLibrary('./test.so')
fib = so.AnalysisFile
result = fib()




