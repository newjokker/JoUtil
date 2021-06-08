# -*- coding: utf-8  -*-
# -*- author: jokker -*-

from JoTools.for_csdn.word_pic.word_pic import WordImage
from PIL import Image
from JoTools.operateDeteRes import OperateDeteRes
from JoTools.txkjRes.deteRes import DeteRes
from JoTools.utils.FileOperationUtil import FileOperationUtil

# -------------------------------------------------------------------------------------

xml_dir = r"C:\data\fzc_优化相关资料\dataset_fzc\000_0_标准测试集\xml"
# -------------------------------------------------------------------------------------


for each in OperateDeteRes.get_class_count(xml_dir).items():
    print(each)

