# -*- coding: utf-8  -*-
# -*- author: jokker -*-


from JoTools.utils.FileOperationUtil import FileOperationUtil
from JoTools.txkjRes.deteRes import DeteRes
from JoTools.operateDeteRes import OperateDeteRes

xml_dir = r"F:\20211019_防震锤锈蚀数据清洗\xml"
img_dir = r"C:\Users\14271\Desktop\fzcRust_data"
save_dir = r"F:\20211019_防震锤锈蚀数据清洗\fix_data"

save_list = []
for each_xml_path in FileOperationUtil.re_all_file(xml_dir, endswitch=['.xml']):

    each_img_path = OperateDeteRes.get_assign_file_path(FileOperationUtil.bang_path(each_xml_path)[1], img_dir, suffix_list=['.jpg', '.JPG'])

    if each_img_path:

        a = DeteRes(each_xml_path)

        if a.has_tag('fzc_rust'):

            save_list.append(each_img_path)
            save_list.append(each_xml_path)


FileOperationUtil.move_file_to_folder(save_list, save_dir, is_clicp=False)









