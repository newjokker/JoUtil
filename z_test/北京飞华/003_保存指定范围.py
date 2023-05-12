# -*- coding: utf-8  -*-
# -*- author: jokker -*-


import os
from JoTools.utils.FileOperationUtil import FileOperationUtil
from JoTools.txkjRes.deteRes import DeteRes


img_xml_dir = r"C:\Users\14271\Desktop\北京飞华\002_要标注的数据_02\xml"
save_dir = r"C:\Users\14271\Desktop\北京飞华\002_要标注的数据_02\crop"

for each_img_path in FileOperationUtil.re_all_file(img_xml_dir, endswitch=[".jpg"]):

    each_xml_path = each_img_path[:-3] + "xml"

    a = DeteRes(each_xml_path)
    a.img_path = each_img_path

    bbox = a.filter_by_tags(need_tag=["bounding_box"], update=False)

    a.filter_by_tags(remove_tag=["bounding_box"], update=True)

    save_xml_path = os.path.join(save_dir, FileOperationUtil.bang_path(each_img_path)[1] + ".xml")

    if len(bbox) > 0:

        a.save_assign_range(assign_range=bbox[0].get_rectangle(), save_dir=save_dir)

    else:
        a.save_to_xml(save_xml_path)









