# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import redis
import pickle
from PIL import Image

# fixme DENIED Redis is running in protected mode because protected mode is enabled --> https://blog.csdn.net/Agly_Clarlie/article/details/52251746
# fixme 185 服务器上开启 redis 服务： ./src/redis-server redis.conf

img_path = r"C:\Users\14271\Desktop\del\res.jpg"


r = redis.StrictRedis(host='192.168.3.185', port=6379)

# 设置关键词
r.set('jokker', 'hello')
# 获取关键词
print(r.get('jokker'))

# todo 将图像存储在 redis 中

# a = Image.open(img_path)
#
# b = pickle.dumps(a)  # frame is numpy.ndarray
# r.set('image',b)


# todo host,port,key

# img = r.get('image')

# for i in range(10):
#     img = pickle.loads(r.get('image'))
#     print(img.width)
#     print(img.height)
#








