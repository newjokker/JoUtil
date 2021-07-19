# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import os
from JoTools.utils.JsonUtil import JsonUtil
from JoTools.utils.FileOperationUtil import FileOperationUtil
from imutils.perspective import four_point_transform
import cv2
import numpy as np


xml_point_dir = r"C:\data\集装箱温度识别\001_data\divide\xml_point"
# img_dir = r"C:\data\集装箱温度识别\001_data\divide\img"
img_dir = r"C:\Users\14271\Desktop\del"


for each_json_path in FileOperationUtil.re_all_file(xml_point_dir, endswitch=['.json']):
    img_path = os.path.join(img_dir, FileOperationUtil.bang_path(each_json_path)[1] + '.jpg')
    a = JsonUtil.load_data_from_json_file(each_json_path)
    shapes = a["shapes"]
    four_points = shapes[0]['points']

    # 图片路径
    image = cv2.imread(img_path, cv2.IMREAD_COLOR)

    print(image.shape)

    # print(four_points)
    rect = four_point_transform(image, np.array(four_points))

    # cv2.imwrite()


    # cv2.imwrite('rect.png', rect)
    # cv2.imshow("rect", rect)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    #
    # break










