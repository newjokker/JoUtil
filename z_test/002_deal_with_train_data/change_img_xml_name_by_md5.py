# -*- coding: utf-8  -*-
# -*- author: jokker -*-


import os
import shutil
from JoTools.utils.FileOperationUtil import FileOperationUtil
from JoTools.txkjRes.deteRes import DeteRes
from JoTools.utils.PrintUtil import PrintUtil
from JoTools.utils.HashlibUtil import HashLibUtil

img_dir = r"\\192.168.3.80\算法-数据交互\aqm_0_0_8版本数据_入库_del_2022_930\img"
xml_dir = r"\\192.168.3.80\算法-数据交互\aqm_0_0_8版本数据_入库_del_2022_930\xml"
save_dir = r"\\192.168.3.80\算法-数据交互\aqm_0_0_8版本数据_入库_del_2022_930"


save_img_dir = os.path.join(save_dir, 'JPEGImages')
os.makedirs(save_img_dir, exist_ok=True)
save_xml_dir = os.path.join(save_dir, 'Annotations')
os.makedirs(save_xml_dir, exist_ok=True)



for each_img_path in FileOperationUtil.re_all_file(img_dir, endswitch=['.jpg', '.JPG', '.png', '.PNG']):
    print(each_img_path)
    each_md5 = HashLibUtil.get_file_md5(each_img_path)
    img_new_path = os.path.join(save_img_dir, "{0}.jpg".format(each_md5))
    xml_new_path = os.path.join(save_xml_dir, "{0}.xml".format(each_md5))
    #
    each_xml_path = os.path.join(xml_dir, FileOperationUtil.bang_path(each_img_path)[1] + '.xml')
    #
    if os.path.exists(each_xml_path):

        a = DeteRes(each_xml_path)
        if len(a) < 1:
            continue

        # shutil.move(each_img_path, img_new_path)
        # shutil.move(each_xml_path, xml_new_path)

        shutil.copy(each_img_path, img_new_path)
        shutil.copy(each_xml_path, xml_new_path)









