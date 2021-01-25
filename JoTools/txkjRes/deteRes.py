# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import os
import cv2
import copy
import random
import numpy as np
from abc import ABC
from PIL import Image
from JoTools.utils.JsonUtil import JsonUtil
# from JoTools.txkj.parseXml import parse_xml, save_to_xml
from JoTools.txkjRes.deteAngleXml import parse_xml, save_to_xml
from .resBase import ResBase
from .deteObj import DeteObj
from .deteAngleObj import DeteAngleObj
from JoTools.txkjRes.resTools import ResTools


# todo save_to_json, save_to_xml ，是否直接改为 to_json，to_xml
# todo 添加 log 信息，
# todo 增加隐式的 try except 并记录报错信息


# todo 很多功能还不支持斜框的操作，比如 nms 之类的

class DeteRes(ResBase, ABC):
    """检测结果"""

    def __init__(self, xml_path=None, assign_img_path=None, json_dict=None, log=None):
        # 子类新方法需要放在前面
        self._alarms = []
        # todo 执行操作的时候自动记录操作状态和结果
        self._log = log
        super().__init__(xml_path, assign_img_path, json_dict)

    def _parse_xml_info(self):
        """解析 xml 中存储的检测结果"""
        xml_info = parse_xml(self.xml_path)
        #
        if 'size' in xml_info:
            if 'height' in xml_info['size']:
                self.height = float(xml_info['size']['height'])
            if 'width' in xml_info['size']:
                self.width = float(xml_info['size']['width'])
        #
        if 'filename' in xml_info:
            self.file_name = xml_info['filename']

        if 'folder' in xml_info:
            self.folder = xml_info['folder']

        # 解析 object 信息
        for each_obj in xml_info['object']:
            # bndbox
            if 'bndbox' in each_obj:
                bndbox = each_obj['bndbox']
                x_min, x_max, y_min, y_max = int(bndbox['xmin']), int(bndbox['xmax']), int(bndbox['ymin']), int(bndbox['ymax'])
                if 'prob' not in each_obj: each_obj['prob'] = -1
                if 'id' not in each_obj: each_obj['id'] = -1
                self.add_obj(x1=x_min, x2=x_max, y1=y_min, y2=y_max, tag=each_obj['name'], conf=each_obj['prob'], assign_id=each_obj['id'])
            # robndbox
            if 'robndbox' in each_obj:
                bndbox = each_obj['robndbox']
                cx, cy, w, h, angle = float(bndbox['cx']), float(bndbox['cy']), float(bndbox['w']), float(bndbox['h']), float(bndbox['angle'])
                if 'prob' not in each_obj: each_obj['prob'] = -1
                if 'id' not in each_obj: each_obj['id'] = -1
                self.add_angle_obj(cx, cy, w, h, angle, tag=each_obj['name'], conf=each_obj['prob'], assign_id=each_obj['id'])

    def _parse_json_info(self):
        """解析 json 信息"""

        json_info = self.json_dict

        if 'size' in json_info:
            json_info['size'] = JsonUtil.load_data_from_json_str(json_info['size'])
            if 'height' in json_info['size']:
                self.height = float(json_info['size']['height'])
            if 'width' in json_info['size']:
                self.width = float(json_info['size']['width'])
        #
        if 'filename' in json_info:
            self.file_name = json_info['filename']

        if 'path' in json_info:
            self.img_path = json_info['path']

        if 'folder' in json_info:
            self.folder = json_info['folder']

        # 解析 object 信息
        if 'object' in json_info:
            for each_obj in JsonUtil.load_data_from_json_str(json_info['object']):
                each_obj = JsonUtil.load_data_from_json_str(each_obj)
                # bndbox
                if 'bndbox' in each_obj:
                    bndbox = each_obj['bndbox']
                    x_min, x_max, y_min, y_max = int(bndbox['xmin']), int(bndbox['xmax']), int(bndbox['ymin']), int(bndbox['ymax'])
                    if 'prob' not in each_obj: each_obj['prob'] = -1
                    if 'id' not in each_obj: each_obj['id'] = -1
                    self.add_obj(x1=x_min, x2=x_max, y1=y_min, y2=y_max, tag=each_obj['name'], conf=each_obj['prob'], assign_id=each_obj['id'])
                # robndbox
                if 'robndbox' in each_obj:
                    bndbox = each_obj['robndbox']
                    cx, cy, w, h, angle = float(bndbox['cx']), float(bndbox['cy']), float(bndbox['w']), float(bndbox['h']), float(bndbox['angle'])
                    if 'prob' not in each_obj: each_obj['prob'] = -1
                    if 'id' not in each_obj: each_obj['id'] = -1
                    self.add_angle_obj(cx, cy, w, h, angle, tag=each_obj['name'], conf=each_obj['prob'],assign_id=each_obj['id'])

    # ------------------------------------------ common ----------------------------------------------------------------
    @property
    def alarms(self):
        """获取属性自动进行排序"""
        return sorted(self._alarms, key=lambda x:x.conf)

    @property
    def obj_count(self):
        """要素个数"""
        return len(self._alarms)

    def parse_img_info(self):
        """主动解析图像信息"""
        self._parse_img_info()

    def save_to_xml(self, save_path, assign_alarms=None):
        """保存为 xml 文件"""
        xml_info = {'size': {'height': str(self.height), 'width': str(self.width), 'depth': '3'},
                    'filename': self.file_name, 'path': self.img_path, 'object': [], 'folder': self.folder,
                    'segmented': "", 'source': ""}

        if assign_alarms is None:
            alarms = self._alarms
        else:
            alarms = assign_alarms
        #
        for each_dete_obj in alarms:
            # bndbox
            if isinstance(each_dete_obj, DeteObj):
                each_obj = {'name': each_dete_obj.tag, 'prob': str(each_dete_obj.conf), 'id':str(each_dete_obj.id),
                            'bndbox': {'xmin': str(each_dete_obj.x1), 'xmax': str(each_dete_obj.x2),
                                       'ymin': str(each_dete_obj.y1), 'ymax': str(each_dete_obj.y2)}}
                xml_info['object'].append(each_obj)
            # robndbox
            elif isinstance(each_dete_obj, DeteAngleObj):
                each_obj = {'name': each_dete_obj.tag, 'prob': str(each_dete_obj.conf), 'id': str(each_dete_obj.id),
                            'robndbox': {'cx': str(each_dete_obj.cx), 'cy': str(each_dete_obj.cy),
                                         'w': str(each_dete_obj.w), 'h': str(each_dete_obj.h),'angle': str(each_dete_obj.angle)}}
                xml_info['object'].append(each_obj)

        # 保存为 xml
        save_to_xml(xml_info, xml_path=save_path)

    def save_to_json(self, assign_alarms=None):
        """转为 json 结构"""

        json_dict = {'size': JsonUtil.save_data_to_json_str({'height': int(self.height), 'width': int(self.width), 'depth': '3'}),
                    'filename': self.file_name, 'path': self.img_path, 'object': [], 'folder': self.folder,
                    'segmented': "", 'source': ""}
        # 可以指定输出的 alarms
        if assign_alarms is None:
            alarms = self._alarms
        else:
            alarms = assign_alarms
        #
        json_object = []
        for each_dete_obj in alarms:
            # bndbox
            if isinstance(each_dete_obj, DeteObj):
                each_obj = {'name': each_dete_obj.tag, 'prob': float(each_dete_obj.conf), 'id':int(each_dete_obj.id),
                            'bndbox': {'xmin': int(each_dete_obj.x1), 'xmax': int(each_dete_obj.x2),
                                       'ymin': int(each_dete_obj.y1), 'ymax': int(each_dete_obj.y2)}}
                json_object.append(JsonUtil.save_data_to_json_str(each_obj))
            # robndbox
            elif isinstance(each_dete_obj, DeteAngleObj):
                each_obj = {'name': each_dete_obj.tag, 'prob': str(each_dete_obj.conf), 'id': str(each_dete_obj.id),
                            'robndbox': {'cx': float(each_dete_obj.cx), 'cy': float(each_dete_obj.cy),
                                         'w': float(each_dete_obj.w), 'h': float(each_dete_obj.h),
                                         'angle': float(each_dete_obj.angle)}}
                json_object.append(JsonUtil.save_data_to_json_str(each_obj))
        json_dict['object'] = JsonUtil.save_data_to_json_str(json_object)
        return json_dict

    def get_dete_obj_by_id(self, assign_id):
        """获取 id 对应的 deteObj 对象"""
        for each_dete_obj in self._alarms:
            if int(each_dete_obj.id) == int(assign_id):
                return each_dete_obj
        return None

    def get_id_list(self):
        """获取要素 id list，有时候会过滤掉一些 id 这时候按照 id 寻找就会有问题"""
        id_list = []
        for each_dete_obj in self._alarms:
            id_list.append(each_dete_obj.id)
        return id_list

    def refresh_obj_id(self):
        """跟新要素的 id，重新排列"""
        index = 0
        for each_dete_obj in self._alarms:
            each_dete_obj.id = index
            index += 1

    def get_sub_img_by_id(self, assign_id, augment_parameter=None):
        """根据指定 id 得到小图的矩阵数据"""
        assign_dete_res = self.get_dete_obj_by_id(assign_id=assign_id)

        if assign_dete_res is None:
            raise ValueError("assign id not exist")

        img = Image.open(self.img_path)
        if augment_parameter is None:
            crop_range = [assign_dete_res.x1, assign_dete_res.y1, assign_dete_res.x2, assign_dete_res.y2]
        else:
            crop_range = [assign_dete_res.x1, assign_dete_res.y1, assign_dete_res.x2, assign_dete_res.y2]
            crop_range = ResTools.region_augment(crop_range, [self.width, self.height], augment_parameter=augment_parameter)

        img_crop = img.crop(crop_range)
        return np.array(img_crop)

    def add_obj(self, x1, y1, x2, y2, tag, conf, assign_id=None):
        """快速增加一个检测框要素"""
        one_dete_obj = DeteObj(x1=x1, y1=y1, x2=x2, y2=y2, tag=tag, conf=conf, assign_id=assign_id)
        self._alarms.append(one_dete_obj)

    def add_angle_obj(self, cx, cy, w, h, angle, tag, conf, assign_id=None):
        """增加一个角度矩形对象"""
        one_dete_obj = DeteAngleObj(cx=cx, cy=cy, w=w, h=h, angle=angle, tag=tag, conf=conf, assign_id=assign_id)
        self._alarms.append(one_dete_obj)

    def draw_dete_res(self, save_path, line_thickness=2, color_dict=None):
        """在图像上画出检测的结果"""
        #
        if color_dict is None:
            color_dict = {}
        #
        img = cv2.imdecode(np.fromfile(self.img_path, dtype=np.uint8), 1)
        #
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
            # draw rectangle
            cv2.rectangle(img, (each_res.x1, each_res.y1), (each_res.x2, each_res.y2), color=each_color, thickness=tl)
            #
            tf = max(tl - 2, 1)  # font thickness
            s_size = cv2.getTextSize(str('{:.0%}'.format(each_res.conf)), 0, fontScale=float(tl) / 3, thickness=tf)[0]
            t_size = cv2.getTextSize(each_res.tag, 0, fontScale=float(tl) / 3, thickness=tf)[0]
            c2 = c1[0] + t_size[0] + s_size[0] + 15, c1[1] - t_size[1] - 3
            cv2.rectangle(img, c1, c2, each_color, -1)  # filled
            cv2.putText(img, '{}: {:.0%}'.format(each_res.tag, each_res.conf), (c1[0], c1[1] - 2), 0, float(tl) / 3, [0, 0, 0], thickness=tf, lineType=cv2.FONT_HERSHEY_SIMPLEX)
        # 保存图片，解决保存中文乱码问题
        cv2.imencode('.jpg', img)[1].tofile(save_path)
        return color_dict

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
                if ResTools.cal_iou(each, each_res, ignore_tag=ignore_tag) > threshold:
                    is_add = False
                    break
            # 如果判断需要添加到结果中
            if is_add is True:
                res.append(each_res)
        self._alarms = res

    def filter_by_area(self, area_th):
        """根据面积大小（像素个数）进行筛选"""
        new_alarms = []
        for each_dete_res in self._alarms:
            if each_dete_res.get_area() >= area_th:
                new_alarms.append(each_dete_res)
        self._alarms = new_alarms

    def filter_by_tages(self, need_tag=None, remove_tag=None):
        """根据 tag 类型进行筛选"""
        new_alarms = []

        if (need_tag is not None and remove_tag is not None) or (need_tag is None and remove_tag is None):
            raise ValueError(" need tag and remove tag cant be None or not None in the same time")

        if isinstance(need_tag, str) or isinstance(remove_tag, str):
            raise ValueError("need list tuple or set not str")

        if need_tag is not None:
            need_tag = set(need_tag)
            for each_dete_res in self._alarms:
                if each_dete_res.tag in need_tag:
                    new_alarms.append(each_dete_res)
        else:
            remove_tag = set(remove_tag)
            for each_dete_res in self._alarms:
                if each_dete_res.tag not in remove_tag:
                    new_alarms.append(each_dete_res)
        self._alarms = new_alarms

    def filter_by_conf(self, conf_th, assign_tag_list=None):
        """根据置信度进行筛选，指定标签就能对不同标签使用不同的置信度"""
        new_alarms = []
        for each_dete_res in self._alarms:
            if assign_tag_list is not None:
                if each_dete_res.tag not in assign_tag_list:
                    new_alarms.append(each_dete_res)
                    continue
            if each_dete_res.conf >= conf_th:
                new_alarms.append(each_dete_res)
        self._alarms = new_alarms

    def do_fzc_format(self):
        """按照防振锤模型设定的输出格式进行格式化， [tag, index, int(x1), int(y1), int(x2), int(y2), str(score)]"""
        res_list = []
        index = 0
        # 遍历得到多有的
        for each_res in self._alarms:
            # res_list.append([each_res.tag, index, each_res.x1, each_res.y1, each_res.x2, each_res.y2, str(each_res.conf)])
            res_list.append([each_res.tag, each_res.id, each_res.x1, each_res.y1, each_res.x2, each_res.y2, str(each_res.conf)])
            index += 1
        return res_list

    # ------------------------------------------ common test -----------------------------------------------------------

    def add_obj_2(self, one_dete_obj):
        """增加一个检测框"""
        self._alarms.append(one_dete_obj)

    def crop_and_save(self, save_dir, augment_parameter=None, method=None, exclude_tag_list=None, split_by_tag=False):
        """将指定的类型的结果进行保存，可以只保存指定的类型，命名使用标准化的名字 fine_name + tag + index, 可指定是否对结果进行重采样，或做特定的转换，只要传入转换函数
        * augment_parameter = [0.5, 0.5, 0.2, 0.2]
        """
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
            # 图片扩展
            if augment_parameter is not None:
                bndbox = ResTools.region_augment(bndbox, [self.width, self.height], augment_parameter=augment_parameter)
                loc_str = "[{0}_{1}_{2}_{3}]".format(bndbox[0], bndbox[1], bndbox[2], bndbox[3])
            else:
                loc_str = "[{0}_{1}_{2}_{3}]".format(each_obj.x1, each_obj.y1, each_obj.x2, each_obj.y2)
            # 为了区分哪里是最新加上去的，使用特殊符号 -+- 用于标志
            if split_by_tag is True:
                each_save_dir = os.path.join(save_dir, each_obj.tag)
                if not os.path.exists(each_save_dir):
                    os.makedirs(each_save_dir)
            else:
                each_save_dir = save_dir

            each_save_path = os.path.join(each_save_dir, '{0}-+-{1}_{2}_{3}_{4}.jpg'.format(img_name, each_obj.tag, tag_count_dict[each_obj.tag], loc_str, each_obj.conf))
            each_crop = img.crop(bndbox)
            # 对截图的图片自定义操作, 可以指定缩放大小之类的
            if method is not None:
                each_crop = method(each_crop)
            # 保存截图
            each_crop.save(each_save_path, quality=95)

    def do_nms_in_assign_tags(self, tag_list, threshold=0.1):
        """在指定的 tags 之间进行 nms，其他类型的 tag 不受影响"""
        # 备份 alarms
        all_alarms = copy.deepcopy(self._alarms)
        # 拿到非指定 alarms
        self.filter_by_tages(remove_tag=tag_list)
        other_alarms = copy.deepcopy(self._alarms)
        # 拿到指定 alarms 进行 nms
        self.reset_alarms(all_alarms)
        self.filter_by_tages(need_tag=tag_list)
        self.do_nms(threshold, ignore_tag=True)
        # 添加其他类型
        for each_dete_obj in other_alarms:
            self._alarms.append(each_dete_obj)

    def filter_by_area_ratio(self, ar=0.0006):
        """根据面积比例进行删选"""
        # get area
        th_area = float(sel.width * self.height) * ar
        self.filter_by_area(area_th=th_area)

    def filter_by_func(self, func):
        """根据指定方法进行筛选"""
        new_alarms = []
        for each_dete_res in self._alarms:
            if func(each_dete_res):
                new_alarms.append(each_dete_res)
        self._alarms = new_alarms

    def format_check(self):
        """类型检查，规范类型"""
        self.height = int(self.height)
        self.width = int(self.width)
        # object 类型整理
        for each_alarm in self.alarms:
            each_alarm.format_check()

    def update_tags(self, update_dict):
        """更新标签"""
        # tag 不在不更新字典中的就不进行更新
        for each_dete_res in self._alarms:
            if each_dete_res.tag in update_dict:
                each_dete_res.tag = update_dict[each_dete_res.tag]

    def reset_alarms(self, assign_alarms):
        """重置 alarms"""
        self._alarms = assign_alarms

    def save_assign_range(self, assign_range, save_dir, save_name=None, iou_1=0.85):
        """保存指定范围，同时保存图片和 xml """
        x1, y1, x2, y2 = int(assign_range[0]),int(assign_range[1]),int(assign_range[2]),int(assign_range[3])
        assign_dete_obj = DeteObj(x1=x1, y1=y1, x2=x2, y2=y2, tag='None', conf=-1)

        offset_x, offset_y = -int(assign_range[0]), -int(assign_range[1])
        height, width = y2 - y1, x2 - x1

        new_alarms = []
        # 这边要是直接使用 .copy 的话，alarms 里面的内容还是会被改变的, list 的 .copy() 属于 shallow copy 是浅复制，对浅复制中的可变类型修改的时候原数据会受到影响，https://blog.csdn.net/u011995719/article/details/82911392
        for each_dete_obj in copy.deepcopy(self._alarms):
            # 计算重合度
            each_iou_1 = ResTools.cal_iou_1(each_dete_obj, assign_dete_obj, ignore_tag=True)
            if each_iou_1 > iou_1:
                # 对结果 xml 的范围进行调整
                each_dete_obj.do_offset(offset_x, offset_y)
                # 修正目标的范围
                if each_dete_obj.x1 < 0:
                    each_dete_obj.x1 = 0
                if each_dete_obj.y1 < 0:
                    each_dete_obj.y1 = 0
                if each_dete_obj.x2 > width:
                    each_dete_obj.x2 = width
                if each_dete_obj.y2 > height:
                    each_dete_obj.y2 = height
                #
                new_alarms.append(each_dete_obj)

        # 保存 xml
        if save_name is None:
            loc_str = "[{0}_{1}_{2}_{3}]".format(assign_range[0], assign_range[1], assign_range[2], assign_range[3])
            save_name = os.path.split(self.xml_path)[1].strip('.xml')+ '-+-' + loc_str

        xml_save_dir = os.path.join(save_dir, 'Annotations')
        img_save_dir = os.path.join(save_dir, 'JPEGImages')
        xml_save_path = os.path.join(xml_save_dir, save_name + '.xml')
        jpg_save_path = os.path.join(img_save_dir, save_name + '.jpg')
        if not os.path.exists(xml_save_dir):os.makedirs(xml_save_dir)
        if not os.path.exists(img_save_dir):os.makedirs(img_save_dir)
        #
        self.save_to_xml(xml_save_path, new_alarms)

        # 保存 jpg
        img = Image.open(self.img_path)
        crop = img.crop(assign_range)
        crop.save(jpg_save_path, quality=95)

    def get_max_range(self):
        """得到标签的最大范围"""
        # 拿到每一个标签的位置, 计算所有位置的最大值和最小值
        range_list = []
        for each_dete_obj in self._alarms:
            range_list.append(each_dete_obj.get_rectangle())
        return ResTools.merge_range_list(range_list)

    @staticmethod
    def get_region_xml_from_cut_xml(xml_path, save_dir, img_dir):
        """从裁剪后的 xml 得到之前的 xml，恢复文件名和 dete_obj 位置"""

        # fixme 未完全测试，需要进行改进，将长宽信息存入矩阵中，
        # fixme 需要获取原始图像的长宽，因为处理后的 xml 需要保留原始图像的长宽信息,或者直接读取图片得到长宽也行

        if not os.path.exists(xml_path):
            raise ValueError("xml path is not exists")

        xml_name = os.path.split(xml_path)[1][:-4]
        split_loc = xml_name.rfind("-+-")

        if split_loc == -1:
            raise ValueError("no loc info in xml name")

        region_name = xml_name[:split_loc]
        range_list = eval(','.join(xml_name[split_loc+3:].split('_')))
        off_x, off_y = range_list[0], range_list[1]
        # xml 位置恢复
        img_path = os.path.join(img_dir, region_name + '.JPG')
        img = Image.open(img_path)

        #
        a = DeteRes(xml_path)
        a.height, a.width = img.height, img.width
        for each_dete_obj  in a.alarms:
            each_dete_obj.do_offset(off_x, off_y)
        # 保存
        save_path = os.path.join(save_dir, region_name+'.xml')
        a.save_to_xml(save_path)

    def count_tags(self):
        """统计标签数"""
        tags_count = {}
        for each_dete_res in self._alarms:
            each_tag = each_dete_res.tag
            if each_tag in tags_count:
                tags_count[each_tag] += 1
            else:
                tags_count[each_tag] = 1
        return tags_count

    def angle_obj_to_obj(self):
        """将斜框全部转为正框"""
        new_alarms = []
        for each_obj in self._alarms:
            if isinstance(each_obj, DeteRes):
                new_alarms.append(each_obj)
            elif isinstance(each_obj, DeteAngleObj):
                each_obj = each_obj.to_dete_obj()
                new_alarms.append(each_obj)
        self._alarms = new_alarms