# -*- coding: utf-8  -*-
# -*- author: jokker -*-
import pprint
# from JoTools.operateResXml import OperateResXml
from JoTools.txkjRes.deteRes import DeteRes
from JoTools.utils.FileOperationUtil import FileOperationUtil
#
# xml_path = r"C:\Users\14271\Desktop\del\test.xml"
# img_path = r"C:\Users\14271\Desktop\del\test.jpg"
#
# xml_dir = r"C:\Users\14271\Desktop\test"
#
for each in FileOperationUtil.re_all_file(r"C:\Users\14271\Desktop\del\新建文件夹\xml转code", lambda x: str(x).endswith('.xml')):
    a = DeteRes(each)
    a.save_to_xml(each)

    pass

# OperateResXml.show_class_count(xml_dir)
#
#
#
# # 更新标签
# for xml_index, each_xml_path in enumerate(xml_list):
#     #
#     each_dete_res = DeteRes(each_xml_path)
#     each_dete_res.do_nms_in_assign_tags(['KG', 'K', 'Lm'], 0.1)
#     each_dete_res.save_to_xml(each_xml_path)
#
# OperateResXml.show_class_count(xml_dir)
#
# class do():
#
#     def __call__(self, a):
#         print(str(a)*3)
#
#
#
#
# stuff = ['spam', 'eggs', 'lumberjack', 'knights', 'ni']
# stuff.insert(0, stuff[:])
# pp = pprint.PrettyPrinter(indent=4)
# pp.pprint(stuff)
#
# a = do()
# a('123')

