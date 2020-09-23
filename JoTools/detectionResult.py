# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import os
import sys


# 没有下面三行代码，就会报错
# this_dir = os.path.dirname(__file__)
# lib_path = os.path.join(this_dir, '.')
# sys.path.insert(0, lib_path)

# 错误的原因是：在一个 py 文件中，运行代码和调用这个 py 文件 import 的内容不一样


from PIL import Image
import cv2
import numpy as np
import random
from .utils.FileOperationUtil import FileOperationUtil
from .txkj.parseXml import parse_xml, save_to_xml
import copy
import collections


"""
* 可用于中间结果，这样可以直接裁剪并保存，如何指定每一个裁剪保存的名字是一个关键
* 具有可扩展性，可以继承并丰富其中的内容
* xml_info 应该进行重写，不应该将结果放在字典中，而应该放在类中，这样编程比较方便，不容易出错
"""


class DeteObj(object):
    """检测结果的一个检测对象，就是一个矩形框对应的信息"""

    def __init__(self, x1=None, y1=None, x2=None, y2=None, tag=None, conf=None):
        self.conf = conf
        self.tag = tag
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

    def do_offset(self, offset_x, offset_y):
        """对结果进行偏移"""
        self.x1 += offset_x
        self.x2 += offset_x
        self.y1 += offset_y
        self.y2 += offset_y

    def get_rectangle(self):
        """获取矩形范围"""
        return [self.x1, self.y1, self.x2, self.y2]

    def get_format_list(self):
        """得到标准化的 list 主要用于打印"""
        return [str(self.tag), int(self.x1), int(self.y1), int(self.x2), int(self.y2), format(float(self.conf), '.4f')]


