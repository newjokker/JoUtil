# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import os
from JoTools.for_csdn.word_pic.word_pic import WordImage
from PIL import Image
from JoTools.operateDeteRes import OperateDeteRes
from JoTools.txkjRes.deteRes import DeteRes
from JoTools.utils.FileOperationUtil import FileOperationUtil


img_dir = r"/home/suanfa-4/武汉数据备份/2021年6月算法培育"
save_dir = r"/home/suanfa-3/ldq/modelManageNew/testdir/modeldata/fzc/fzc_wuhan_006"

file_path_list = []


for each_xml_file in FileOperationUtil.re_all_file(img_dir, endswitch='.xml'):
    #print(each_xml_file)
    a = DeteRes(each_xml_file)
    if a.has_tag("040303022") or a.has_tag("040303021"):
        # get img path
        each_img_path = os.path.split(each_xml_file)[0].strip("xml") + FileOperationUtil.bang_path(each_xml_file)[1] + '.jpg'
        if os.path.exists(each_img_path):
            file_path_list.append(each_img_path)
            file_path_list.append(each_xml_file)

        print(each_img_path)
        #break

    else:
        continue


FileOperationUtil.move_file_to_folder(file_path_list, save_dir, is_clicp=False)