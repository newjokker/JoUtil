# -*- coding: utf-8  -*-
# -*- author: jokker -*-


import os
import os.path
from JoTools.utils.FileOperationUtil import FileOperationUtil
from JoTools.txkjRes.deteRes import DeteRes



img_dir = r"C:\Users\14271\Desktop\temp\part2"

xml_dir = r"C:\Users\14271\Desktop\temp\part_2_dete"

index = 0
for each_img_path in FileOperationUtil.re_all_file(img_dir, endswitch=[".jpg", ".JPG", ".png", ".PNG"]):

    each_xml_path = os.path.join(xml_dir, FileOperationUtil.bang_path(each_img_path)[1] + ".xml")

    if not os.path.exists(each_xml_path):
        os.remove(each_img_path)
        index += 1
        print(index, each_img_path)
        continue

    a = DeteRes(each_xml_path)

    a.filter_by_conf(0.4, update=True)

    if(len(a) == 0):
        os.remove(each_img_path)
        os.remove(each_xml_path)
        index += 1
        print(index, each_img_path)
    else:
        pass
        # print("keep : ", each_img_path)







