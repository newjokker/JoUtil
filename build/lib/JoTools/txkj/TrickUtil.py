# -*- coding: utf-8  -*-
# -*- author: jokker -*-

# 模型训练，调参的一些 ticks

# todo 对检测模型进行修改，一次性多检测几个图片

from PIL import Image
import cv2
import numpy as np
import random
import os
from Report.FileOperationUtil import FileOperationUtil
from TXKJ_DP.DPTools.parseXml import ParseXml, parse_xml
import uuid
import shutil


class TrickUtil(object):

    @staticmethod
    def region_augment(region_rect, img_size, augment_parameter=None):
        """上下左右指定扩增长宽的比例, augment_parameter, 左右上下"""

        if augment_parameter is None:
            augment_parameter = [0.6, 0.6, 0.1, 0.1]

        widht, height = img_size
        x_min, y_min, x_max, y_max = region_rect
        region_width = int(x_max - x_min)
        region_height = int(y_max - y_min)
        new_x_min = x_min - int(region_width * augment_parameter[0])
        new_x_max = x_max + int(region_width * augment_parameter[1])
        new_y_min = y_min - int(region_height * augment_parameter[2])
        new_y_max = y_max + int(region_height * augment_parameter[3])

        new_x_min = max(0, new_x_min)
        new_y_min = max(0, new_y_min)
        new_x_max = min(widht, new_x_max)
        new_y_max = min(height, new_y_max)

        return (new_x_min, new_y_min, new_x_max, new_y_max)

    # ---------------------------------------------- 图像裁剪为小图 -----------------------------------------------------

    @staticmethod
    def cut_img_to_small(img_path, save_dir, cut_num=2, overlap_ratio=0.1):
        """将图片裁切成下图，小图之间留有重叠，按照多个层次进行裁剪，切出来的图像与原图像比例一致，图像之间需要有一定的重合比例"""
        img = Image.open(img_path)
        (width, height) = img.size
        # 遍历每个区块
        for i in range(cut_num):
            for j in range(cut_num):
                # 找到按照规则应该
                x1, y1 = int(width * (float(i)/float(cut_num))), int(height * (float(j)/float(cut_num)))
                x2, y2 = int(width * (float(i + 1) / float(cut_num))), int(height * (float(j+1)/float(cut_num)))
                region_range = [x1, y1, x2, y2]
                # 对范围进行扩展，得到新的范围
                extend_region = TrickUtil.region_augment(region_range, (width, height), augment_parameter=[overlap_ratio]*4)
                save_path = os.path.join(save_dir, os.path.split(img_path)[1][:-4] + "_{0}_{1}.jpg".format(extend_region[0], extend_region[1]))
                each_img = img.crop(extend_region)
                each_img.save(save_path)

    @staticmethod
    def cut_img_mat_to_small_memory(img, cut_num=2, overlap_ratio=0.1):
        """cut_img_to_small 不保存为图片，输出对应的矩阵的版本, 将他们合并为一个矩阵列表，和一个偏移量列表，矩阵可以重采样为指定大小"""
        img_mat_list = []
        img_offset_list = []
        # res = {}
        (height, width) = img.shape[:2]
        # 遍历每个区块
        for i in range(cut_num):
            for j in range(cut_num):
                # 找到按照规则应该
                x1, y1 = int(width * (float(i)/float(cut_num))), int(height * (float(j)/float(cut_num)))
                x2, y2 = int(width * (float(i + 1) / float(cut_num))), int(height * (float(j+1)/float(cut_num)))
                region_range = [x1, y1, x2, y2]
                # 对范围进行扩展，得到新的范围
                extend_region = TrickUtil.region_augment(region_range, (width, height), augment_parameter=[overlap_ratio]*4)
                # res[(extend_region[0], extend_region[1])] = img[extend_region[1]:extend_region[3]+1, extend_region[0]:extend_region[2]]
                img_mat_list.append(img[extend_region[1]:extend_region[3]+1, extend_region[0]:extend_region[2]])
                img_offset_list.append((extend_region[0], extend_region[1]))

        return img_mat_list, img_offset_list

    # ----------------------------------------------- 常用的函数 --------------------------------------------------------

    @staticmethod
    def cal_iou(dete_res_1, dete_res_2, ignore_tag=False):
        """计算两个检测结果相交程度, xmin, ymin, xmax, ymax，标签不同，检测结果相交为 0, ignore_tag 为 True 那么不同标签也计算 iou"""
        if dete_res_1.tag != dete_res_2.tag and ignore_tag is False:
            return 0
        else:
            dx = max(min(dete_res_1.x2, dete_res_2.x2) - max(dete_res_1.x1, dete_res_2.x1) + 1, 0)
            dy = max(min(dete_res_1.y2, dete_res_2.y2) - max(dete_res_1.y1, dete_res_2.y1) + 1, 0)
            overlap_area = dx * dy
            union_area = ((dete_res_1.x2 - dete_res_1.x1 + 1) * (dete_res_1.y2 - dete_res_1.y1 + 1) +
                          (dete_res_2.x2 - dete_res_2.x1 + 1) * (dete_res_2.y2 - dete_res_2.y1 + 1) - overlap_area)
            return overlap_area * 1. / union_area

    @staticmethod
    def do_nms_for_res(dete_res_list, threshold=0.1, ignore_tag=False):
        """对结果做 nms 处理，"""
        # 参考：https://blog.csdn.net/shuzfan/article/details/52711706

        # fixme 是否需要对 dete_res 进行更新？

        dete_res_list = sorted(dete_res_list, key=lambda x:x.conf, reverse=True)
        if len(dete_res_list) > 0:
            res = [dete_res_list.pop(0)]
        else:
            return dete_res_list
        # 循环，直到 dete_res_list 中的数据被处理完
        while len(dete_res_list) > 0:
            each_res = dete_res_list.pop(0)
            is_add = True
            for each in res:
                # 计算每两个框之间的 iou，要是 nms 大于阈值，同时标签一致，去除置信度比较小的标签
                if TrickUtil.cal_iou(each, each_res, ignore_tag=ignore_tag) > threshold:
                    is_add = False
                    break
            # 如果判断需要添加到结果中
            if is_add is True:
                res.append(each_res)

        return res

    # ------------------------------------------------------------------------------------------------------------------




    # @staticmethod
    # def draw_lab(dete_res, img_path, save_path):
    #     """在图像上画出检测的结果"""
    #     img = cv2.imdecode(np.fromfile(img_path, dtype=np.uint8), 1)
    #     #
    #     for each in dete_res:
    #         cv2.rectangle(img, (each[2], each[4]), (each[3], each[5]), color=(0,0,255), thickness=3)
    #     #
    #     cv2.imwrite(save_path, img)

    # @staticmethod
    # def get_merge_xml_info_from_xml_list(xml_path_list, img_path):
    #     """解析多个 xml 并将它们合并到一个 xml_info 中"""
    #
    #     # todo 拿到原数据的长宽，就是所有元素的最大长宽，或者这一步，长宽数据并不重要，可以不用考虑
    #     # todo 对小图的结果进行偏移，并进行合并
    #     # todo 大图和小图进行合并，
    #
    #     dete_res = []
    #     for each_xml_path in xml_path_list:
    #         # 解析 xml 信息
    #         each_xml_info = parse_xml(each_xml_path)
    #         # 拿到偏移量
    #         if '_' in os.path.split(each_xml_path)[1]:
    #             offset_info = os.path.split(each_xml_path)[1].split('_')[-2:]
    #             offset_x = int(offset_info[0])
    #             offset_y = int(str(offset_info[1]).rstrip(".xml"))
    #         else:
    #             offset_x, offset_y = 0, 0
    #         #
    #         for each_obj in each_xml_info["object"]:
    #             x_min, x_max = int(each_obj['bndbox']['xmin']), int(each_obj['bndbox']['xmax'])
    #             y_min, y_max = int(each_obj['bndbox']['ymin']), int(each_obj['bndbox']['ymax'])
    #             x_min, x_max, y_min, y_max = x_min + offset_x, x_max + offset_x, y_min + offset_y, y_max + offset_y
    #             dete_res.append([each_obj['name'], random.random(), x_min, x_max, y_min, y_max])
    #
    #     # 画出矩形，显示出类型和概率
    #     # img = cv2.imdecode(np.fromfile(img_path, dtype=np.uint8), 1)
    #     # img.
    #     # print(dete_res)
    #
    #     TrickUtil.draw_lab(dete_res, r"C:\Users\14271\Desktop\大图切小图\大图\test_0.jpg", r"C:\Users\14271\Desktop\test_0.jpg")

    # @staticmethod
    # def merge_detection_res():
    #     """将裁切后检出来的要素进行组合，按照一定的规则对最后的结果进行去除，有的识别了半个，怎么拼接"""
    #
    #     # todo 大图检测不出来，小图有可能检测出来吗？对小图进行一些变换呢？
    #
    #     # todo 按照什么样的规则对检测结果进行拼接？考虑到小图中可能检测到的只是一部分这种情况，需要先过滤到检测不全这个情况
    #
    #     # todo 对于小图和大图同时检测出来，以大图为准，小图和大图矛盾，取大图的结果
    #
    #     pass

    # ------------------------------------------------------------------------------------------------------------------
    # @staticmethod
    # def draw_dete_res(dete_res, img_path, save_path, line_thickness=2, color_dict=None):
    #     """在图像上画出检测的结果"""
    #     # 初始化颜色字典
    #     if color_dict is None:
    #         color_dict = {}
    #     # 支持传入矩阵和图片路径
    #     if isinstance(img_path, np.ndarray):
    #         img = img_path
    #     else:
    #         img = cv2.imdecode(np.fromfile(img_path, dtype=np.uint8), 1)
    #
    #     # 每种标签使用不同的颜色
    #     for each_res in dete_res:
    #         #
    #         if each_res.tag in color_dict:
    #             each_color = color_dict[each_res.tag]
    #         else:
    #             each_color = [random.randint(0, 255), random.randint(0,255), random.randint(0, 255)]
    #             color_dict[each_res.tag] = each_color
    #         # --------------------------------------------------------------------------
    #         tl = line_thickness or int(round(0.001 * max(img.shape[0:2])))
    #         c1, c2 =(each_res.x1, each_res.y1), (each_res.x2, each_res.y2)
    #         # --------------------------------------------------------------------------
    #         # 画矩形
    #         cv2.rectangle(img, (each_res.x1, each_res.y1), (each_res.x2, each_res.y2), color=each_color, thickness=tl)
    #         # 打标签
    #         tf = max(tl - 2, 1)  # font thickness
    #         s_size = cv2.getTextSize(str('{:.0%}'.format(each_res.conf)), 0, fontScale=float(tl) / 3, thickness=tf)[0]
    #         t_size = cv2.getTextSize(each_res.tag, 0, fontScale=float(tl) / 3, thickness=tf)[0]
    #         c2 = c1[0] + t_size[0] + s_size[0] + 15, c1[1] - t_size[1] - 3
    #         cv2.rectangle(img, c1, c2, each_color, -1)  # filled
    #         cv2.putText(img, '{}: {:.0%}'.format(each_res.tag, each_res.conf), (c1[0], c1[1] - 2), 0, float(tl) / 3, [0, 0, 0], thickness=tf, lineType=cv2.FONT_HERSHEY_SIMPLEX)
    #     # 保存图片，解决保存中文乱码问题
    #     cv2.imencode('.jpg', img)[1].tofile(save_path)
    #     return color_dict
    #
    # @staticmethod
    # def draw_xml_dete_res_to_img(img_path, xml_path, save_path, color_dict=None):
    #     """将得到的以 xml 形式保存的检测结果画到图像上"""
    #     # 解析 xml 拿到框
    #     xml_info = parse_xml(xml_path)
    #     # 从 xml 中拿到 dete res 结果
    #     dete_res = []
    #     for each_obj in xml_info["object"]:
    #         each_dete_res = DeteObj()
    #         each_dete_res.conf = float(each_obj["prob"])
    #         each_dete_res.x1 = int(each_obj["bndbox"]["xmin"])
    #         each_dete_res.y1 = int(each_obj["bndbox"]["ymin"])
    #         each_dete_res.x2 = int(each_obj["bndbox"]["xmax"])
    #         each_dete_res.y2 = int(each_obj["bndbox"]["ymax"])
    #         each_dete_res.tag = each_obj["name"]
    #         dete_res.append(each_dete_res)
    #     # 进行最大值抑制，nms 操作，可以忽略或者不忽略相同的标签，这部分独立出去比较好
    #     # dete_res = TrickUtil.do_nms_for_res(dete_res, ignore_tag=True)
    #     # 画出结果
    #     TrickUtil.draw_dete_res(dete_res, img_path, save_path, color_dict=color_dict)

    # @staticmethod
    # def do_nms_for_dete_xml(xml_path, save_xml_path):
    #     """对检测结果的 xml 做一次 nms，并将结果保存为 xml """
    #     xml_parser = ParseXml()
    #     xml_info = xml_parser.get_xml_info(xml_path)
    #     # 从 xml 中拿到 dete res 结果
    #     dete_res = []
    #     for each_obj in xml_info["object"]:
    #         each_dete_res = DeteObj()
    #         each_dete_res.conf = float(each_obj["prob"])
    #         each_dete_res.x1 = int(each_obj["bndbox"]["xmin"])
    #         each_dete_res.y1 = int(each_obj["bndbox"]["ymin"])
    #         each_dete_res.x2 = int(each_obj["bndbox"]["xmax"])
    #         each_dete_res.y2 = int(each_obj["bndbox"]["ymax"])
    #         each_dete_res.tag = each_obj["name"]
    #         # fixme 对 conf 进行过滤，这部分后面需要删除
    #         if each_dete_res.conf < 0.9:
    #             continue
    #         dete_res.append(each_dete_res)
    #
    #     # 进行最大值抑制，nms 操作，可以忽略或者不忽略相同的标签
    #     if len(dete_res) > 0:
    #         dete_res = TrickUtil.do_nms_for_res(dete_res, ignore_tag=True)
    #     # 将做完 nms 的结果保存到 xml 中
    #     xml_info["object"] = []
    #     for each_dete_res in dete_res:
    #         each_obj = {}
    #         each_obj["name"] = each_dete_res.tag
    #         each_obj["prob"] = str(each_dete_res.conf)
    #         each_obj["bndbox"] = {}
    #         each_obj["bndbox"]["xmin"] = str(each_dete_res.x1)
    #         each_obj["bndbox"]["ymin"] = str(each_dete_res.y1)
    #         each_obj["bndbox"]["xmax"] = str(each_dete_res.x2)
    #         each_obj["bndbox"]["ymax"] = str(each_dete_res.y2)
    #         xml_info["object"].append(each_obj)
    #     # 将 xml 信息保存到 xml 中
    #     xml_parser.save_to_xml(save_xml_path, xml_info)

    # ------------------------------------------------------------------------------------------------------------------
    # @staticmethod
    # def check_diff_bt_dete(dete_res_1, dete_res_2):
    #     """比较两次检测结果的不一样的图，计算 iou 来算是不是一样，比较宽松"""
    #     pass



