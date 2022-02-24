# -*- coding: utf-8  -*-
# -*- author: jokker -*-


# __loader__是由加载器在导入的模块上设置的属性，访问它时将会返回加载器对象本身。

#

import os

print(__loader__)

print(os.__loader__)