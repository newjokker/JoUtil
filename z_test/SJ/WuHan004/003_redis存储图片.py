# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import redis
import base64
import numpy as np

# 图片转文字

with open(r"C:\Users\14271\Desktop\del\img\110kV楼东线_001#_下相_DJI_0081.jpg", "rb") as f:  # 打开01.png图片
    # base64_data = base64.b64encode(f.read())  # 读取图片转换的二进制文件，并给赋值
    r = redis.Redis(host='192.168.3.185', port=6379)
    r.set("jpg_test", f.read())

var = r.get("jpg_test")
print(var)
# data = base64.b64decode(var)  # 把二进制文件解码，并复制给data


img_np_arr = np.fromstring(var, np.uint8)

print(len(data))

print(img_np_arr.shape)

# with open("/home/jd/Pictures/jd.jpeg", "wb") as f:  # 写入生成一个jd.png
#     f.write(data)







