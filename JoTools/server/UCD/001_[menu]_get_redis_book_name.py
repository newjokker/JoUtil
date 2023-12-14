# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import redis

r = redis.Redis(host='192.168.3.221', port=6379, db=0)

a = r.hgetall("menu")

a = r.hdel("menu", "info")

a = r.hset("menu", "official", "个人不可修改只能看的信息")

# for each in a:
#     print(each.decode('utf-8').ljust(15, " "), a[each].decode('utf-8'))
#


