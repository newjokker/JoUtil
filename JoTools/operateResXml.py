# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import os
import time
import numpy as np
import prettytable
from .txkj.parseXml import ParseXml, parse_xml
from .utils.FileOperationUtil import FileOperationUtil
import matplotlib.pyplot as plt
from progress.bar import Bar
import progressbar


class OperateResXml(object):
    """用于统计和处理结果 xml 中的信息"""

    # ------------------------------------------ 展示 ------------------------------------------------------------------
    @staticmethod
    def show_class_count(xml_folder, conf_func=lambda x:float(x)>-2):
        """查看 voc xml 的标签"""
        xml_info, name_dict = [], {}
        # 遍历 xml 统计 xml 信息
        xml_list = FileOperationUtil.re_all_file(xml_folder, lambda x: str(x).endswith('.xml'))
        # 进度条
        pb = progressbar.ProgressBar(len(xml_list)).start()
        #
        for xml_index, each_xml_path in enumerate(xml_list):
            pb.update(xml_index)
            each_xml_info = parse_xml(each_xml_path)
            xml_info.append(each_xml_info)
            for each in each_xml_info['object']:
                if each['name'] not in name_dict:
                    # 对置信度进行过滤
                    if conf_func(each['prob']):
                        name_dict[each['name']] = 1
                else:
                    if conf_func(each['prob']):
                        name_dict[each['name']] += 1
        # 结束进度条
        pb.finish()
        # 将找到的信息用表格输出
        tb = prettytable.PrettyTable()
        tb.field_names = ['class', 'count']
        for each in sorted(name_dict.items(), key=lambda x: x[1]):
            tb.add_row(each)
        # 打印信息
        print(tb)

    @staticmethod
    def show_area_spread(xml_dir, assign_class=None):
        """看面积的分布，做一个面积统计直方图，按照中位数之类的，百分之十的大小，百分之二十的大小"""
        # fixme 已经在其他地方实现
        area_list = []
        for each_xml_path in FileOperationUtil.re_all_file(xml_dir, lambda x:str(x).endswith('.xml')):
            print(each_xml_path)
            xml_info = parse_xml(each_xml_path)
            for each_obj in xml_info["object"]:
                # 过滤掉非指定类型
                if assign_class is not None and each_obj["name"] != assign_class:
                    continue

                bndbox = each_obj['bndbox']
                width = int(bndbox['xmax']) - int(bndbox['xmin'])
                height = int(bndbox['ymax']) - int(bndbox['ymin'])
                area_list.append(width * height)

        area_array = np.array(area_list)
        # plt.hist(area_array, bins=30, range=[np.min(area_array), np.max(area_array)], density=True)
        print([np.min(area_array), np.max(area_array)])
        plt.hist(area_array, bins=30, range=[np.min(area_array), np.max(area_array)])
        # 绘制网格线  看的比较清晰一些
        plt.ylabel("count")
        plt.xlabel("area")
        plt.grid()
        plt.show()

    # ------------------------------------------ 操作 ------------------------------------------------------------------
    @staticmethod
    def merge_class(xml_dir_path, merge_dict, save_folder=None):
        """合并 xml 中的类型，merge_dict = {'holder': 'fzc', 'single': 'fzc', 'fzc': 'fzc'}"""

        if save_folder is None:
            save_folder = xml_dir_path
        elif not os.path.exists(save_folder):
            os.makedirs(save_folder)
        #
        for each in FileOperationUtil.re_all_file(xml_dir_path, lambda x: str(x).endswith('.xml')):
            a = ParseXml()
            xml_info = a.get_xml_info(each)
            for each_object in xml_info['object']:
                # print(each_object)
                obj_name = each_object['name']
                if obj_name in merge_dict:
                    each_object['name'] = merge_dict[obj_name]
                else:
                    print("obj name : {0}".format(obj_name))
                    raise ValueError("obj name 不在 merge dict 中")

            save_path = os.path.join(save_folder, os.path.split(each)[1])
            a.save_to_xml(save_path, assign_xml_info=xml_info)

    @staticmethod
    def remove_no_need_class(xml_dir, save_xml_dir, need_obj_name_list=None, remobe_obj_name_list=[]):
        """去掉不需要的类别"""

        if not os.path.exists(save_xml_dir):
            os.makedirs(save_xml_dir)

        a = ParseXml()
        for each_xml_path in FileOperationUtil.re_all_file(xml_dir, lambda x: str(x).endswith('.xml')):
            xml_info = parse_xml(each_xml_path)
            new_objects = []
            for each_obj in xml_info['object']:

                if need_obj_name_list is None:
                    if each_obj['name'] not in remobe_obj_name_list:
                        new_objects.append(each_obj)
                else:
                    if each_obj['name'] in need_obj_name_list:
                        # if float(each_obj['difficult']) > assign_confidence:
                        new_objects.append(each_obj)

            # 没有 obj 不保存
            # if len(new_objects) == 0:
            #     print("* no object not save : {0}".format(save_path))
            #     continue

            xml_info['object'] = new_objects
            save_path = os.path.join(save_xml_dir, os.path.split(each_xml_path)[1])
            a.save_to_xml(save_path, assign_xml_info=xml_info)

    # todo 将一些操作移到这边来

























