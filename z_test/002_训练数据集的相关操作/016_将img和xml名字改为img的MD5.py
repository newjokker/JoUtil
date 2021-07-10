# -*- coding: utf-8  -*-
# -*- author: jokker -*-


import os
import shutil
from JoTools.utils.FileOperationUtil import FileOperationUtil
from JoTools.txkjRes.deteRes import DeteRes
from JoTools.utils.PrintUtil import PrintUtil
from JoTools.utils.HashlibUtil import HashLibUtil

img_dir = r"C:\Users\14271\Desktop\寻找未被发现的fzc_broken\JPEGImages"
xml_dir = r"C:\Users\14271\Desktop\寻找未被发现的fzc_broken\xml"
save_dir = r"C:\Users\14271\Desktop\寻找未被发现的fzc_broken\train_data"


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
        # shutil.copy(each_img_path, img_new_path)
        # shutil.copy(each_xml_path, xml_new_path)

        shutil.move(each_img_path, img_new_path)
        shutil.move(each_xml_path, xml_new_path)








