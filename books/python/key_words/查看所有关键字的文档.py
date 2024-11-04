# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import builtins


for each in dir(builtins):
    print(("{0}".format(each)).center(20, "*"))
    print(each.__doc__)
    print('-'*50)


