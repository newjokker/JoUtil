# -*- coding: utf-8  -*-
# -*- author: jokker -*-


from JoTools.txkj.parseXml import parse_xml
from JoTools.detectionResult import DeteRes
from JoTools.for_csdn.word_pic.word_pic import WordImage
from JoTools.utils.FileOperationUtil import FileOperationUtil
import os



xml_dir = r"C:\data\fzc_优化相关资料\dataset_fzc\000_train_data_step_1\xml"
img_dir = r"C:\data\fzc_优化相关资料\dataset_fzc\000_train_data_step_1\img"
save_dir = r"C:\Users\14271\Desktop\fzc_train_data_extend"


# exit()

for each_xml_path in FileOperationUtil.re_all_file(xml_dir, lambda x:str(x).endswith('.xml')):
    print((each_xml_path))
    each_img_name = os.path.split(each_xml_path)[1][:-4] + '.JPG'
    each_img_path = os.path.join(img_dir, each_img_name)
    #
    a = DeteRes(each_xml_path, each_img_path)

    if len(a.alarms) >= 2:
        max_range = a.get_max_range()
        a.save_assign_range(max_range, save_dir=save_dir)




# for each_xml_path in FileOperationUtil.re_all_file(xml_dir, lambda x:str(x).endswith('.xml')):
#     DeteRes.get_region_xml_from_cut_xml(each_xml_path, save_dir)
#
#
