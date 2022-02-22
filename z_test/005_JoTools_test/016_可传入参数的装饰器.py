# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import time
from JoTools.utils.DecoratorUtil import DecoratorUtil

@DecoratorUtil.time_this_new_2(2)
def test():
    time.sleep(1)




test()