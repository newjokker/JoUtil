# -*- coding: utf-8  -*-
# -*- author: jokker -*-


import redis
import pickle
from PIL import Image

# fixme DENIED Redis is running in protected mode because protected mode is enabled --> https://blog.csdn.net/Agly_Clarlie/article/details/52251746

img_path = r"C:\Users\14271\Desktop\del\res.jpg"


r = redis.StrictRedis(host='192.168.3.185', port=6379)


print(len(r.keys()))

for each in r.keys():
    r.delete(each)


