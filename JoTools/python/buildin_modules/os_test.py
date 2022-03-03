# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import sys
import os
import nt

from JoTools.txkjRes.deteRes import DeteRes

from os_t import heh


print(heh(24))

# posix代表类 Unix, nt表示 Windows 系统,不同操作系统在安装Python环境时，windows有nt模块而没有posix模块，linux中则相反
# sys.modules['os_t.heh'] = lambda x:x*x 规范模块名
# sys.modules是一个全局字典，Python启动后就加载在内存中，记录新导入的模块
#
