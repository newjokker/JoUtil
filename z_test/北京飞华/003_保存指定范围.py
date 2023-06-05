# -*- coding: utf-8  -*-
# -*- author: jokker -*-


import os
from JoTools.utils.FileOperationUtil import FileOperationUtil
from JoTools.txkjRes.deteRes import DeteRes


img_xml_dir = r"C:\Users\14271\Desktop\北京飞华\010_鞋子视频检测\003_验证数据\img_xml"
save_dir = r"C:\Users\14271\Desktop\北京飞华\010_鞋子视频检测\003_验证数据\val"

for each_img_path in FileOperationUtil.re_all_file(img_xml_dir, endswitch=[".jpg"]):
    each_xml_path = each_img_path[:-3] + "xml"

    if os.path.exists(each_xml_path):

        a = DeteRes(each_xml_path)
        a.img_path = each_img_path

        a.filter_by_dete_res_mask(mask_dete_res=1, cover_index_th=0.01, update=True)

        bbox = a.filter_by_tags(need_tag=["bounding_box"], update=False)
        a.filter_by_tags(remove_tag=["bounding_box"], update=True)
        save_xml_path = os.path.join(save_dir, FileOperationUtil.bang_path(each_img_path)[1] + ".xml")

        if len(bbox) > 0:
            a.save_assign_range(assign_range=bbox[0].get_rectangle(), save_dir=save_dir)
        else:
            a.save_to_xml(save_xml_path)


