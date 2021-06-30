# -*- coding: utf-8  -*-
# -*- author: jokker -*-


from JoTools.for_csdn.word_pic.word_pic import WordImage
from PIL import Image
from JoTools.operateDeteRes import OperateDeteRes
from JoTools.txkjRes.deteRes import DeteRes
from JoTools.utils.FileOperationUtil import FileOperationUtil


img_dir = r"C:\data\fzc_优化相关资料\dataset_fzc\000_train_data_step_1\crop_with_xml_fix_xml"
save_dir = r"C:\data\fzc_优化相关资料\dataset_fzc\000_train_data_step_1\crop_xml"


img_list = list(FileOperationUtil.re_all_file(img_dir, endswitch=['.xml']))


FileOperationUtil.move_file_to_folder(img_list, save_dir, is_clicp=True)




