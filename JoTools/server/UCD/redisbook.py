# -*- coding: utf-8  -*-
# -*- author: jokker -*-


import redis


r = redis.Redis(host='192.168.3.221', port=6379, db=0)


# 插入信息
r.hset("menu", "cmd", "常用命令")

