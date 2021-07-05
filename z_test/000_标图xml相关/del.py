# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import os
from JoTools.utils.FileOperationUtil import FileOperationUtil

img_dir = r"/home/suanfa-4/ldq/001_train_data/fzc_step_1/JPEGImages"
xml_dir = r"/home/suanfa-4/ldq/001_train_data/fzc_step_1/Annotations"

index = 0
for each_img_path in FileOperationUtil.re_all_file(img_dir, endswitch=['.jpg']):
    each_xml_path = os.path.join(xml_dir, FileOperationUtil.bang_path(each_img_path)[1] + '.xml')
    if not os.path.exists(each_xml_path):
        os.remove(each_img_path)
        index += 1

for each_xml_path in FileOperationUtil.re_all_file(img_dir, endswitch=['.xml']):
    each_img_path = os.path.join(xml_dir, FileOperationUtil.bang_path(each_xml_path)[1] + '.jpg')
    if not os.path.exists(each_img_path):
        os.remove(each_xml_path)
        index += 1



print(index)





