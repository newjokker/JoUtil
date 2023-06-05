# -*- coding: utf-8  -*-
# -*- author: jokker -*-


import os
from PIL import Image
from JoTools.txkjRes.deteRes import DeteRes
from JoTools.utils.FileOperationUtil import FileOperationUtil


img_dir     = r"C:\Users\14271\Desktop\北京飞华\010_鞋子视频检测\003_验证数据\val\images"
txt_dir     = r"C:\Users\14271\Desktop\北京飞华\010_鞋子视频检测\003_验证数据\val\labels"
save_dir    = r"C:\Users\14271\Desktop\北京飞华\010_鞋子视频检测\003_验证数据\val\new_xml"

for each_txt_path in FileOperationUtil.re_all_file(txt_dir, endswitch=[".txt"]):

    each_name = FileOperationUtil.bang_path(each_txt_path)[1]

    each_img_path = os.path.join(img_dir, each_name + ".jpg")
    each_img_path_2 = os.path.join(img_dir, each_name + ".JPG")


    if not os.path.exists(each_img_path):
        if os.path.exists(each_img_path_2):
            each_img_path = each_img_path_2
        # else:
            # raise ValueError("loss img path")
        continue
    else:
        img = Image.open(each_img_path)
        width, height = img.width, img.height

    a = DeteRes()
    a.img_path = each_img_path
    with open(each_txt_path, "r") as txt_file:
        for each_line in txt_file:
            label, x, y, w, h = each_line.split(" ")
            x = float(x) * width
            y = float(y) * height
            w = float(w) * width
            h = float(h) * height
            #
            x1 = int(x - w/2)
            x2 = int(x + w/2)
            y1 = int(y - h/2)
            y2 = int(y + h/2)

            a.add_obj(x1, y1, x2, y2, tag=str(label))
    save_path = os.path.join(save_dir, each_name + ".xml")
    a.save_to_xml(save_path)







