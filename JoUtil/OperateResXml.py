# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import os
import time
import numpy as np
import prettytable
from JoUtil.DPTools.parseXml import parse_xml, ParseXml
from JoUtil.Report.FileOperationUtil import FileOperationUtil
import matplotlib.pyplot as plt
from progress.bar import Bar


class OperateResXml(object):
    """用于统计和处理结果 xml 中的信息"""

    # ------------------------------------------ 展示 ------------------------------------------------------------------
    @staticmethod
    def show_class_count(xml_folder):
        """查看 voc xml 的标签"""
        xml_info, name_dict = [], {}

        # 遍历 xml 统计 xml 信息
        for each_xml_path in FileOperationUtil.re_all_file(xml_folder, lambda x: str(x).endswith('.xml')):
            each_xml_info = parse_xml(each_xml_path)
            xml_info.append(each_xml_info)
            for each in each_xml_info['object']:
                if each['name'] not in name_dict:
                    name_dict[each['name']] = 1
                else:
                    name_dict[each['name']] += 1

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

        # for i in range(10, 100, 10):
        #     res = np.percentile(area_array, i, interpolation='midpoint')
        #     print(res)

        # todo 读取的时候增加进度条

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
    def remove_no_need_class(xml_dir, save_xml_dir, need_obj_name_list, assign_confidence=0.0):
        """去掉不需要的类别"""

        if not os.path.exists(save_xml_dir):
            os.makedirs(save_xml_dir)

        a = ParseXml()
        for each_xml_path in FileOperationUtil.re_all_file(xml_dir, lambda x:str(x).endswith('.xml')):
            xml_info = parse_xml(each_xml_path)
            new_objects = []
            for each_obj in xml_info['object']:
                if each_obj['name'] in need_obj_name_list:
                    # if float(each_obj['difficult']) > assign_confidence:
                    new_objects.append(each_obj)
            xml_info['object'] = new_objects
            save_path = os.path.join(save_xml_dir, os.path.split(each_xml_path)[1])
            a.save_to_xml(save_path, assign_xml_info=xml_info)

    # todo 裁剪小图到文件夹，实现裁剪一个小图即可


def test():
    bar = Bar('Processing', max=100, fill='#', suffix='%(percent)d%%')
    for i in range(100):
        time.sleep(0.1)
        bar.next()
    bar.finish()


if __name__ == "__main__":

    # a = progressbar.ProgressBar(100)
    #
    # a.start()
    #
    # for i in range(10):
    #     a.update(5)
    #
    # # for i in progressbar.ProgressBar(100):
    #     time.sleep(0.2)

    # import sys, time  # 调用sys模块，time模块
    #
    # print("test")
    #
    # sys.stdout.write("# ")
    # for i in range(20):  # 循环20次
    #     # sys.stdout.write('\033[41;1m.\033[0m')  # 背景色为红色的点
    #     sys.stdout.write('#')
    #     # todo 进度条后面显示已经完成的比例
    #     # print(sys.stdout.seek(i))
    #     sys.stdout.seek(i+1)
    #     sys.stdout.flush()  # 边输出边刷新
    #     time.sleep(0.1)
    #
    #
    # # test()
    #
    # exit()

    xml_dir = r"C:\Users\14271\Desktop\优化开口销第二步\003_检测结果\result_eff_0.15_71"

    OperateResXml.remove_no_need_class(xml_dir, xml_dir, need_obj_name_list=["K", "Lm", "Xnormal"])

    OperateResXml.show_class_count(xml_dir)

    # OperateResXml.show_area_spread(xml_dir, "Lm")























