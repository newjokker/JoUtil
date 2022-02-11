# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import os
from JoTools.utils.FileOperationUtil import FileOperationUtil


img_dir = r"C:\Users\14271\Desktop\for_unet_data"

index = 0
for each_img_path in FileOperationUtil.re_all_file(img_dir, endswitch=['.jpg', '.JPG']):
    dir, name, suffix = FileOperationUtil.bang_path(each_img_path)
    each_json_path = os.path.join(img_dir, name + ".json")
    if not os.path.exists(each_json_path):
        index += 1
        print(index, each_img_path)
        print(index, each_json_path)

        os.remove(each_img_path)









