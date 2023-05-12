# -*- coding: utf-8  -*-
# -*- author: jokker -*-

from JoTools.txkjRes.deteRes import DeteRes
from JoTools.utils.FileOperationUtil import FileOperationUtil


xml_dir = r"C:\Users\14271\Desktop\北京飞华\del\demo_xml"

# save_dir = r"C:\Users\14271\Desktop\img_xml\people"

two = 0
one= 0

for xml_path in FileOperationUtil.re_all_file(xml_dir, endswitch=[".xml"]):

    # print(xml_path)

    a = DeteRes(xml_path)
    b = DeteRes(xml_path)

    # a.print_as_fzc_format()

    a.update_tags({"gzf_error":"gzf", "gzf_miss":"gzf"})

    tag_dict = a.count_tags()

    if "gzf" in tag_dict:
        if tag_dict["gzf"] == 1:
            one += 1
        else:
            two += 1

        bbox= a.get_bounding_box()

        b.add_obj_2(bbox)
        b.save_to_xml(xml_path)

    else:
        print(0)

    print("-"*100)


print("one", one)

print("two", two)

sorted([1,2,3,4,5], key=lambda x:FileOperationUtil.bang_path(x)[1].split("_"))
