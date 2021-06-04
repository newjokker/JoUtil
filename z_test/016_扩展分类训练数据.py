# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import os
from JoTools.txkj.imageAugmentation import ImageAugmentation
from JoTools.utils.FileOperationUtil import FileOperationUtil
from JoTools.operateDeteRes import OperateDeteRes, OperateTrainData

img_dir = r"/home/ldq/001_train_data/fzc_step_1_5_20210601/origin"
OperateTrainData.augmente_classify_img(img_dir, expect_img_num=15000)

# todo 设定每一个小类扩展后的数目相等
# todo 设定子文件夹中的扩展后的数据相等
# todo 不删除训练文件，只对部分训练文件进行扩增
# todo 只能有两层文件夹，第一层文件夹中显示分类后的类型，第二层显示一个类型中包含的几个小类型的数据

# todo 设定每一个文件夹中最后扩展后的数目 img_count_dict = {}




# def augmente_classify_img(img_dir, expect_img_num=20000):
#     """扩展分类数据集, expect_img_num 每个子类的数据数目"""
#
#     """
#     数据必须按照一定的格式进行排序
#     * img_dir
#         * tag_a
#             * tag_a_1
#             * tag_a_2
#             * tag_a_3
#         * tag_b
#             * tag_b_1
#         * tag_c
#             * tag_c_1
#             * tag_c_2
#     """
#
#     img_count_dict = {}
#     augmente_index_dict = {}
#
#     # get img_count_dict
#     for each_dir in os.listdir(img_dir):
#         # class 1
#         tag_dir = os.path.join(img_dir, each_dir)
#         if not os.path.isdir(tag_dir):
#             continue
#         img_count_dict[each_dir] = {}
#         # class 2
#         for each_child_dir in os.listdir(tag_dir):
#             child_dir = os.path.join(tag_dir, each_child_dir)
#             if not os.path.isdir(child_dir):
#                 continue
#             # record
#             img_count_dict[each_dir][each_child_dir] = len(list(FileOperationUtil.re_all_file(child_dir, endswitch=['.jpg', '.JPG'])))
#
#     # get augmente_index_dict
#     for each_tag in img_count_dict:
#         child_dir_num = len(img_count_dict[each_tag])
#         for each_child in img_count_dict[each_tag]:
#             each_child_img_need_num = int(expect_img_num / child_dir_num)
#             each_child_real_num = img_count_dict[each_tag][each_child]
#             # augmente_index
#             augmente_index = each_child_img_need_num / each_child_real_num if (each_child_img_need_num > each_child_real_num) else None
#             each_img_dir = os.path.join(img_dir, each_tag, each_child)
#             augmente_index_dict[each_img_dir] = augmente_index
#             # print
#             print(each_tag, each_child, augmente_index)
#
#     # do augmente
#     for each_img_dir in augmente_index_dict:
#         # create new dir
#         augmente_dir = each_img_dir + "_augmente"
#         os.makedirs(augmente_dir, exist_ok=True)
#         #
#         imgs_list = FileOperationUtil.re_all_file(each_img_dir, endswitch=['.jpg', '.JPG'])
#         # if need augmente, augmente_index is not None
#         if augmente_index_dict[each_img_dir]:
#             a = ImageAugmentation(imgs_list, augmente_dir, prob=augmente_index_dict[each_img_dir] / 12)
#             # 只在原图上进行变换
#             a.mode = 0
#             a.do_process()
#             print(augmente_index_dict[each_img_dir], each_img_dir)


