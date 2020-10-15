# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import os
import copy
import random
import math
import shutil
import numpy as np
import prettytable
from ..utils.JsonUtil import JsonUtil
from ..utils.CsvUtil import CsvUtil
from ..utils.ImageUtil import ImageUtil
from .parseXml import ParseXml, parse_xml
from ..utils.FileOperationUtil import FileOperationUtil
from PIL import Image

# 这里面核心函数就是对 Efficientdet 数据的支持，其他的都可以删掉，无所谓


class CocoDatabaseUtil(object):

    # ----------- 训练数据之间互转 ----------------

    @staticmethod
    def voc2coco(xml_dir, save_path, category_dict):
        """voc 转为 coco文件"""

        # 检查 category_dict 是否按照规范填写的
        for each in category_dict.values():
            if each == 0:
                raise ValueError("需要从 category_dict 的值 需要从 1 开始")

        coco_dict = {"info": {"description": "", "url": "", "version": "", "year": 2020, "contributor": "",
                              "data_created": "'2020-04-14 01:45:18.567988'"},
                     "licenses": [{"id": 1, "name": None, "url": None}],
                     "categories": [],
                     "images": [],
                     "annotations": []}

        # 加载分类信息
        for each_category in category_dict:
            categories_info = {"id": category_dict[each_category], "name": each_category, "supercategory": 'None'}
            coco_dict['categories'].append(categories_info)

        # 加载
        box_id = 0
        for index, each_xml_path in enumerate(FileOperationUtil.re_all_file(xml_dir, lambda x: str(x).endswith('.xml'))):
            xml_info = parse_xml(each_xml_path)
            each_image = {"id": index, "file_name": xml_info["filename"],
                          "width": int(float(xml_info["size"]["width"])),
                          "height": int(float(xml_info["size"]["height"]))}
            coco_dict['images'].append(each_image)
            for bndbox_info in xml_info["object"]:
                category_id = category_dict[bndbox_info['name']]
                each_box = bndbox_info['bndbox']
                bndbox = [float(each_box['xmin']), float(each_box['ymin']),
                          (float(each_box['xmax']) - float(each_box['xmin'])),
                          (float(each_box['ymax']) - float(each_box['ymin']))]
                area = bndbox[2] * bndbox[3]
                segmentation = [bndbox[0], bndbox[1], (bndbox[0] + bndbox[2]), bndbox[1], (bndbox[0] + bndbox[2]),
                                (bndbox[1] + bndbox[3]), bndbox[0], (bndbox[1] + bndbox[3])]
                each_annotations = {"id": box_id, "image_id": index, "category_id": category_id, "iscrowd": 0,
                                    "area": area, "bbox": bndbox, "segmentation": segmentation}
                coco_dict['annotations'].append(each_annotations)
                box_id += 1

        # 保存文件
        JsonUtil.save_data_to_json_file(coco_dict, save_path)

    @staticmethod
    def coco2voc(json_file_path, save_folder):
        """json文件转为xml文件"""

        if not os.path.exists(save_folder):
            os.makedirs(save_folder)

        json_info = JsonUtil.load_data_from_json_file(json_file_path)
        # 解析 categories，得到字典
        categorie_dict = {}
        for each_categorie in json_info["categories"]:
            categorie_dict[each_categorie['id']] = each_categorie['name']

        # 解析 image 信息
        image_dict = {}
        for each in json_info["images"]:
            id = each['id']
            file_name = each['file_name']
            width = each['width']
            height = each['height']
            image_dict[id] = {"filename": each['file_name'], 'object': [], "folder": "None", "path": "None",
                              "source": {"database": "Unknow"},
                              "segmented": "0", "size": {"width": str(width), "height": str(height), "depth": "3"}}

        # 解析 annotations 信息
        for each in json_info["annotations"]:
            image_id = each['image_id']
            category_id = each['category_id']
            each_name = categorie_dict[category_id]
            bbox = each["bbox"]
            bbox_dict = {"xmin": str(bbox[0]), "ymin": str(bbox[1]), "xmax": str(int(bbox[0]) + int(bbox[2])),
                         "ymax": str(int(bbox[1]) + int(bbox[3]))}
            object_info = {"name": each_name, "pose": "Unspecified", "truncated": "0", "difficult": "0",
                           "bndbox": bbox_dict}
            image_dict[image_id]["object"].append(object_info)

        # 将数据转为 xml
        aa = ParseXml()
        for each_img in image_dict.values():
            save_path = os.path.join(save_folder, each_img['filename'][:-3] + 'xml')
            aa.save_to_xml(save_path, each_img)

    @staticmethod
    def csv2voc(csv_path, save_folder):
        """csv 转为 voc 文件"""

        csv_info = CsvUtil.read_csv_to_list(csv_path)

        image_dict = {}

        for each in csv_info[1:]:
            image_id = each[0]
            bbox = each[3].strip("[]").split(',')
            bbox_dict = {"xmin": str(bbox[0]), "ymin": str(bbox[1]), "xmax": str(float(bbox[0]) + float(bbox[2])),
                         "ymax": str(float(bbox[1]) + float(bbox[3]))}
            object_info = {"name": "xiao_mai", "pose": "Unspecified", "truncated": "0", "difficult": "0",
                           "bndbox": bbox_dict}
            #
            if image_id not in image_dict:
                image_dict[image_id] = {}
                image_dict[image_id]["filename"] = "{0}.jpg".format(each[0])
                image_dict[image_id]["folder"] = "None"
                image_dict[image_id]["source"] = {"database": "Unknow"}
                image_dict[image_id]["path"] = "None"
                image_dict[image_id]["segmented"] = "0"
                image_dict[image_id]["size"] = {"width": str(each[1]), "height": str(each[2]), "depth": "3"}
                image_dict[image_id]['object'] = [object_info]
            else:
                image_dict[image_id]['object'].append(object_info)

        # 将数据转为 xml
        aa = ParseXml()
        for each_img in image_dict.values():
            save_path = os.path.join(save_folder, each_img['filename'][:-3] + 'xml')
            aa.save_to_xml(save_path, each_img)

    @staticmethod
    def voc2csv(xml_dir, save_csv_path):
        """voc xml 转为 csv 文件"""

        csv_list = []
        for each in FileOperationUtil.re_all_file(xml_dir, lambda x: str(x).endswith('.xml')):
            xml_info = parse_xml(each)
            a = xml_info['object']
            width = xml_info['size']['width']
            height = xml_info['size']['height']
            file_name = xml_info['filename'][:-4]
            #
            for each_box_info in xml_info['object']:
                each_class = each_box_info['name']
                each_box = each_box_info['bndbox']
                # fixme 这边对防振锤 box 做一下限定, x,y,w,h
                x, y, w, h = int(each_box['xmin']), int(each_box['ymin']), (
                            int(each_box['xmax']) - int(each_box['xmin'])), (
                                         int(each_box['ymax']) - int(each_box['ymin']))
                each_line = [file_name, width, height, [x, y, w, h], each_class]

                csv_list.append(each_line)

        CsvUtil.save_list_to_csv(csv_list, save_csv_path)

    # ----------- 图片转为 coco 数据样式 -----------

    @staticmethod
    def zoom_img_and_xml_to_square(img_path, xml_path, save_dir, assign_length_of_side=1536, assign_save_name=None):
        """将图像先填充为正方形，再将 xml 和 图像拉伸到指定长宽"""
        file_list = []
        img = ImageUtil(img_path)
        img_shape = img.get_img_shape()
        # 将图像填充为正方形
        img_mat = img.get_img_mat()
        length_of_side = max(img_shape[0], img_shape[1])
        new_img = np.ones((length_of_side, length_of_side, 4), dtype=np.uint8) * 127
        new_img[:img_shape[0], :img_shape[1], :] = img_mat
        img.set_img_mat(new_img)
        #
        img.convert_to_assign_shape((assign_length_of_side, assign_length_of_side))
        if assign_save_name is None:
            img_name = os.path.split(img_path)[1]
        else:
            img_name = assign_save_name + '.jpg'
        save_path = os.path.join(save_dir, img_name)
        img.save_to_image(save_path)
        file_list.append(save_path)
        # 读取 xml，xml 进行 resize 并保存
        img_shape = (length_of_side, length_of_side)  # 图像信息已经进行了更新
        xml = ParseXml()
        each_xml_info = xml.get_xml_info(xml_path)
        # 改变图片长宽
        each_xml_info['size'] = {'width': str(assign_length_of_side), 'height': str(assign_length_of_side), 'depth': '3'}
        each_xml_info["filename"] = img_name

        # 遍历每一个 object 改变其中的坐标
        for each_object in each_xml_info['object']:
            bndbox = each_object['bndbox']
            bndbox['xmin'] = str(int(float(bndbox['xmin']) / (img_shape[0] / assign_length_of_side)))
            bndbox['xmax'] = str(int(float(bndbox['xmax']) / (img_shape[0] / assign_length_of_side)))
            bndbox['ymin'] = str(int(float(bndbox['ymin']) / (img_shape[1] / assign_length_of_side)))
            bndbox['ymax'] = str(int(float(bndbox['ymax']) / (img_shape[1] / assign_length_of_side)))

        if assign_save_name is None:
            xml_name = os.path.split(xml_path)[1]
        else:
            xml_name = assign_save_name + '.xml'

        save_xml_path = os.path.join(save_dir, xml_name)
        xml.save_to_xml(save_xml_path)
        file_list.append(save_xml_path)
        return file_list

    @staticmethod
    def change_img_to_coco_format(img_folder, save_folder, assign_length_of_side=1536, xml_folder=None, val_train_ratio=0.1, category_dict=None, file_head=""):
        """将文件夹中的文件转为 coco 的样式，正方形，填充需要的部分, 将按照需要对文件进行重命名, file_head 文件的前缀"""
        if xml_folder is None:
            xml_folder = img_folder
        # 创建保存文件夹
        if not os.path.exists(save_folder):
            os.makedirs(save_folder)

        # 创建 train 和 val 文件夹
        train_dir = os.path.join(save_folder, "train")
        val_dir = os.path.join(save_folder, "val")
        annotations_dir = os.path.join(save_folder, "annotations")

        if not os.path.exists(train_dir):
            os.makedirs(train_dir)

        if not os.path.exists(val_dir):
            os.makedirs(val_dir)

        if not os.path.exists(annotations_dir):
            os.makedirs(annotations_dir)

        # 计算文件名的长度
        count = len(os.listdir(img_folder))
        o_count = int(math.log10(count)) + 1

        for index, each_img_name in enumerate(os.listdir(img_folder)):
            if not each_img_name.endswith('.jpg'):
                continue

            img_path = os.path.join(img_folder, each_img_name)
            xml_path = os.path.join(xml_folder, each_img_name[:-3] + 'xml')

            print("{0} : {1}".format(index, img_path))

            if not os.path.exists(xml_path):
                continue

            # 进行转换
            assign_save_name = file_head + str(index).rjust(o_count, "0")
            file_list = CocoDatabaseUtil.zoom_img_and_xml_to_square(img_path, xml_path, save_folder, assign_length_of_side, assign_save_name=assign_save_name)

            # 有一定的概率分配到两个文件夹之中
            if random.random() > val_train_ratio:
                traget_dir = train_dir
            else:
                traget_dir = val_dir

            for each_file_path in file_list:
                new_file_path = os.path.join(traget_dir, os.path.split(each_file_path)[1])
                shutil.move(each_file_path, new_file_path)

        # 将 xml 生成 json 文件，并存放到指定的文件夹中
        if category_dict is not None:
            save_train_path = os.path.join(annotations_dir, "instances_train.json")
            save_val_path = os.path.join(annotations_dir, "instances_val.json")
            CocoDatabaseUtil.voc2coco(train_dir, save_train_path, category_dict=category_dict)
            CocoDatabaseUtil.voc2coco(val_dir, save_val_path, category_dict=category_dict)
        else:
            print("未指定 category_dict 不进行 xml --> json 转换")

    # ----------- 查看 数据信息 -----------

    @staticmethod
    def show_voc_class_info(xml_folder):
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
    def filter_objs(obj_info):
        """进行 两个 single 一个 middle_pole 的过滤，有三个概率"""
        obj_dict = {"single":[], "middle_pole":[]}
        for each in obj_info:
            obj_dict[each['name']].append(float(each['difficult']))

        if len(obj_dict['middle_pole']) != 1:
            return False
        elif obj_dict['middle_pole'][0] < 0.7:
            return False
        elif len(obj_dict['single']) < 2:
            return False
        elif max(obj_dict['single']) < 0.7:
            return False
        elif min(obj_dict['single']) < 0.7:
            return False
        else:
            return True

    @staticmethod
    def find_broken_fzc(xml_dir, save_dir):
        """查看 obj 信息，名字，概率，"""
        pt = prettytable.PrettyTable()
        pt.field_names = ['name', 'probability']
        score_list = []

        # 生成保存文件夹
        true_dir = os.path.join(save_dir, "True")
        false_dir = os.path.join(save_dir, "False")
        if not os.path.exists(true_dir):
            os.makedirs(true_dir)
        if not os.path.exists(false_dir):
            os.makedirs(false_dir)

        # 遍历所有的 xml 文件
        all_xml_path_list = FileOperationUtil.re_all_file(xml_dir, lambda x:str(x).endswith('.xml'))
        for each_xml_path in all_xml_path_list:
            xml_info = parse_xml(each_xml_path)
            res = CocoDatabaseUtil.filter_objs(xml_info['object'])
            score_list.append(res)

            jpg_path = each_xml_path[:-3] + 'jpg'

            if not os.path.exists(jpg_path):
                continue

            if res is True:
                save_path = os.path.join(true_dir, os.path.split(jpg_path)[1])
            else:
                save_path = os.path.join(false_dir, os.path.split(jpg_path)[1])
            shutil.copy(jpg_path, save_path)

        print(np.sum(score_list)/float(len(score_list)))

    @staticmethod
    def merge_voc_class(xml_dir_path, merge_dict, save_folder=None):
        """合并 xml 中的类型"""

        if save_folder is None:
            save_folder = xml_dir_path
        elif not os.path.exists(save_folder):
            os.makedirs(save_folder)

        # merge_dict = {'holder': 'fzc', 'single': 'fzc', 'fzc': 'fzc',
        #               'ljj': 'ljj', 'xj': 'xj', 'other': 'other'}

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
    def find_imgs_which_have_xml(img_xml_path, save_path):
        """找到那些有对应 xml 的图片，与 xml 一起保存到指定位置"""
        for xml_index, each_xml_path in enumerate(FileOperationUtil.re_all_file(img_xml_path, lambda x:str(x).endswith('.xml'))):
            each_img_path = each_xml_path[:-3] + 'jpg'
            if not os.path.exists(each_img_path):
                continue
            # 复制对应文件到指定文件夹
            new_xml_path = os.path.join(save_path, os.path.split(each_xml_path)[1])
            new_img_path = os.path.join(save_path, os.path.split(each_img_path)[1])
            shutil.copyfile(each_xml_path, new_xml_path)
            shutil.copyfile(each_img_path, new_img_path)

            print("{0} : {1}".format(xml_index, each_xml_path))

    @staticmethod
    def show_area_spread(xml_dir):
        """看面积的分布，做一个面积统计直方图，按照中位数之类的，百分之十的大小，百分之二十的大小"""

        area_list = []
        for each_xml_path in FileOperationUtil.re_all_file(xml_dir, lambda x:str(x).endswith('.xml')):
            print(each_xml_path)
            xml_info = parse_xml(each_xml_path)
            for each_obj in xml_info["object"]:
                bndbox = each_obj['bndbox']
                width = int(bndbox['xmax']) - int(bndbox['xmin'])
                height = int(bndbox['ymax']) - int(bndbox['ymin'])
                area_list.append(width * height)

        print(len(area_list))

        area_array = np.array(area_list)

        for i in range(10, 100, 10):
            res = np.percentile(area_array, i, interpolation='midpoint')
            print(res)

        print("OK")

    @staticmethod
    def re_set_diffcult_info(xml_dir, save_dir):
        """重置 diffcult 信息"""
        a = ParseXml()
        for each_xml_path in FileOperationUtil.re_all_file(xml_dir, lambda x:str(x).endswith('.xml')):
            xml_info = parse_xml(each_xml_path)
            for each_obj in xml_info['object']:
                each_obj['difficult'] = '0'

            save_path = os.path.join(save_dir, os.path.split(each_xml_path)[1])
            a.save_to_xml(save_path, assign_xml_info=xml_info)

    # ----------- 分析结果数据 -----------

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

    @staticmethod
    def analyze_detection_res_in_every_section(xml_dir, img_dir, save_dir, section_list=None):
        """分析每个区间的数据的正确率，截图放到对应的文件夹里面"""

        # todo 需要把防振锤往外扩增，左右各扩 0.8，上下 扩 0.1

        if section_list is None:
            section_list = [0, 0.2, 0.4, 0.6, 0.8, 1]

        for i in range(len(section_list)-1):
            each_section = [section_list[i], section_list[i+1]]
            each_section_dir = os.path.join(save_dir, "{0}-{1}".format(each_section[0], each_section[1]))
            if not os.path.exists(each_section_dir):
                os.makedirs(each_section_dir)

        for index, each_xml_path in enumerate(FileOperationUtil.re_all_file(xml_dir, lambda x:str(x).endswith('.xml'))):
            # print(index, each_xml_path)
            img_path = os.path.join(img_dir, os.path.split(each_xml_path)[1][:-3] + 'jpg')

            # 文件不存在进行过滤
            if not os.path.exists(img_path):
                print("img 文件不存在 : {0}".format(img_path))
                continue

            img = Image.open(img_path)
            xml_info = parse_xml(each_xml_path)
            img_size = (float(xml_info['size']['width']), float(xml_info['size']['height']))
            for obj_index, each_obj_info in enumerate(xml_info['object']):
                score = float(each_obj_info["difficult"])       # fixme 这个参数要进行规范一下
                name = each_obj_info['name']
                # 左上角，右下角的点，
                region_loc = [int(each_obj_info['bndbox']['xmin']), int(each_obj_info['bndbox']['ymin']),
                              int(each_obj_info['bndbox']['xmax']), int(each_obj_info['bndbox']['ymax'])]
                #
                for i in range(1, len(section_list)):
                    if score < section_list[i]:
                        each_save_dir = os.path.join(save_dir, "{0}-{1}".format(section_list[i-1], section_list[i]), name)

                        if not os.path.exists(each_save_dir):
                            os.makedirs(each_save_dir)

                        save_path = os.path.join(each_save_dir, os.path.split(each_xml_path)[1][:-4] + '_{0}.jpg'.format(obj_index))
                        # 将矩形框进行扩展
                        # region_loc = DatabaseUtil.region_augment(region_loc, img_size, [0.5, 0.5, 0.05, 0.05])
                        region = img.crop((region_loc[0], region_loc[1], region_loc[2], region_loc[3]))
                        region.save(save_path)
                        break

    @staticmethod
    def merge_object(xml_dir_path, merge_dict):
        """根据合并字典，合并分类"""
        # merge_dict = {'single':'fzc', 'fzc':'fzc'}
        for each in FileOperationUtil.re_all_file(xml_dir_path, lambda x: str(x).endswith('.xml')):
            a = ParseXml()
            print(each)
            xml_info = a.get_xml_info(each)
            for each_object in xml_info['object']:
                obj_name = each_object['name']
                if obj_name in merge_dict:
                    each_object['name'] = merge_dict[obj_name]
                else:
                    print("obj name : {0}".format(obj_name))
                    raise ValueError("obj name 不在 merge dict 中")

            a.save_to_xml(each, assign_xml_info=xml_info)

    @staticmethod
    def remove_no_need_object(xml_dir, save_xml_dir, need_obj_name_list, assign_confidence=0.0):
        """去掉不需要的分类"""

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

    @staticmethod
    def crop_small_img(img_dir, save_dir, assign_name_list=None, xml_dir=None):
        """截取小图，可以对截图的扩进行范围扩展"""

        if xml_dir is None:
            xml_dir = img_dir

        for xml_index, each_xml_path in enumerate(FileOperationUtil.re_all_file(xml_dir, lambda x:str(x).endswith('.xml'))):

            if xml_index % 100 == 0:
                print(xml_index)

            each_img_path = os.path.join(img_dir, os.path.split(each_xml_path)[1][:-3]+'jpg')
            xml_info = parse_xml(each_xml_path)

            if not xml_info["size"]:
                continue

            width = int(float(xml_info["size"]["width"]))
            height = int(float(xml_info["size"]["height"]))
            if not os.path.exists(each_img_path):
                print("文件不存在 ： {0}".format(each_img_path))
                continue

            each_img = Image.open(each_img_path)

            for obj_index, each_obj in enumerate(xml_info['object']):
                each_name = each_obj["name"]
                each_bndbox = [float(each_obj["bndbox"]["xmin"]), float(each_obj["bndbox"]["ymin"]),
                               float(each_obj["bndbox"]["xmax"]), float(each_obj["bndbox"]["ymax"])]

                # 过滤掉那些不需要裁剪的标签
                if not assign_name_list is None:
                    if not each_name in assign_name_list:
                        continue

                # 对结果进行裁剪
                each_bndbox = CocoDatabaseUtil.region_augment(each_bndbox, [width, height], augment_parameter=[0.5, 0.5, 0.2, 0.2])
                each_crop = each_img.crop(each_bndbox)
                crop_save_path = os.path.join(save_dir, os.path.split(each_img_path)[1][:-4] + "-{0}.jpg".format(obj_index))
                each_crop.save(crop_save_path)


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
    def get_subset_from_pic(xml_path, save_dir, min_count=6, small_img_count=3):
        """从一个图片中拿到标签元素的子集"""
        xml_operate = ParseXml()
        xml_info = xml_operate.get_xml_info(xml_path)
        box_list = []
        for each in xml_info["object"]:
            each_range = (int(each["bndbox"]["xmin"]), int(each["bndbox"]["ymin"]), int(each["bndbox"]["xmax"]), int(each["bndbox"]["ymax"]))
            box_list.append(each_range)

        if len(box_list) < 1:
            return

        # fixme 都有全局的图，要是元素大于等于 6 还另外生成小图

        # 图片中的所有元素放到一个小截图中
        merge_range = DatabaseKG.merge_range_list(box_list)
        # 修改数据范围
        xml_info_tmp = copy.deepcopy(xml_info)
        for each_obj in xml_info_tmp["object"]:
            each_obj["bndbox"]["xmin"] = str(int(each_obj["bndbox"]["xmin"]) - merge_range[0] )
            each_obj["bndbox"]["ymin"] = str(int(each_obj["bndbox"]["ymin"]) - merge_range[1] )
            each_obj["bndbox"]["xmax"] = str(int(each_obj["bndbox"]["xmax"]) - merge_range[0] )
            each_obj["bndbox"]["ymax"] = str(int(each_obj["bndbox"]["ymax"]) - merge_range[1] )
        # 存储 xml 和 jpg
        xml_info_tmp["size"] = {'width': str(merge_range[2]-merge_range[0]), 'height': str(merge_range[3]-merge_range[1]), 'depth': '3'}
        each_xml_save_path = os.path.join(save_dir, os.path.split(xml_path)[1])
        xml_operate.save_to_xml(each_xml_save_path, xml_info_tmp)
        # 剪切图像
        each_jpg_save_path = os.path.join(save_dir, os.path.split(xml_path)[1][:-4] + ".jpg")
        img_path = xml_path[:-4] + ".jpg"
        img = Image.open(img_path)
        each_crop = img.crop(merge_range)
        each_crop.save(each_jpg_save_path)

        # 元素个数大于阈值，另外生成小图
        if len(box_list) > min_count:
            for i in range(small_img_count):
                # xml_info_tmp = xml_info.copy()
                xml_info_tmp = copy.deepcopy(xml_info)      # copy() 原来不是深拷贝啊，不是直接开辟空间存放值？
                # 打乱顺序
                random.shuffle(box_list)
                # 拿出其中的三个，得到外接矩形的外接矩形
                merge_range = DatabaseKG.merge_range_list(box_list[:3])
                # 遍历所有要素，找到在 merge_range 中的要素，
                obj_list = []
                for each_obj in xml_info_tmp["object"]:
                    each_range = (int(each_obj["bndbox"]["xmin"]), int(each_obj["bndbox"]["ymin"]), int(each_obj["bndbox"]["xmax"]), int(each_obj["bndbox"]["ymax"]))
                    # print(each_range, merge_range)
                    if DatabaseKG.is_in_range(each_range, merge_range):
                        # 裁剪后的图像范围要进行对应的平移
                        each_obj["bndbox"]["xmin"] = str(int(each_obj["bndbox"]["xmin"]) - merge_range[0])
                        each_obj["bndbox"]["ymin"] = str(int(each_obj["bndbox"]["ymin"]) - merge_range[1])
                        each_obj["bndbox"]["xmax"] = str(int(each_obj["bndbox"]["xmax"]) - merge_range[0])
                        each_obj["bndbox"]["ymax"] = str(int(each_obj["bndbox"]["ymax"]) - merge_range[1])
                        obj_list.append(each_obj)
                #
                xml_info_tmp["object"] = obj_list
                xml_info_tmp["size"] = {'width': str(merge_range[2]-merge_range[0]), 'height': str(merge_range[3]-merge_range[1]), 'depth': '3'}
                xml_name = "_{0}.xml".format(i)
                img_name = "_{0}.jpg".format(i)
                xml_info_tmp["filename"] = img_name                                                             # 修改文件名
                each_xml_save_path = os.path.join(save_dir, os.path.split(xml_path)[1][:-4] + xml_name)
                xml_operate.save_to_xml(each_xml_save_path, xml_info_tmp)
                # 剪切图像
                each_jpg_save_path = os.path.join(save_dir, os.path.split(xml_path)[1][:-4] + img_name)
                img_path = xml_path[:-4] + ".jpg"
                img = Image.open(img_path)
                each_crop = img.crop(merge_range)
                each_crop.save(each_jpg_save_path)



