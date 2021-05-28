# -*- coding: utf-8  -*-
# -*- author: jokker -*-

from JoTools.for_csdn.word_pic.word_pic import WordImage
from PIL import Image
from JoTools.operateDeteRes import OperateDeteRes
from JoTools.txkjRes.deteRes import DeteRes
from JoTools.utils.FileOperationUtil import FileOperationUtil

# -------------------------------------------------------------------------------------
ratio = 2                                               # 图像缩小的比例
img_path = r"C:\Users\14271\Desktop\test.jpg"
save_path = r'C:\Users\14271\Desktop\test_2.jpg'
# -------------------------------------------------------------------------------------


for each in OperateDeteRes.get_class_count(r"/home/suanfa-4/ldq/del/merge").items():
    print(each)


#
# xml_dir = r"C:\Users\14271\Desktop\ceshiji\merge\jyhQX"
#
# for each_xml_path in FileOperationUtil.re_all_file(xml_dir):
#     a = DeteRes(xml_path=each_xml_path)
#     # a.filter_by_tags(need_tag=['XJfail'])
#     a.save_to_xml(each_xml_path)
#
#     # print(a.count_tags())
#     # break
#



# for each in OperateDeteRes.get_class_count(xml_dir).items():
#     print(each)




