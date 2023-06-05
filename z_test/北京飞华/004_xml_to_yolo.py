# -*- coding: utf-8  -*-
# -*- author: jokker -*-


import os
from JoTools.txkjRes.deteRes import DeteRes
from JoTools.utils.FileOperationUtil import FileOperationUtil

xml_dir = r"C:\Users\14271\Desktop\北京飞华\010_鞋子视频检测\003_验证数据\val\Annotations"
img_dir = r"C:\Users\14271\Desktop\北京飞华\010_鞋子视频检测\003_验证数据\val\JPEGImages"
res_dir = r"C:\Users\14271\Desktop\北京飞华\010_鞋子视频检测\003_验证数据\val\labels"

tag_list = ["aqm","aqm_error","aqm_miss","bounding_box","gzf","gzf_error","gzf_miss","kz","kz_error","st","st_miss","xz"]
tag_map = {}
for index, each in enumerate(tag_list):
    tag_map[each] = index

index = 0
for each_xml_path in FileOperationUtil.re_all_file(xml_dir, endswitch=[".xml"]):
    index += 1
    print(index, each_xml_path)
    dete_res = DeteRes(each_xml_path)

    dete_res.img_path = os.path.join(img_dir, FileOperationUtil.bang_path(each_xml_path)[1] + ".jpg")

    if os.path.exists(dete_res.img_path):
        dete_res.update_tags({"st_error":"st"})
        each_txt_path = os.path.join(res_dir, FileOperationUtil.bang_path(each_xml_path)[1] + ".txt")
        dete_res.save_to_yolo_txt(each_txt_path, tag_map)
    else:
        raise ValueError("error")














