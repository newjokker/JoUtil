# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import random
import os
import shutil
import cv2
import PIL.Image as Image
from JoTools.operateDeteRes import OperateDeteRes
from JoTools.txkjRes.deteRes import DeteRes,DeteObj
from JoTools.utils.FileOperationUtil import FileOperationUtil
from JoTools.utils.RandomUtil import RandomUtil


xml_dir = r"\\192.168.3.80\算法\大金具-算法\qfm\连接件训练数据集"
save_dir = r"\\192.168.3.80\算法\大金具-算法\qfm\连接件训练数据集_update_xml"


OperateDeteRes.get_class_count(xml_dir, print_count=True)


update_tags = {"BGXJ":"robndbox_BGXJ", "DBTZB":"robndbox_DBTZB",
               "LCLB":"robndbox_LCLB", "LKLB":"robndbox_LKLB",
               "LLB":"robndbox_LLB", "LLLB":"robndbox_LLLB",
               "LSXXJ":"robndbox_LSXXJ", "PGuaBan":"robndbox_PGuaBan",
               "PTTZB":"robndbox_PTTZB", "QYB":"robndbox_QYB", "STXJ":"robndbox_STXJ",
               "SXJ":"robndbox_SXJ", "Sanjiaoban":"robndbox_Sanjiaoban", "TXXJ":"robndbox_TXXJ",
               "UBGuaBan":"robndbox_UBGuaBan", "UGuaHuan":"robndbox_UGuaHuan", "ULuoShuan":"robndbox_ULuoShuan",
               "WTGB":"robndbox_WTGB", "XieXingXJ":"robndbox_XieXingXJ", "XinXingHuan":"robndbox_XinXingHuan",
               "XuanChuiXianJia":"robndbox_XuanChuiXianJia", "YuJiaoShiXJ":"robndbox_YuJiaoShiXJ", "ZBDGuaBan":"robndbox_ZBDGuaBan",
               "ZGuaBan":"robndbox_ZGuaBan", "ZHGuaHuan":"robndbox_ZHGuaHuan", "Zhongchui":"robndbox_Zhongchui",
               "other1":"robndbox_other1", "other2":"robndbox_other2", "other3":"robndbox_other3",
               }

for each_xml_path in FileOperationUtil.re_all_file(xml_dir, endswitch=['.xml']):
    a = DeteRes(each_xml_path)
    a.update_tags(update_dict=update_tags)
    # a.filter_by_tags(need_tag=["td"])
    # a.do_augment(augment_parameter=[0.05,0.05,0.05,0.05])
    save_path = os.path.join(save_dir, os.path.split(each_xml_path)[1])
    a.save_to_xml(save_path)


OperateDeteRes.get_class_count(save_dir, print_count=True)


