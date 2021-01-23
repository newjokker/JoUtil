# -*- coding: utf-8  -*-
# -*- author: jokker -*-


"""相关的工具"""

import cv2
import numpy as np


class ResTools(object):
    """Res 需要的函数"""

    @staticmethod
    def merge_range_list(range_list):
        """进行区域合并得到大的区域"""
        x_min_list, y_min_list, x_max_list, y_max_list = [], [], [], []
        for each_range in range_list:
            x_min_list.append(each_range[0])
            y_min_list.append(each_range[1])
            x_max_list.append(each_range[2])
            y_max_list.append(each_range[3])
        return (min(x_min_list), min(y_min_list), max(x_max_list), max(y_max_list))

    @staticmethod
    def region_augment(region_rect, img_size, augment_parameter=None):
        """上下左右指定扩增长宽的比例, augment_parameter, 左右上下"""
        if augment_parameter is None:
            augment_parameter = [0.6, 0.6, 0.1, 0.1]

        widht, height = img_size
        x_min, y_min, x_max, y_max = region_rect
        region_width = int(x_max - x_min)
        region_height = int(y_max - y_min)
        #
        new_x_min = x_min - int(region_width * augment_parameter[0])
        new_x_max = x_max + int(region_width * augment_parameter[1])
        new_y_min = y_min - int(region_height * augment_parameter[2])
        new_y_max = y_max + int(region_height * augment_parameter[3])
        #
        new_x_min = max(0, new_x_min)
        new_y_min = max(0, new_y_min)
        new_x_max = min(widht, new_x_max)
        new_y_max = min(height, new_y_max)

        return (new_x_min, new_y_min, new_x_max, new_y_max)

    @staticmethod
    def cal_iou(dete_obj_1, dete_obj_2, ignore_tag=False):
        """计算两个检测结果相交程度, xmin, ymin, xmax, ymax，标签不同，检测结果相交为 0, ignore_tag 为 True 那么不同标签也计算 iou"""
        if dete_obj_1.tag != dete_obj_2.tag and ignore_tag is False:
            return 0.0
        else:
            dx = max(min(dete_obj_1.x2, dete_obj_2.x2) - max(dete_obj_1.x1, dete_obj_2.x1) + 1, 0)
            dy = max(min(dete_obj_1.y2, dete_obj_2.y2) - max(dete_obj_1.y1, dete_obj_2.y1) + 1, 0)
            overlap_area = dx * dy
            union_area = ((dete_obj_1.x2 - dete_obj_1.x1 + 1) * (dete_obj_1.y2 - dete_obj_1.y1 + 1) +
                          (dete_obj_2.x2 - dete_obj_2.x1 + 1) * (dete_obj_2.y2 - dete_obj_2.y1 + 1) - overlap_area)
            return overlap_area * 1. / union_area

    @staticmethod
    def cal_iou_1(dete_obj_1, dete_obj_2, ignore_tag=False):
        """计算两个矩形框的相交面积，占其中一个矩形框面积的比例 ， """
        if dete_obj_1.tag != dete_obj_2.tag and ignore_tag is False:
            return 0
        else:
            dx = max(min(dete_obj_1.x2, dete_obj_2.x2) - max(dete_obj_1.x1, dete_obj_2.x1) + 1, 0)
            dy = max(min(dete_obj_1.y2, dete_obj_2.y2) - max(dete_obj_1.y1, dete_obj_2.y1) + 1, 0)
            overlap_area = dx * dy
            union_area = ((dete_obj_1.x2 - dete_obj_1.x1 + 1) * (dete_obj_1.y2 - dete_obj_1.y1 + 1))
            return overlap_area * 1. / union_area

    @staticmethod
    def crop_angle_rect(img_path, rect):
        """输入的是弧度，需要转为角度"""
        # get the parameter of the small rectangle
        print(rect)
        center, size, angle = rect[0], rect[1], rect[2]
        center, size = tuple(map(int, center)), tuple(map(int, size))
        # get row and col num in img
        img = cv2.imdecode(np.fromfile(img_path, dtype=np.uint8), 1)
        height, width = img.shape[0], img.shape[1]
        # calculate the rotation matrix
        M = cv2.getRotationMatrix2D(center, (180*angle)/3.14, 1)
        # rotate the original image
        img_rot = cv2.warpAffine(img, M, (width, height))
        # now rotated rectangle becomes vertical and we crop it
        img_crop = cv2.getRectSubPix(img_rot, size, center)
        return img_crop

