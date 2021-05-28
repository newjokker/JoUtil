# -*- coding: utf-8  -*-
# -*- author: jokker -*-


import os
from JoTools.utils.FileOperationUtil import FileOperationUtil
from JoTools.txkjRes.deteRes import DeteRes


img_dir = r"/home/suanfa-1/武汉/2021年4月集中培育"
xml_dir = r"/home/suanfa-4/ldq/fzc_v1.2.3.2_new_flow_redis/merge"
save_dir = r"/home/suanfa-4/ldq/fzc_v1.2.3.2_new_flow_redis/crop"

name_dict = set()

for each_img_path in FileOperationUtil.re_all_file(img_dir, lambda x:str(x).endswith(('.jpg', '.JPG'))):
    img_name = os.path.split(each_img_path)[1]
    if img_name not in name_dict:
        name_dict.add(img_name)
        xml_path = os.path.join(xml_dir, img_name[:-3] + 'xml')
        if os.path.exists(xml_path):
            try:
                a = DeteRes()
                a.img_path = each_img_path
                a.xml_path = xml_path
                a.crop_and_save(save_dir, augment_parameter=[0.3, 0.3, 0.3, 0.3], split_by_tag=True)
            except Exception as e:
                print(e)







#