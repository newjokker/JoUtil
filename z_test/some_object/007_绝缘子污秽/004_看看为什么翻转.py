# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import cv2
import os
import numpy as np
from JoTools.operateDeteRes import OperateDeteRes, DeteRes
from JoTools.utils.FileOperationUtil import FileOperationUtil


img_dir = r"C:\Users\14271\Desktop\jyz_demo"
xml_dir = r"C:\Users\14271\Desktop\jyz_demo"
save_dir = r"C:\Users\14271\Desktop\find_bug\crop_new"

for each_xml_path in FileOperationUtil.re_all_file(xml_dir, endswitch=['.xml']):
    img_path = os.path.join(img_dir, FileOperationUtil.bang_path(each_xml_path)[1] + ".jpg")


    a = DeteRes(each_xml_path, assign_img_path=img_path)

    # a.img_path = img_path

    for index, each_dete_obj in enumerate(a):
        each_im = a.get_sub_img_by_dete_obj(each_dete_obj, RGB=True)

        save_path = os.path.join(save_dir, FileOperationUtil.bang_path(each_xml_path)[1] + '_{0}.jpg').format(index)

        print(save_path)

        cv2.imwrite(save_path, each_im)

    cv2.imwrite(os.path.join(save_dir, FileOperationUtil.bang_path(each_xml_path)[1] + '.jpg'), np.asarray(a.img))





















