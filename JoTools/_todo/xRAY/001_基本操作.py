# -*- coding: utf-8  -*-
# -*- author: jokker -*-


# todo 读取数据并二值化

# todo 亮度均衡化

import cv2
import numpy as np
from  JoTools.utils.FileOperationUtil import FileOperationUtil

img_path = r"C:\Users\14271\Desktop\del\J22300549663-OK-20210131181951636-2.jpg"
# img_dir = r"C:\Users\14271\Desktop\20210315 XRAY\翻折1\1号机翻折图片"


# for each_img_path in FileOperationUtil.re_all_file(img_dir, endswitch=['.jpg']):
# for each_img_path in FileOperationUtil.re_all_file(img_dir):


img_mat = cv2.imdecode(np.fromfile(img_path, dtype=np.uint8), 1)

ret, thresh1 = cv2.threshold(img_mat, 70, 255, cv2.THRESH_BINARY)

cv2.imwrite(r"C:\Users\14271\Desktop\del\test_hehe.jpg", thresh1)






