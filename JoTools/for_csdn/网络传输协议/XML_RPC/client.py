# -*- coding: utf-8  -*-
# -*- author: jokker -*-

from xmlrpc.client import ServerProxy
import hashlib


# fixme 这个直接能搞成一个段子服务器，增加一个推送图片服务的功能，这样能自动帮我整理碰到的很有意思的图片和段子

s = ServerProxy('http://192.168.3.221:11222', allow_none=True)




def get_str_md5(assign_str):
    md5 = hashlib.md5()
    md5.update(assign_str)
    return md5.hexdigest()



print(get_str_md5(b'123456'))

exit()



# s.set("name", "jokker")
# s.set("age", "30")
#
# print(s.get("name"))


s.set("img_data"*100000, b'img_data')

print(type(s.get("img_data")))





