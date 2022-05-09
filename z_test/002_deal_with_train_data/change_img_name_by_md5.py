# -*- coding: utf-8  -*-
# -*- author: jokker -*-


import os
import shutil
from JoTools.utils.FileOperationUtil import FileOperationUtil
from JoTools.txkjRes.deteRes import DeteRes
from JoTools.utils.PrintUtil import PrintUtil
from JoTools.utils.HashlibUtil import HashLibUtil

img_dir = r"E:\多标签分类\body_xml_img\img_xml"
save_dir = r"E:\多标签分类\body_xml_img\img_xml"


for each_img_path in FileOperationUtil.re_all_file(img_dir, endswitch=['.jpg', '.JPG', '.png', '.PNG']):
    print(each_img_path)
    each_md5 = HashLibUtil.get_file_md5(each_img_path)
    img_new_path = os.path.join(save_dir, "{0}.jpg".format(each_md5))

    shutil.move(each_img_path, img_new_path)