if __name__ == "__main__":

    # img = cv2.imdecode(np.fromfile(r"C:\Users\14271\Desktop\大图切小图\大图\test_0.jpg", dtype=np.uint8), 1)
    # imgMatList, imgLabelList = TrickUtil.cut_img_mat_to_small_memory(img, 3)
    #
    # for i in range(len(imgLabelList)):
    #     print(imgLabelList[i])
    #     print(imgMatList[i].shape)
    #     print("-"*50)

    # for each in res.items():
    #     print(each[0], each[1].shape)


    # TrickUtil.cut_img_to_small(r"C:\Users\14271\Desktop\大图切小图\大图\test_0.jpg", r"C:\Users\14271\Desktop\大图切小图\小图", cut_num=4)

    # xml_path_list = FileOperationUtil.re_all_file(r"C:\Users\14271\Desktop\大图切小图\result\test_1", lambda x:str(x).endswith('.xml'))
    #
    # TrickUtil.get_merge_xml_info_from_xml_list(xml_path_list, 123)

    # dete_res_list = []
    # for i in range(100):
    #     dete_res_list.append(DeteRes(conf=random.random(), tag=random.choice(["a", "b", "c", "d"]), x1=random.randint(10, 100),
    #                                  x2=random.randint(100, 300), y1=random.randint(10, 100), y2=random.randint(100, 300)))
    #
    # TrickUtil.do_nms_for_res(dete_res_list)

    # todo 保存结果中文出现异常，应该是编码问题

    # color_dict = {"Fnormal":(0, 255, 0), "fzc_broken":(0, 0, 255)}
    color_dict = {"K":(0, 0, 255), "Xnormal":(0, 255, 0), "Lm":(255, 0, 0)}
    # for xml_path in FileOperationUtil.re_all_file(r"C:\Users\14271\Desktop\result", lambda x:str(x).endswith((".xml"))):
    #     save_path = os.path.join(r"C:\data\fzc_优化相关资料\防振锤优化\110_使用裁切小图的方式进行优化\阈值 0.9\xml", os.path.split(xml_path)[1])
    #     TrickUtil.do_nms_for_dete_xml(xml_path, save_path)
    #

    img_dir = r"C:\Users\14271\Desktop\优化开口销第二步\000_标准测试集\内蒙-南平【标准】Lm3cls测试集\NM_standerd_pic"
    xml_dir = r"C:\Users\14271\Desktop\优化开口销第二步\003_检测结果\result_faster"
    save_dir = r"C:\Users\14271\Desktop\优化开口销第二步\003_检测结果\result_faster"

    for index, xml_path in enumerate(FileOperationUtil.re_all_file(xml_dir, lambda x:str(x).endswith((".xml")))):
        print(index, " : ", xml_path)
        img_path = os.path.join(img_dir, os.path.split(xml_path)[1][:-4] + '.jpg')

        if not os.path.exists(img_path):
            continue

        save_path = os.path.join(save_dir, os.path.split(img_path)[1])
        TrickUtil.draw_xml_dete_res_to_img(img_path, xml_path, save_path, color_dict=color_dict)