# if __name__ == "__main__":

    # img_dir = r"C:\Users\14271\Desktop\优化开口销第二步\001_训练数据\save_small_img_new"
    # xml_dir = r"C:\Users\14271\Desktop\优化开口销第二步\001_训练数据\save_small_img_new"
    # save_dir = r"C:\Users\14271\Desktop\优化开口销第二步\001_训练数据\save_small_img_reshape"
    #
    # # category_dict = {"middle_pole":1, "single":2, "no_single":3}
    # # category_dict = {"fzc":1, "zd":2, "xj":3, "other":4, "ljj":5}
    # # category_dict = {"fzc":1, "zfzc":2, "hzfzc":3, "holder":4, "single":5}
    # category_dict = {"K":1, "KG":2, "Lm":3, "dense2":4, "other_L4kkx":5,"other_fist":6,"other_fzc":7,"other1":8,"other2":9,
    #                  "other3":10, "other4":11, "other5":12, "other6":13, "other7":14, "other8":15, "other9":16, "dense1":17, "dense3":18}
    #
    #
    # # DatabaseUtil.change_img_to_coco_format(img_dir, save_dir, 1536, xml_dir, category_dict=category_dict, file_head="")
    #
    # # merge_dict = {"fzc_broken": 'fzc', "fzc": "fzc", "Fnormal": "fzc", "xj": "xj", "ljj": "ljj", "other": "other", "zd": "zd"}
    # # merge_dict = {"middle_single": "middle_pole", "no_single": "no_single", "middle_pole":"middle_pole", "single":"single"}
    # # DatabaseUtil.merge_voc_class(xml_dir, merge_dict=merge_dict,
    # #                              save_folder=r"C:\Users\14271\Desktop\dataset_fzc\013_再次增加标图数量，而且全部采用扩展后的图\001_新增的小防振锤")
    #
    # CocoDatabaseUtil.show_voc_class_info(r"C:\Users\14271\Desktop\优化开口销第二步\003_检测结果\result_faster")
    #
    # # --------------------------------------------------------------------------------------------------------
    # # xmlDir = r"C:\Users\14271\Desktop\优化开口销第二步\000_原始数据_Part_CY-JTM_OrignalPic-Xml20200515"
    # # saveDir = r"C:\Users\14271\Desktop\优化开口销第二步\001_训练数据\save_small_img_new"
    # #
    # # for index, each_xml_path in enumerate(FileOperationUtil.re_all_file(xmlDir, lambda x:str(x).endswith((".xml")))[:1922]):
    # #     print(index, each_xml_path)
    # #     DatabaseKG.get_subset_from_pic(each_xml_path, saveDir)
    # # --------------------------------------------------------------------------------------------------------
    #
    # # DatabaseUtil.show_area_spread(r"C:\Users\14271\Desktop\del\step_1_0.1")
    #
    # # DatabaseUtil.voc2coco(r"C:\Users\14271\Desktop\优化开口销第二步\001_训练数据\save_small_img_new",
    # #                       r"C:\Users\14271\Desktop\instances_val.json",
    # #                       category_dict=category_dict)
    #
    # # DatabaseUtil.coco2voc(r"C:\Users\14271\Desktop\del.json", save_folder=r"C:\Users\14271\Desktop\del123")
    #
    # # DatabaseUtil.analyze_detection_res_in_every_section(r"C:\Users\14271\Desktop\防振锤优化\006_使用多分类\004_数据反标，增加训练量，efficientdet-d7_282_94090\merge_0.7",
    # #                                                     r"C:\Users\14271\Desktop\防振锤优化\006_使用多分类\004_数据反标，增加训练量，efficientdet-d7_282_94090\result",
    # #                                                     r"C:\Users\14271\Desktop\防振锤优化\007_根据置信度分级设置规则\res_normal",section_list = [0, 0.4, 0.6, 0.8, 1])
    #
    # # DatabaseUtil.remove_no_need_object(r"C:\Users\14271\Desktop\防振锤优化\000_标准测试集\xml_zd",
    # #                                    r"C:\Users\14271\Desktop\防振锤优化\000_标准测试集\xml_remove_zd", {"Fnormal", "fzc_broken"}, assign_confidence=0.5)
    #
    # # DatabaseUtil.find_broken_fzc(r"C:\Users\14271\Desktop\step_2", r"C:\Users\14271\Desktop\compare")
    #
    # # DatabaseUtil.find_imgs_which_have_xml(r"C:\Users\14271\Desktop\防振锤优化\000_标准测试集\35kV", r"C:\Users\14271\Desktop\防振锤优化\000_标准测试集\no_fzc")
    #
    # # DatabaseUtil.crop_small_img(r"C:\Users\14271\Desktop\dataset_fzc\012_增加step_2标图范围，标图数量\fzc_single_add_35KV\train",
    # #                             r"C:\Users\14271\Desktop\检查 no_single 是不是标对了", assign_name_list=["no_single"],
    # #                             xml_dir=r"C:\Users\14271\Desktop\dataset_fzc\012_增加step_2标图范围，标图数量\fzc_single_add_35KV\train")
    #
    # # DatabaseUtil.re_set_diffcult_info(r"C:\Users\14271\Desktop\dataset_fzc\013_再次增加标图数量，而且全部采用扩展后的图\002_最开始数据中的小防振锤",
    # #                                   r"C:\Users\14271\Desktop\dataset_fzc\013_再次增加标图数量，而且全部采用扩展后的图\002_最开始数据中的小防振锤")