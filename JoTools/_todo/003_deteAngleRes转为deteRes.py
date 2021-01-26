# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import sys
import cv2
import os
from JoTools.txkjRes.deteAngleXml import parse_xml, save_to_xml
from JoTools.txkjRes.deteAngleRes import DeteAngleRes
from JoTools.txkjRes.deteRes import DeteRes
from JoTools.operateDeteRes import OperateDeteRes
from JoTools.utils.FileOperationUtil import FileOperationUtil


img_dir = r"C:\Users\14271\Desktop\10kv\10kV_part2"
xml_dir = r"C:\Users\14271\Desktop\10kv\10kV_part2"
save_dir = r"C:\Users\14271\Desktop\10kv_crop_new_2"



def crop(xml_path, jpg_path, save_dir):
    """裁剪"""
    a = DeteAngleRes(xml_path=xml_path, assign_img_path=jpg_path)
    b = DeteRes(assign_img_path=jpg_path)
    new_alarms = []
    for each in a.alarms:
        new_alarms.append(each.to_dete_obj())

    b.reset_alarms(new_alarms)
    b.crop_and_save(save_dir, augment_parameter=[0.3,0.3,0.3,0.3], split_by_tag=True)
    # b.crop_and_save(save_dir)


def crop2(xml_path, jpg_path, save_dir):
    """裁剪"""
    a = DeteRes(xml_path=xml_path, assign_img_path=jpg_path)
    a.angle_obj_to_obj()
    a.crop_and_save(save_dir, augment_parameter=[0.3,0.3,0.3,0.3], split_by_tag=True)



if __name__ == "__main__":


    # crop(r"C:\Users\14271\Desktop\del\A相大号侧-1.xml", r"C:\Users\14271\Desktop\del\A相大号侧-1.jpg", r"C:\Users\14271\Desktop\del\crop")


    for index, each_xml_path in enumerate(FileOperationUtil.re_all_file(img_dir, lambda x:str(x).endswith(".xml"))):
        print(index, each_xml_path)
        each_img_path = os.path.join(img_dir, os.path.split(each_xml_path)[1][:-3] + 'jpg')

        if not os.path.exists(each_img_path):
            continue

        try:
            crop2(each_xml_path, each_img_path, save_dir)
        except Exception as e:
            print(e)

