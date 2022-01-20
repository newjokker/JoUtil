# -*- coding: utf-8  -*-
# -*- author: jokker -*-

from JoTools.utils.DecoratorUtil import DecoratorUtil
import logging
from JoTools.utils.LogUtil import LogUtil


log = LogUtil.get_log(r"C:\Users\14271\Desktop\del.log", 4, "test", print_to_console=True)



def test(x, y):

    log.info("* start")

    for i in range(10):
        print(x+y)

    log.info("* stop")
    return x+y



test(2,3)

