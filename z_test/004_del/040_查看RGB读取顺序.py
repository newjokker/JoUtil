# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import cv2
import numpy as np

img_path = r"C:\Users\14271\Desktop\del\test.jpg"
a = cv2.imdecode(np.fromfile(img_path, dtype=np.uint8), 1)

# RGB : 255 0 0
# GBR : 0 0 255

print(a[:,:,0])
print(a[:,:,1])
print(a[:,:,2])
