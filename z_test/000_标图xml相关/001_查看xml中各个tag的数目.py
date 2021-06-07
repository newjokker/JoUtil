# -*- coding: utf-8  -*-
# -*- author: jokker -*-

from JoTools.for_csdn.word_pic.word_pic import WordImage
from PIL import Image
from JoTools.operateDeteRes import OperateDeteRes
from JoTools.txkjRes.deteRes import DeteRes
from JoTools.utils.FileOperationUtil import FileOperationUtil

# -------------------------------------------------------------------------------------

xml_dir = r"C:\data\fzc_优化相关资料\dataset_fzc\999_wait_for_train\武汉电科院四月五月数据"
# -------------------------------------------------------------------------------------


for each in OperateDeteRes.get_class_count(xml_dir).items():
    print(each)



