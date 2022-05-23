# -*- coding: utf-8  -*-
# -*- author: jokker -*-

"""
* json 分析系统
* 分析 json 太慢了，最好分析基于 json 数据的 pkl 数据，
* 分析结果写到一个标准的 json 中，作为推荐结果的输入数据
* 所有的分析只在一次遍历中实现，不需要多次遍历 pkl 中的 json 信息

"""
import copy
import os
import numpy as np
import seaborn
import pandas
import matplotlib.pyplot as plt
from collections import Counter
from JoTools.utils.PickleUtil import PickleUtil
from JoTools.utils.FileOperationUtil import FileOperationUtil
from JoTools.utils.PrintUtil import PrintUtil
from JoTools.utils.JsonUtil import JsonUtil

# todo 将检测结果使用一个结构进行存储

# todo 检测 json 是否有问题的，出一份报告，比如 box 出到画面外

# todo 分析各个标签的迫切指数

# todo 根据指定条件进行分析，比如指定分析某几个标签之类的


class JsonAnalyse(object):
    """用作 json 分析的一个类"""

    def __init__(self, pkl_dir):
        self.pkl_dir = pkl_dir
        #
        self.uc_index = 0
        self.tag_counter = Counter()
        self.shape_type_counter = Counter()
        self.tag_count_distribute = Counter()
        self.has_label = Counter()
        self.recommend_index = Counter()
        # 中心点所在 block 位置
        self.block_xsize = 100
        self.block_ysize = 100
        self.loc_mat = np.zeros((self.block_xsize, self.block_ysize), dtype=np.int32)
        self.interval_count = 100000
        self.area_mat = np.zeros((self.interval_count), dtype=np.int32)
        # 指定分析其中的几个标签
        self.assign_analysis_tag_list = set()

    def get_tag_info_from_json_info(self, json_info):
        """从 json_info 中获取基础统计信息"""
        tag_list = []           # 每个标签的个数
        tag_type_list = []      # 每种标注类型的个数，斜框，矩形
        #
        for each_obj in json_info.objects:
            label = each_obj.label
            # 去掉不需要统计的标签
            if not (self.assign_analysis_tag_list is None or len(self.assign_analysis_tag_list) == 0 or label in self.assign_analysis_tag_list):
                continue
            #
            shape_type = each_obj.shape_type
            tag_list.append(label)
            tag_type_list.append(shape_type)
        # 是否标注
        if len(tag_list) == 0:
            self.has_label['no'] += 1
        else:
            self.has_label['yes'] += 1
        # 各标签的数目
        self.tag_counter += Counter(tag_list)
        # 各标签类型的数目
        self.shape_type_counter += Counter(tag_type_list)
        # 每个 json 中标签数目的分布
        self.tag_count_distribute[len(tag_list)] += 1

    def get_size_info_from_json_info(self, json_info):
        """从 json_info 中获取标签大小统计信息"""
        W, H = json_info.W, json_info.H
        for each_obj in json_info.objects:
            # 去掉不需要统计的标签
            label = each_obj.label
            if not (self.assign_analysis_tag_list is None or len(self.assign_analysis_tag_list) == 0 or label in self.assign_analysis_tag_list):
                continue

            if each_obj.shape_type == "rectangle":
                (x1, y1), (x2, y2) = each_obj.points
                w = x2 - x1
                h = y2 - y1
                cx = (w/2.0) + x1
                cy = (h/2.0) + y1
            elif each_obj.shape_type == "robndbox":
                cx, cy, w, h, angle = each_obj.points
            else:
                return

            try:
                self.loc_mat[int((cx / W) * self.block_xsize), int((cy / H) * self.block_ysize)] += 1
                area_ratio = (w * h) / (W * H)
                self.area_mat[int(area_ratio * self.interval_count)] += 1
                # self.area_list.append(area_ratio)
            except Exception as e:
                print("error")
                print(json_info.json_path)
                print(e)
                print('-'*20)

    def get_impendency_index(self, weight_dict):
        """计算迫切指数， 根据权重计算出来"""

        if len(self.tag_counter) == 0:
            self.analyse()

        tag_count = 0
        for each_tag in self.tag_counter:
            tag_count += self.tag_counter[each_tag]
        #
        for each_tag in self.tag_counter:
            if each_tag in weight_dict:
                self.recommend_index[each_tag] = (self.tag_counter[each_tag] / tag_count) * weight_dict[each_tag]
            else:
                self.recommend_index[each_tag] = (self.tag_counter[each_tag] / tag_count) * 1

    def analyse(self, print_res=False):
        # init
        self.uc_index = 0
        self.tag_counter = Counter()
        self.shape_type_counter = Counter()
        # 基础信息统计
        for pkl_index, each_pkl_path in enumerate(FileOperationUtil.re_all_file(self.pkl_dir, endswitch='.pkl')):
            print(pkl_index, each_pkl_path)
            pkl_info = PickleUtil.load_data_from_pickle_file(each_pkl_path)
            for each_uc in pkl_info:
                self.uc_index += 1
                json_info = pkl_info[each_uc]
                # get tag info
                self.get_tag_info_from_json_info(json_info)
                # get box info
                self.get_size_info_from_json_info(json_info)

        if print_res:
            PrintUtil.print(self.tag_counter)
            PrintUtil.print(self.shape_type_counter)
            PrintUtil.print(self.has_label)
            # PrintUtil.print(self.tag_count_distribute)
            print(f'json count : {self.uc_index}')

    def save_analyse_res(self, save_dir):
        """将检测结果输出为 json 文件"""

        self._save_json(save_dir)
        self._save_hetmap_loc_mat(save_dir)
        self._save_scatter_area_mat(save_dir)
        self._save_scatter_tag_count_distribute(save_dir, 30)

    def _save_json(self, save_dir):
        # json
        json_path = os.path.join(save_dir, "base.json")
        data = {'tag_counter': self.tag_counter, 'shape_type_counter':self.shape_type_counter,
                'tag_count_distribute':self.tag_count_distribute, 'has_label':self.has_label,
                'recommend_index':self.recommend_index}
        JsonUtil.save_data_to_json_file(data, json_path)

    def _save_hetmap_loc_mat(self, save_dir):
        # heatmap
        fig = seaborn.heatmap(self.loc_mat)
        heatmap = fig.get_figure()
        heat_map_path = os.path.join(save_dir, 'heatmap_obj_center.png')
        heatmap.savefig(heat_map_path, dpi=1000)

    def _save_scatter_area_mat(self, save_dir):
        save_scatter_dir = os.path.join(save_dir, "scatter_area_mat")
        os.makedirs(save_scatter_dir, exist_ok=True)
        a = zip(range(self.interval_count), self.area_mat)
        data = pandas.DataFrame(data=a, columns=['x','y'])
        step = int(self.interval_count/20)
        for i in range(step, self.interval_count, step):
            each_data = data[i-step:i]
            plt.figure(figsize=(50, 6))
            plt.xlabel('area ratio , /1000,000')
            plt.ylabel('point count')
            plt.tight_layout()
            plt.scatter(each_data['x'].tolist(), each_data['y'].tolist())
            plt.savefig(os.path.join(save_scatter_dir, f"scatter_{i}.png"), quality=100)
            plt.close()

    def _save_scatter_tag_count_distribute(self, save_dir, max_count=30):
        plt.figure(figsize=(50, 6))
        plt.xlabel('tag count')
        plt.ylabel('json count')
        plt.tight_layout()
        plt.scatter(self.tag_count_distribute.keys(), self.tag_count_distribute.values())
        save_path = os.path.join(save_dir, "tag_count_distribute.png")
        plt.savefig(save_path, quality=100)
        plt.close()
        # delete some data
        for each_key in copy.deepcopy(self.tag_count_distribute):
            if each_key > max_count:
                del self.tag_count_distribute[each_key]
        # save img after delete
        plt.figure(figsize=(30, 6))
        plt.xticks(range(max_count+1))
        plt.xlabel('tag count')
        plt.ylabel('json count')
        plt.tight_layout()
        plt.scatter(self.tag_count_distribute.keys(), self.tag_count_distribute.values())
        save_path = os.path.join(save_dir, f"tag_count_distribute_{max_count}.png")
        plt.savefig(save_path, quality=100)
        plt.close()





if __name__ == "__main__":


    # print(tag_counter)
    # print(shape_type_counter)

    # pkl 数据文件夹
    pklDir = r"C:\Users\14271\Desktop\del\buffer"
    save_res_dir = r"C:\Users\14271\Desktop\analyse_res"

    a = JsonAnalyse(pklDir)

    a.assign_analysis_tag_list = {'hat', 'person', 'long', 'short'}

    a.analyse(print_res=True)

    a.get_impendency_index(weight_dict={})

    a.save_analyse_res(save_res_dir)


