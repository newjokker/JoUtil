# -*- coding: utf-8  -*-
# -*- author: jokker -*-


from JoTools.txkjRes.deteRes import DeteRes
from JoTools.utils.FileOperationUtil import FileOperationUtil

xml_dir = r"C:\Users\14271\Desktop\北京飞华\029_工器具破损\img"

for each_img_path in FileOperationUtil.re_all_file(xml_dir, endswitch=[".xml"]):

    a = DeteRes(each_img_path)

    if(len(a) == 2):
        a.print_as_fzc_format()

        if a[0].get_area() > a[1].get_area():
            a[0].tag = "big"
            a[1].tag = "small"
        else:
            a[1].tag = "big"
            a[0].tag = "samll"

    a.save_to_xml(each_img_path)
