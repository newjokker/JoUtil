# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import os
import copy
import random
import collections
from PIL import Image
import numpy as np
from .detectionResult import DeteRes, DeteObj
from .utils.FileOperationUtil import FileOperationUtil
from .txkj.parseXml import parse_xml, save_to_xml
import cv2
from .utils.NumberUtil import NumberUtil
import prettytable


# todo 重写 OperateDeteRes 中的函数，很多函数功能的实现已经移植到 DeteRes 类中了，使用调用里面的方法比较好

class OperateDeteRes(object):
    """基于检测结果的操作"""

    def __init__(self):
        self.label_list = ["Fnormal", "fzc_broken"]                                 # xml 中的分类
        self.iou_thershold = 0.4                                                   # 判定两矩形重合的 iou 阈值
        self.color_dict = {"extra":(0,0,255), "correct":(0,255,0), "mistake":(203,192,255), "miss":(0,255,255)}    # 颜色表

    @staticmethod
    def _cal_iou(dete_obj_1, dete_obj_2, ignore_tag=False):
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


    # ------------------------------------------- acc dete -------------------------------------------------------------
    @staticmethod
    def _update_check_res(res, each_res):
        """更新字典"""
        for each in each_res:
            if each in res:
                res[each] += each_res[each]
            else:
                res[each] = each_res[each]

    def compare_customer_and_standard(self, dete_res_standard, dete_res_customized, assign_img_path=None, save_path=None):
        """对比 两个 DeteRes 实例 之间的差异， 自己算出来的和标准数据集之间的差异"""
        check_res = []
        check_dict = collections.defaultdict(lambda: 0)
        # 对比标准数据集和找到的结果
        for obj_s in dete_res_standard.alarms:
            # 增加是否被检查出来，新属性
            if not hasattr(obj_s, "be_detect"):
                obj_s.be_detect = False

            for obj_c in dete_res_customized.alarms:
                # 增加一个新属性
                if not hasattr(obj_c, "is_correct"):
                    obj_c.is_correct = None

                # 当两个范围 iou 在一定范围内，认为识别正确，此时，给 customized 的 dete_obj 增加一个已被检测的标签
                if obj_c.is_correct is None:
                    each_iou = self._cal_iou(obj_s, obj_c, ignore_tag=True)
                    if each_iou >= self.iou_thershold:
                        if obj_s.tag == obj_c.tag:
                            obj_c.is_correct = True
                            obj_s.be_detect = True
                        else:
                            obj_c.is_correct = False
                            obj_c.correct_tag = obj_s.tag
                            obj_s.be_detect = True

        # 多检，正确，错检
        for obj_c in dete_res_customized.alarms:
            if not hasattr(obj_c, "is_correct") or obj_c.is_correct is None:
                new_tag = "extra_{0}".format(obj_c.tag)
                check_dict[new_tag] += 1
                if new_tag not in self.color_dict:
                    self.color_dict[new_tag] = self.color_dict["extra"]
                obj_c.tag = new_tag
            elif obj_c.is_correct is True:
                new_tag = "correct_{0}".format(obj_c.tag)
                check_dict[new_tag] += 1
                if new_tag not in self.color_dict:
                    self.color_dict[new_tag] = self.color_dict["correct"]
                obj_c.tag = new_tag
            elif obj_c.is_correct is False:
                new_tag = "mistake_{0}-{1}".format(obj_c.correct_tag, obj_c.tag)
                check_dict[new_tag] += 1
                # 每出现一种新类型，保持和 mistake 颜色一致
                if new_tag not in self.color_dict:
                    self.color_dict[new_tag] = self.color_dict["mistake"]
                obj_c.tag = new_tag
            else:
                raise ValueError("多余结果")
            check_res.append(obj_c)

        # 漏检
        for obj_s in dete_res_standard.alarms:
            if obj_s.be_detect is False:
                new_tag = "miss_{0}".format(obj_s.tag)
                check_dict[new_tag] += 1
                if new_tag not in self.color_dict:
                    self.color_dict[new_tag] = self.color_dict["miss"]
                obj_s.tag = new_tag
                check_res.append(obj_s)

        # 不画图直接返回对比统计结果
        if save_path is False or assign_img_path is None:
            return check_dict

        # 画图，并返回统计结果
        dete_res_standard.reset_alarms(check_res)
        if assign_img_path is not None:
            dete_res_standard.img_path = assign_img_path
        # 保存图片
        dete_res_standard.draw_dete_res(save_path, color_dict=self.color_dict)
        # 保存 xml
        save_xml_path = save_path[:-4] + '.xml'
        dete_res_standard.save_to_xml(save_xml_path)
        return check_dict

    def cal_model_acc(self, standard_xml_dir, customized_xml_dir, assign_img_dir, save_dir=None):
        """计算模型的性能，通过对比标准结果和跑出来的结果，save_dir 不为 None 就保存结果"""
        standard_xml_path_set = set(FileOperationUtil.re_all_file(standard_xml_dir, lambda x:str(x).endswith('.xml')))
        customized_xml_path_set = set(FileOperationUtil.re_all_file(customized_xml_dir, lambda x:str(x).endswith('.xml')))
        check_res = {}      # 检验结果
        # 对比
        for xml_path_s in standard_xml_path_set:
            print(xml_path_s)
            xml_name = os.path.split(xml_path_s)[1]
            xml_path_c = os.path.join(customized_xml_dir, xml_name)
            assign_img_path = os.path.join(assign_img_dir, xml_name[:-3] + 'jpg')
            save_img_path = os.path.join(save_dir, xml_name[:-3] + 'jpg')

            # jpg 文件不存在就不进行画图了
            if not os.path.isfile(assign_img_path):
                # fixme 支持 jpg 和 JPG 两种格式
                assign_img_path = os.path.join(assign_img_dir, xml_name[:-3] + 'JPG')
                if not os.path.isfile(assign_img_path):
                    assign_img_path = None
                    save_img_path = None
            #
            if xml_path_c in customized_xml_path_set:
                # 对比两个结果的差异
                each_check_res = self.compare_customer_and_standard(DeteRes(xml_path_s), DeteRes(xml_path_c), assign_img_path=assign_img_path, save_path=save_img_path)
                # 对比完了之后在 customized_xml_path_set 中删除这个对比过的 xml 路径
                customized_xml_path_set.remove(xml_path_c)
            else:
                # 算作漏检，新建一个空的 customized_xml_path 放进去检查
                each_check_res = self.compare_customer_and_standard(DeteRes(xml_path_s), DeteRes(), assign_img_path=assign_img_path, save_path=save_img_path)
            # 更新统计字典
            self._update_check_res(check_res, each_check_res)

        # 剩下的都算多检
        for xml_path_c in customized_xml_path_set:
            xml_name = os.path.split(xml_path_c)[1]
            xml_path_c = os.path.join(customized_xml_dir, xml_name)
            assign_img_path = os.path.join(assign_img_dir, xml_name[:-3] + 'jpg')
            save_img_path = os.path.join(save_dir, xml_name[:-3] + 'jpg')
            # 不进行画图
            if not os.path.isfile(assign_img_path):
                assign_img_path = None
                save_img_path = None

            each_check_res = self.compare_customer_and_standard(DeteRes(), DeteRes(xml_path_c), assign_img_path=assign_img_path, save_path=save_img_path)
            self._update_check_res(check_res, each_check_res)

        return check_res
        # return self.cal_acc_rec(check_res)

    @staticmethod
    def cal_acc_rec(check_res, tag_list=None):
        """根据结果得到正确率和召回率"""
        res = {}
        extra_dict, miss_dict, correct_dict, mistake_dict = {}, {}, {}, {}
        # 获得字典
        for each_key in check_res:
            if str(each_key).startswith('extra_'):
                new_key = each_key.lstrip('extra_')
                extra_dict[new_key] = check_res[each_key]
            elif str(each_key).startswith('correct_'):
                new_key = each_key.lstrip('correct_')
                correct_dict[new_key] = check_res[each_key]
            elif str(each_key).startswith('miss_'):
                new_key = each_key.lstrip('miss_')
                miss_dict[new_key] = check_res[each_key]
            elif str(each_key).startswith('mistake_'):
                new_key = each_key.lstrip('mistake_')
                mistake_dict[new_key] = check_res[each_key]
        # 计算准确率和召回率
        # 准确率，预测为正样本的有多少正样本 correct_a / (correct_a + mistake_x_a + extra_a)
        # 召回率：是针对我们原来的样本而言的，它表示的是样本中的正例有多少被预测正确了
        if tag_list is None:
            tag_list = list(correct_dict.keys())
        #
        for each_tag in tag_list:
            each_mistake_num = 0
            each_correct_num = 0
            each_extra_num = 0
            each_miss_num = 0
            #
            if each_tag in correct_dict:
                each_correct_num = correct_dict[each_tag]
            if each_tag in extra_dict:
                each_extra_num = extra_dict[each_tag]
            if each_tag in miss_dict:
                each_miss_num = miss_dict[each_tag]
            # 计算错检数
            for each_mistake_tag in mistake_dict:
                each_from, each_to = each_mistake_tag.split('-')
                if each_to == each_tag:
                    each_mistake_num += mistake_dict[each_mistake_tag]
            # 计算准确率和召回率
            if float(sum([each_correct_num, each_mistake_num, each_extra_num])) != 0:
                each_acc = each_correct_num / float(sum([each_correct_num, each_mistake_num, each_extra_num]))
            else:
                each_acc = -1
            if float(sum([each_correct_num, each_miss_num])) != 0:
                each_rec = each_correct_num / float(sum([each_correct_num, each_miss_num]))
            else:
                each_rec = -1
            #
            res[each_tag] = {'acc':each_acc, 'rec':each_rec}
        return res

    # ------------------------------------------- acc classify ---------------------------------------------------------
    @staticmethod
    def cal_acc_classify(standard_img_dir, customized_img_dir):
        """"对比两个分类结果文件夹，分类就是将原图进行了重新的排列"""

        # 拿到标签
        return_res = []
        standard_dict = {}
        stand_label_count = {}
        res_dict = {}
        for each_img_path in FileOperationUtil.re_all_file(standard_img_dir, lambda x:str(x).endswith(('.jpg', '.JPG', '.png'))):
            # 拿到第一级别文件夹名，作为 label
            img_label = each_img_path[len(standard_img_dir):].strip(os.sep).split(os.sep)[0]
            img_name = os.path.split(each_img_path)[1]
            standard_dict[img_name] = img_label
            if img_label in stand_label_count:
                stand_label_count[img_label] += 1
            else:
                stand_label_count[img_label] = 1
        #
        for each_img_path in FileOperationUtil.re_all_file(customized_img_dir, lambda x:str(x).endswith(('.jpg', '.JPG', '.png'))):
            # 拿到第一级别文件夹名，作为 label
            img_label = each_img_path[len(customized_img_dir):].strip(os.sep).split(os.sep)[0]
            img_name = os.path.split(each_img_path)[1]
            #
            standard_img_label = standard_dict[img_name]
            #
            if standard_img_label == img_label:
                correct_str = "correct_{0}".format(standard_img_label)
                if correct_str in res_dict:
                    res_dict[correct_str].append(each_img_path)
                else:
                    res_dict[correct_str] = [each_img_path]
            else:
                mistake_str = "mistake_{0}_{1}".format(standard_img_label, img_label)
                if mistake_str in res_dict:
                    res_dict[mistake_str].append(each_img_path)
                else:
                    res_dict[mistake_str] = [each_img_path]

        stand_label_list = list(stand_label_count.keys())
        tb = prettytable.PrettyTable()
        tb.field_names = ["  ", "class", "num", "per"]

        # 计算每一个类型的召回率
        for each in stand_label_list:
            correct_str = "correct_{0}".format(each)
            if correct_str in res_dict:
                # print(correct_str, len(res_dict[correct_str]), NumberUtil.format_float(len(res_dict[correct_str])/stand_label_count[each], 2))
                rec = NumberUtil.format_float(len(res_dict[correct_str])/stand_label_count[each], 2)
                one_row = ['rec', each, "{0} | {1}".format(len(res_dict[correct_str]), stand_label_count[each]), rec]
                tb.add_row(one_row)
                return_res.append(one_row)

        # 计算每一个类型的准确率
        for i in stand_label_list:
            correct_str = "correct_{0}".format(i)
            # 去掉没检测出来的类型
            if correct_str not in res_dict:
                continue
            #
            correct_num = len(res_dict[correct_str])
            all_num = correct_num
            for j in stand_label_list:
                mistake_str = "mistake_{0}_{1}".format(j, i)
                if mistake_str in res_dict:
                    all_num += len(res_dict[mistake_str])
            # print("rec {0} : {1}".format(i, NumberUtil.format_float(correct_num/all_num), 2))
            acc = NumberUtil.format_float(correct_num/all_num, 2)
            one_row = ['acc', i, "{0} | {1}".format(correct_num, all_num), acc]
            tb.add_row(one_row)
            return_res.append(one_row)

        mistake_tb = prettytable.PrettyTable()
        mistake_tb.field_names = ["correct", "mistake", "num"]

        for i in stand_label_list:
            for j in stand_label_list:
                mistake_str = "mistake_{0}_{1}".format(i, j)
                if mistake_str in res_dict:
                    # print(mistake_str, len(res_dict[mistake_str]))
                    mistake_tb.add_row([i, j, len(res_dict[mistake_str])])

        print(tb)
        print(mistake_tb)
        return return_res


    # ------------------------------------------- filter ---------------------------------------------------------------

    @staticmethod
    def filter_by_area_ratio(xml_dir, area_ratio_threshold=0.0006, save_dir=None):
        """根据面积比例阈值进行筛选"""
        for each_xml_path in FileOperationUtil.re_all_file(xml_dir, lambda x: str(x).endswith(".xml")):
            a = DeteRes(each_xml_path)
            a.filter_by_area_ratio(area_ratio_threshold)
            if save_dir is None:
                os.remove(each_xml_path)
                a.save_to_xml(each_xml_path)
            else:
                new_save_xml = os.path.join(save_dir, os.path.split(each_xml_path)[1])
                a.save_to_xml(new_save_xml)

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def _get_loc_list(img_name):
        """提取截图中的图片位置"""
        loc_str = ""
        start = False
        #
        for each_i in img_name[::-1]:
            #
            if start is True:
                loc_str += each_i

            if each_i == ']':
                start = True
            elif each_i == '[':
                break

        loc_list = loc_str[::-1].strip('[]').split("_")
        loc_list = list(map(lambda x: int(x), loc_list))
        return loc_list

    @staticmethod
    def _get_region_img_name(img_name):
        """找到原始的文件名"""
        a = str(img_name).find("-+-")
        return img_name[:a]

    @staticmethod
    def _get_crop_img_tag(img_name):
        """获取裁切小图的标签"""
        a = str(img_name).find("-+-")
        b = img_name[a + 3:]
        tag = b.split('_')[0]
        return tag

    @staticmethod
    def get_xml_from_crop_img(img_dir, region_img_dir, save_xml_dir=None):
        """从小图构建 xml，用于快速指定标签和核对问题，可以将 labelimg 设置为使用固定标签进行标注（等待修改）"""

        # todo 原先的标签和现在的标签不一致，就打印出内容

        if save_xml_dir is None:
            save_xml_dir = region_img_dir

        dete_res_dict = {}
        # 小截图信息获取
        for each_xml_path in FileOperationUtil.re_all_file(img_dir, lambda x: str(x).endswith('.jpg')):
            each_img_dir, img_name = os.path.split(each_xml_path)
            # 位置
            loc = OperateDeteRes._get_loc_list(img_name)
            # 原先的标签
            region_tag = OperateDeteRes._get_crop_img_tag(img_name)
            # 现在的标签
            each_tag = each_img_dir[len(img_dir) + 1:]
            # 原先的文件名
            region_img_name = OperateDeteRes._get_region_img_name(img_name)
            # 拿到最新的 tag 信息
            a = DeteObj(x1=loc[0], y1=loc[1], x2=loc[2], y2=loc[3], tag=each_tag)
            #
            if region_img_name in dete_res_dict:
                dete_res_dict[region_img_name].append(a)
            else:
                dete_res_dict[region_img_name] = [a]

        # 将小图信息合并为大图
        for each_img_name in dete_res_dict:
            region_img_path = os.path.join(region_img_dir, "{0}.jpg".format(each_img_name))

            # 去除找不到文件
            if not os.path.exists(region_img_path):
                continue

            # 保存文件
            a = DeteRes(assign_img_path=region_img_path)
            a.reset_alarms(dete_res_dict[each_img_name])
            xml_path = os.path.join(save_xml_dir, "{0}.xml".format(each_img_name))
            a.save_to_xml(xml_path)

    @staticmethod
    def crop_imgs(img_dir, xml_dir, save_dir, split_by_tag=False, exclude_tag_list=None):
        """将文件夹下面的所有 xml 进行裁剪"""
        # todo 增加裁剪指定类型
        index = 0
        for each_xml_path in FileOperationUtil.re_all_file(xml_dir, lambda x: str(x).endswith(".xml")):
            each_img_path = os.path.join(img_dir, os.path.split(each_xml_path)[1][:-3] + 'jpg')

            if not os.path.exists(each_img_path):
                continue

            print(index, each_xml_path)
            a = DeteRes(each_xml_path)
            a.img_path = each_img_path

            a.crop_and_save(save_dir, split_by_tag=split_by_tag, exclude_tag_list=exclude_tag_list)
            index += 1

    @staticmethod
    def get_class_count(xml_folder):
        """查看 voc xml 的标签"""
        xml_info, name_dict = [], {}
        # 遍历 xml 统计 xml 信息
        xml_list = FileOperationUtil.re_all_file(xml_folder, lambda x: str(x).endswith('.xml'))
        #
        for xml_index, each_xml_path in enumerate(xml_list):
            each_xml_info = parse_xml(each_xml_path)
            xml_info.append(each_xml_info)
            for each in each_xml_info['object']:
                if each['name'] not in name_dict:
                    name_dict[each['name']] = 1
                else:
                    name_dict[each['name']] += 1
        return name_dict

    @staticmethod
    def draw_tags(img_dir, xml_dir, save_dir, conf_threshold=None, color_dict=None):
        """将对应的 xml 和 img 进行画图"""
        index = 0

        if color_dict is None:
            color_dict = {}
            tag_count_dict = OperateDeteRes.get_class_count(xml_dir)
            print(tag_count_dict.keys())
            for each_tag in tag_count_dict:
                color_dict[each_tag] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]

        for each_xml_path in FileOperationUtil.re_all_file(xml_dir, lambda x: str(x).endswith(".xml")):
            each_img_name = os.path.split(each_xml_path)[1][:-3] + 'jpg'
            each_img_path = os.path.join(img_dir, each_img_name)
            each_save_img_path = os.path.join(save_dir, each_img_name)
            if not os.path.exists(each_img_path):
                continue

            print(index, each_xml_path)
            a = DeteRes(each_xml_path)
            a.img_path = each_img_path

            # 对重复标签进行处理
            a.do_nms(threshold=0.1, ignore_tag=True)
            # 置信度阈值过滤
            if conf_threshold is not None:
                a.filter_by_conf(conf_threshold)
            # 画出结果
            a.draw_dete_res(each_save_img_path, color_dict=color_dict)
            index += 1

    # ---------------------------------------------------- spared-------------------------------------------------------

    @staticmethod
    def get_area_speard(xml_dir, assign_pt=None):
        """获得面积的分布"""
        area_list = []
        # 遍历 xml 统计 xml 信息
        xml_list = FileOperationUtil.re_all_file(xml_dir, lambda x: str(x).endswith('.xml'))
        #
        for xml_index, each_xml_path in enumerate(xml_list):
            each_dete_res = DeteRes(each_xml_path)
            for each_dete_obj in each_dete_res.alarms:
                area_list.append(each_dete_obj.get_area())
        #
        if assign_pt:
            return np.percentile(area_list, assign_pt)
        else:
            for i in range(10, 95, 10):
                each_area = int(np.percentile(area_list, i))
                print("{0}% : {1}".format(i, each_area))

    # ----------------------------------------------------- 图像扩展 ----------------------------------------------------

    @staticmethod
    def get_subset_from_pic(xml_path, save_dir, assign_num):
        """从大图中扩展小图"""

        a = DeteRes(xml_path)
        pass

    # ------------------------------------------------------------------------------------------------------------------

    @staticmethod
    def update_tags(xml_dir, update_dict):
        """更新标签信息"""
        xml_list = FileOperationUtil.re_all_file(xml_dir, lambda x: str(x).endswith('.xml'))
        #
        for xml_index, each_xml_path in enumerate(xml_list):
            #
            each_dete_res = DeteRes(each_xml_path)
            each_dete_res.update_tags(update_dict)
            each_dete_res.save_to_xml(each_xml_path)


