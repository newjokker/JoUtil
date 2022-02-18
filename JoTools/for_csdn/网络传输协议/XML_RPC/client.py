# -*- coding: utf-8  -*-
# -*- author: jokker -*-

from xmlrpc.client import ServerProxy
import hashlib

import numpy
import numpy as np
from labelme import utils
# fixme 这个直接能搞成一个段子服务器，增加一个推送图片服务的功能，这样能自动帮我整理碰到的很有意思的图片和段子
import cv2
import pickle

s = ServerProxy('http://192.168.3.221:11222', allow_none=True)

img_path = r"C:\Users\14271\Desktop\del\face_2.jpg"

frame = cv2.imdecode(np.fromfile(img_path, dtype=np.uint8), 1)

a = pickle.dumps(frame)

res = s.post_img(a, 'jokker')

print(res)

