# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import redis



# 创建Redis客户端对象
r = redis.Redis(host='192.168.3.221', port=6379, db=0)


r.hset("menu", "info", "常用的一些信息")


