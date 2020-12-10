# -*- coding: utf-8  -*-
# -*- author: jokker -*-


import os
import copy
import random
from JoTools.txkj.parseXml import ParseXml, parse_xml
from JoTools.utils.FileOperationUtil import FileOperationUtil
from JoTools.detectionResult import DeteRes
from PIL import Image



class DatabaseKG():
    """开口销使用的函数"""

    # todo 图像随机旋转，只旋转 90 的倍数，还是用黑框补全

    @staticmethod
    def is_in_range(range_0, range_1):
        """判断一个范围是不是包裹另外一个范围，(xmin, ymin, xmax, ymax)"""
        x_min_0, y_min_0, x_max_0, y_max_0 = range_0
        x_min_1, y_min_1, x_max_1, y_max_1 = range_1
        #
        if x_min_0 < x_min_1:
            return False
        elif x_max_0 > x_max_1:
            return False
        elif y_min_0 < y_min_1:
            return False
        elif y_max_0 > y_max_1:
            return False
        else:
            return True

    @staticmethod
    def _cal_iou_1(dete_obj_1, dete_obj_2, ignore_tag=False):
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
    def get_subset_from_pic(xml_path, img_path, save_dir, min_count=6, small_img_count=3, iou_1=0.5):
        """从一个图片中拿到标签元素的子集"""

        a = DeteRes(xml_path, img_path)
        # 获取所有 box 位置
        box_list = []
        for each_box in a.alarms:
            box_list.append(each_box.get_rectangle())
        #
        img_dir = os.path.join(save_dir, 'JPEGImages')
        xml_dir = os.path.join(save_dir, 'Annotations')
        if not os.path.exists(img_dir): os.makedirs(img_dir)
        if not os.path.exists(xml_dir): os.makedirs(xml_dir)
        # 保存最大范围
        merge_range = a.get_max_range()
        save_name = os.path.split(xml_path)[1][:-4]
        a.save_assign_range(assign_range=merge_range, save_dir=save_dir, iou_1=0.5, save_name=save_name)

        # 元素个数大于阈值，另外生成小图
        if len(box_list) >= min_count:
            for i in range(small_img_count):
                # 打乱顺序
                random.shuffle(box_list)
                # 拿出其中的三个，得到外接矩形的外接矩形，如果只有两个元素那就拿出前两个
                if len(box_list) == 2:
                    merge_range = DatabaseKG.merge_range_list(box_list[:2])
                else:
                    merge_range = DatabaseKG.merge_range_list(box_list[:3])
                # 截取指定范围并保存
                save_name  = os.path.split(xml_path)[1][:-4] + "_{0}".format(i)
                a.save_assign_range(assign_range=merge_range, save_dir=save_dir, iou_1=iou_1, save_name=save_name)



if __name__ == "__main__":


    # --------------------------------------------------------------------------------------------------------
    xmlDir = r"C:\Users\14271\Desktop\kkx_xml\xml"
    imgDir = r"C:\Users\14271\Desktop\kkx_xml\img"
    saveDir = r"C:\Users\14271\Desktop\kkx_clc"

    for index, each_xml_path in enumerate(FileOperationUtil.re_all_file(xmlDir, lambda x:str(x).endswith((".xml")))):
        print(index, each_xml_path)

        each_img_path = os.path.join(imgDir, os.path.split(each_xml_path)[1][:-4] + '.jpg')
        DatabaseKG.get_subset_from_pic(each_xml_path, each_img_path, saveDir, min_count=4, small_img_count=20)
    # --------------------------------------------------------------------------------------------------------

    # todo 输入参数，xml_info img_mat 输出参数: [(xml_info, img_mat), ()]
