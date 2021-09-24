# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import os
from JoTools.operateDeteRes import OperateDeteRes,DeteAcc,DeteRes,DeteObj,DeteAngleObj
from JoTools.utils.FileOperationUtil import FileOperationUtil


crop_ps_dir = r"E:\jyz_leiji_niaofen\new_train_data\crop\filter_crop\脏污"
xml_dir = r"E:\jyz_leiji_niaofen\new_train_data\Annotations"
img_dir = r"E:\jyz_leiji_niaofen\new_train_data\JPEGImages"
save_dir = r"E:\jyz_leiji_niaofen\new_train_data\crop\fix_crop\wuhui"

for each_crop_img in FileOperationUtil.re_all_file(crop_ps_dir, endswitch=['.jpg', '.JPG']):
    print(each_crop_img)
    a = DeteObj()
    each_img_name, each_loc_str = FileOperationUtil.bang_path(each_crop_img)[1].split('-+-')
    a.load_from_name_str(each_loc_str)
    print(a.get_name_str())
    print(each_img_name)

    region_xml = os.path.join(xml_dir, "{0}.xml".format(each_img_name))
    region_img = os.path.join(img_dir, "{0}.jpg".format(each_img_name))

    dete_res = DeteRes(region_xml)
    dete_res.img_path = region_img
    dete_res.filter_by_tags(remove_tag=['ps'])

    dete_res.filter_by_mask(a.get_points(), 0.1, need_in=True )

    dete_res.print_as_fzc_format()

    dete_res.crop_and_save(save_dir, split_by_tag=True)

    print('-'*30)


















