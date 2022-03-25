# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
import time
import JoTools.txkjRes.segmentObj
from JoTools.utils.PointsUtil import PointsUtil
from JoTools.txkjRes.segmentRes import SegmentRes
from JoTools.txkjRes.segmentObj import SegmentObj
from JoTools.utils.FileOperationUtil import FileOperationUtil

def get_lines(img):
    """提取线段"""
    position = np.argwhere(img_ndarry[:,:,0]==2)
    position = position.tolist()
    # top = PointsUtil.get_top_point(position)
    # bottom = PointsUtil.get_bottom_point(position)
    # top, bottom = PointsUtil.bounding_rect_middle_line(position)
    top, bottom = PointsUtil.get_fit_line(position)

    position = np.argwhere(img_ndarry[:,:,0]==1)
    position = position.tolist()
    # left = PointsUtil.get_left_point(position)
    # right = PointsUtil.get_right_point(position)
    # left, right = PointsUtil.bounding_rect_middle_line(position)
    left, right = PointsUtil.get_fit_line(position)

    #
    left = [left[1], left[0]]
    right = [right[1], right[0]]
    top = [top[1], top[0]]
    bottom = [bottom[1], bottom[0]]
    return [[left, right], [bottom, top]]

def get_lines_2(img):
    """提取线段"""
    position = np.argwhere(img_ndarry[:,:,0]==2)
    position = position.tolist()
    # top = PointsUtil.get_top_point(position)
    # bottom = PointsUtil.get_bottom_point(position)
    top, bottom = PointsUtil.bounding_rect_middle_line(position)
    # top, bottom = PointsUtil.get_fit_line(position)

    position = np.argwhere(img_ndarry[:,:,0]==1)
    position = position.tolist()
    # left = PointsUtil.get_left_point(position)
    # right = PointsUtil.get_right_point(position)
    left, right = PointsUtil.bounding_rect_middle_line(position)
    # left, right = PointsUtil.get_fit_line(position)

    #
    left = [left[1], left[0]]
    right = [right[1], right[0]]
    top = [top[1], top[0]]
    bottom = [bottom[1], bottom[0]]
    return [[left, right], [bottom, top]]


img_dir = r"C:\Users\14271\Desktop\xj_labelme\JPEGImages"
mask_dir = r"C:\Users\14271\Desktop\xj_labelme\SegmentationClass"


for img_path in FileOperationUtil.re_all_file(img_dir):

    try:

        each_img_name = os.path.split(img_path)[1]
        mask_path = os.path.join(mask_dir, each_img_name)

        if not os.path.exists(mask_path):
            continue
        else:
            print(img_path)

        img_ndarry = cv2.imdecode(np.fromfile(mask_path, dtype=np.uint8), 1)
        a = SegmentRes()
        a.img_path = img_path

        lines = get_lines(img_ndarry)
        for index, each_line in enumerate(lines):
            each_line_obj = SegmentObj(points=each_line, label=['guaban', 'chuanti'][index], shape_type="line")
            a.shapes.append(each_line_obj)

        save_path = a.img_path[:-3] + 'json'
        a.save_to_json(save_path)

    except Exception as e:
        print(e)

    # mask = cv2.imdecode(np.fromfile(mask_path, dtype=np.uint8), 1)
    # mask = mask * 125
    #
    # cv2.circle(mask, (int(lines[0][0][0]), int(lines[0][0][1])), 5, [255, 0, 255], 2)
    # cv2.circle(mask, (int(lines[0][1][0]), int(lines[0][1][1])), 5, [255, 0, 255], 2)
    # cv2.circle(mask, (int(lines[1][0][0]), int(lines[1][0][1])), 5, [255, 0, 255], 2)
    # cv2.circle(mask, (int(lines[1][1][0]), int(lines[1][1][1])), 5, [255, 0, 255], 2)
    #
    # lines = get_lines_2(img_ndarry)
    # cv2.circle(mask, (int(lines[0][0][0]), int(lines[0][0][1])), 5, [255, 0, 0], 2)
    # cv2.circle(mask, (int(lines[0][1][0]), int(lines[0][1][1])), 5, [255, 0, 0], 2)
    # cv2.circle(mask, (int(lines[1][0][0]), int(lines[1][0][1])), 5, [255, 0, 0], 2)
    # cv2.circle(mask, (int(lines[1][1][0]), int(lines[1][1][1])), 5, [255, 0, 0], 2)



    # plt.imshow(mask)
    # plt.show()

    # break

    # cv2.imshow('test', mask)
    # time.sleep(50)




























