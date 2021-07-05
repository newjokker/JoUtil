# -*- coding: utf-8  -*-
# -*- author: jokker -*-


from JoTools.for_csdn.word_pic.word_pic import WordImage
from PIL import Image
from JoTools.operateDeteRes import OperateDeteRes
from JoTools.txkjRes.deteRes import DeteRes
from JoTools.utils.FileOperationUtil import FileOperationUtil


xml_dir = r"C:\Users\14271\Desktop\fzc_标注\6.15_fzc范围\6.15_fzc范围"
save_dir = r"C:\data\fzc_优化相关资料\dataset_fzc\000_train_data_step_1\fix_obj_range\crop_xml"


img_list = list(FileOperationUtil.re_all_file(xml_dir, endswitch=['.xml']))


FileOperationUtil.move_file_to_folder(img_list, save_dir, is_clicp=True)




