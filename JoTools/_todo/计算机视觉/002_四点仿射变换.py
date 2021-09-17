# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import os
import cv2
import numpy as np
from JoTools.utils.JsonUtil import JsonUtil
from JoTools.utils.FileOperationUtil import FileOperationUtil
from imutils.perspective import four_point_transform



def transform_img_with_4_point(img_mat, four_points, save_path=None):
    """使用四个点对图像进行仿射变换，four_points, 支持浮点，"""

    #
    if len(four_points) != 4:
        print("* 只能输入四个点")
        return None
    #
    if isinstance(img_mat, str):
        img_mat = cv2.imdecode(np.fromfile(img_mat, dtype=np.uint8), 1)
    #
    rect = four_point_transform(img_mat, np.array(four_points))
    #
    if save_path:
        # cv2.imwrite(save_path, rect)
        cv2.imencode('.jpg', rect)[1].tofile(save_path)

    return rect






if __name__ == "__main__":


    xml_point_dir = r"C:\Users\14271\Desktop\jizhuangxiang\img"
    img_dir = r"C:\Users\14271\Desktop\jizhuangxiang\img"
    save_dir = r"C:\Users\14271\Desktop\jizhuangxiang\crop"

    for each_json_path in FileOperationUtil.re_all_file(xml_point_dir, endswitch=['.json']):
        img_path = os.path.join(img_dir, FileOperationUtil.bang_path(each_json_path)[1] + '.png')
        four_points = JsonUtil.load_data_from_json_file(each_json_path)["shapes"][0]['points']
        each_save_path = os.path.join(save_dir, FileOperationUtil.bang_path(each_json_path)[1] + '.jpg')
        # transform
        transform_img_with_4_point(img_path, four_points, each_save_path)