class DeteRes(object):
    """检测结果"""

    def __init__(self, xml_path=None, assign_img_path=None):
        self.height = ""            # 检测图像的高
        self.width = ""             # 检测图像的宽
        self.folder = ""            # 图像存在的文件夹
        self.file_name = ""         # 检测图像文件名
        self._alarms = []            # 这里面存储的是 DeteObj 对象
        self.img_path = ""          # 对应的原图的路径
        self.xml_path = xml_path    # 可以从 xml 中读取检测结果

        # 从 xml 中获取检测结果
        if self.xml_path is not None:
            self._parse_xml_info()

        # 因为文件名在 xml 中经常写错，所以还是要有一个地方输入正确的文件名的
        if assign_img_path is not None:
            self.img_path = assign_img_path

    def _parse_xml_info(self):
        """解析 xml 中存储的检测结果"""
        xml_info = parse_xml(self.xml_path)
        #
        self.height = xml_info['size']['height']
        self.width = xml_info['size']['width']
        self.file_name = xml_info['filename']
        self.img_path = xml_info['path']
        self.folder = xml_info['folder']

        # 解析 object 信息
        for each_obj in xml_info['object']:
            bndbox = each_obj['bndbox']
            x_min, x_max, y_min, y_max = int(bndbox['xmin']), int(bndbox['xmax']), int(bndbox['ymin']), int(bndbox['ymax'])
            if 'prob' not in each_obj:
                each_obj['prob'] = -1
            self.add_obj(x1=x_min, x2=x_max, y1=y_min, y2=y_max, tag=each_obj['name'], conf=float(each_obj['prob']))

    @staticmethod
    def _region_augment(region_rect, img_size, augment_parameter=None):
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

    @staticmethod
    def _cal_iou(dete_obj_1, dete_obj_2, ignore_tag=False):
        """计算两个检测结果相交程度, xmin, ymin, xmax, ymax，标签不同，检测结果相交为 0, ignore_tag 为 True 那么不同标签也计算 iou"""
        if dete_obj_1.tag != dete_obj_2.tag and ignore_tag is False:
            return 0
        else:
            dx = max(min(dete_obj_1.x2, dete_obj_2.x2) - max(dete_obj_1.x1, dete_obj_2.x1) + 1, 0)
            dy = max(min(dete_obj_1.y2, dete_obj_2.y2) - max(dete_obj_1.y1, dete_obj_2.y1) + 1, 0)
            overlap_area = dx * dy
            union_area = ((dete_obj_1.x2 - dete_obj_1.x1 + 1) * (dete_obj_1.y2 - dete_obj_1.y1 + 1) +
                          (dete_obj_2.x2 - dete_obj_2.x1 + 1) * (dete_obj_2.y2 - dete_obj_2.y1 + 1) - overlap_area)
            return overlap_area * 1. / union_area

    # ------------------------------------------ 常用功能  -------------------------------------------------------------

    def add_obj(self, x1, y1, x2, y2, tag, conf):
        """快速增加一个检测框要素"""
        one_dete_obj = DeteObj(x1=x1, y1=y1, x2=x2, y2=y2, tag=tag, conf=conf)
        self._alarms.append(one_dete_obj)

    def draw_dete_res(self, save_path, line_thickness=2, color_dict=None):
        """在图像上画出检测的结果"""
        # 初始化颜色字典
        if color_dict is None:
            color_dict = {}
        # 支持传入矩阵和图片路径

        img = cv2.imdecode(np.fromfile(self.img_path, dtype=np.uint8), 1)

        # 每种标签使用不同的颜色
        for each_res in self._alarms:
            #
            if each_res.tag in color_dict:
                each_color = color_dict[each_res.tag]
            else:
                each_color = [random.randint(0, 255), random.randint(0,255), random.randint(0, 255)]
                color_dict[each_res.tag] = each_color
            # --------------------------------------------------------------------------
            tl = line_thickness or int(round(0.001 * max(img.shape[0:2])))
            c1, c2 =(each_res.x1, each_res.y1), (each_res.x2, each_res.y2)
            # --------------------------------------------------------------------------
            # 画矩形
            cv2.rectangle(img, (each_res.x1, each_res.y1), (each_res.x2, each_res.y2), color=each_color, thickness=tl)
            # 打标签
            tf = max(tl - 2, 1)  # font thickness
            s_size = cv2.getTextSize(str('{:.0%}'.format(each_res.conf)), 0, fontScale=float(tl) / 3, thickness=tf)[0]
            t_size = cv2.getTextSize(each_res.tag, 0, fontScale=float(tl) / 3, thickness=tf)[0]
            c2 = c1[0] + t_size[0] + s_size[0] + 15, c1[1] - t_size[1] - 3
            cv2.rectangle(img, c1, c2, each_color, -1)  # filled
            cv2.putText(img, '{}: {:.0%}'.format(each_res.tag, each_res.conf), (c1[0], c1[1] - 2), 0, float(tl) / 3, [0, 0, 0], thickness=tf, lineType=cv2.FONT_HERSHEY_SIMPLEX)
        # 保存图片，解决保存中文乱码问题
        cv2.imencode('.jpg', img)[1].tofile(save_path)
        return color_dict

    def crop_and_save(self, save_dir, augment_parameter=None, method=None, exclude_tag_list=None):
        """将指定的类型的结果进行保存，可以只保存指定的类型，命名使用标准化的名字 fine_name + tag + index, 可指定是否对结果进行重采样，或做特定的转换，只要传入转换函数"""
        img = Image.open(self.img_path)
        img_name = os.path.split(self.img_path)[1][:-4]
        tag_count_dict = {}
        #
        for each_obj in self._alarms:
            # 截图的区域
            bndbox = [each_obj.x1, each_obj.y1, each_obj.x2, each_obj.y2]
            # 排除掉不需要保存的 tag
            if not exclude_tag_list is None:
                if each_obj.tag in exclude_tag_list:
                    continue
            # 计算这是当前 tag 的第几个图片
            if each_obj.tag not in tag_count_dict:
                tag_count_dict[each_obj.tag] = 0
            else:
                tag_count_dict[each_obj.tag] += 1
            # 是否需要对图片进行扩展
            if augment_parameter is not None:
                bndbox = self._region_augment(bndbox, [self.width, self.height], augment_parameter=[0.5, 0.5, 0.2, 0.2])
            # 保存截图
            each_save_path = os.path.join(save_dir, '{0}_{1}_{2}.jpg'.format(img_name, each_obj.tag, tag_count_dict[each_obj.tag]))
            each_crop = img.crop(bndbox)
            # 对截图的图片自定义操作, 可以指定缩放大小之类的
            if method is not None:
                each_crop = method(each_crop)
            # 保存截图
            each_crop.save(each_save_path)

    def save_to_xml(self, save_path):
        """保存为 xml 文件"""
        xml_info = {}
        xml_info['size'] = {'height':str(self.height), 'width':str(self.width), 'depth':'3'}
        xml_info['filename'] = self.file_name
        xml_info['path'] = self.img_path
        xml_info['object'] = []
        xml_info['folder'] = self.folder
        # 两个无关但是必要的参数，是否需要将其在保存时候，设置默认值
        xml_info['segmented'] = ""
        xml_info['source'] = ""
        # 处理
        for each_dete_obj in self._alarms:
            each_obj = {}
            each_obj['name'] = each_dete_obj.tag
            each_obj['prob'] = str(each_dete_obj.conf)
            each_obj['bndbox'] = {'xmin':str(each_dete_obj.x1), 'xmax':str(each_dete_obj.x2),
                                  'ymin':str(each_dete_obj.y1), 'ymax':str(each_dete_obj.y2)}
            xml_info['object'].append(each_obj)
        # 保存为 xml
        save_to_xml(xml_info, xml_path=save_path)

    @property
    def alarms(self):
        """获取属性自动进行排序"""
        return sorted(self._alarms, key=lambda x:x.conf)

    def reset_alarms(self, assign_alarms):
        """重置 alarms"""
        self._alarms = assign_alarms
    # ------------------------------------------------------------------------------------------------------------------

    def do_nms(self, threshold=0.1, ignore_tag=False):
        """对结果做 nms 处理，"""
        # 参考：https://blog.csdn.net/shuzfan/article/details/52711706
        dete_res_list = copy.deepcopy(self._alarms)
        dete_res_list = sorted(dete_res_list, key=lambda x:x.conf, reverse=True)
        if len(dete_res_list) > 0:
            res = [dete_res_list.pop(0)]
        else:
            self._alarms = []
            return
        # 循环，直到 dete_res_list 中的数据被处理完
        while len(dete_res_list) > 0:
            each_res = dete_res_list.pop(0)
            is_add = True
            for each in res:
                # 计算每两个框之间的 iou，要是 nms 大于阈值，同时标签一致，去除置信度比较小的标签
                if self._cal_iou(each, each_res, ignore_tag=ignore_tag) > threshold:
                    is_add = False
                    break
            # 如果判断需要添加到结果中
            if is_add is True:
                res.append(each_res)
        self._alarms = res


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
                new_tag = "mistake_{0}_{1}".format(obj_c.correct_tag, obj_c.tag)
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
        dete_res_standard.draw_dete_res(save_path, color_dict=self.color_dict)
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



if __name__ == "__main__":

    # xml_info = parse_xml()
    #
    # a = DeteRes(r"C:\Users\14271\Desktop\del\test.xml")
    # a.img_path = r"C:\Users\14271\Desktop\del\test.jpg"
    #
    # # a.do_nms(threshold=0.1, ignore_tag=True)
    #
    # a.draw_dete_res(r"C:\Users\14271\Desktop\del\test_2.jpg")
    # a.crop_and_save(r"C:\Users\14271\Desktop\del\crop")
    # a.save_to_xml(r"C:\Users\14271\Desktop\del\test_new.xml")


    a = OperateDeteRes()

    check_res = a.cal_model_acc(r"C:\Users\14271\Desktop\优化开口销第二步\000_标准测试集\内蒙-南平【标准】Lm3cls测试集\NM_standerd_xml",
                    r"C:\Users\14271\Desktop\优化开口销第二步\003_检测结果\result_faster",
                    r"C:\Users\14271\Desktop\优化开口销第二步\000_标准测试集\内蒙-南平【标准】Lm3cls测试集\NM_standerd_pic",
                    r"C:\Users\14271\Desktop\save_res_2")

    print(check_res)

    # fixme 最后的检验结果是有问题的

    for each in check_res.items():
        print(each)

