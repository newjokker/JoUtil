# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import redis

r = redis.Redis(host='192.168.3.221', port=6379, db=0)

r.hset("menu", "ucd", "ucd常用方法集锦")


