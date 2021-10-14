# -*- coding: utf-8  -*-
# -*- author: jokker -*-

# todo 获取 json 文件，文件名为 md5 值，region_name 为之前的值

import os
import shutil
from JoTools.utils.HashlibUtil import HashLibUtil
from JoTools.utils.FileOperationUtil import FileOperationUtil
from JoTools.utils.JsonUtil import JsonUtil


img_dir = r"C:\Users\14271\Desktop\newpicDir"
save_dir = r"C:\Users\14271\Desktop\img_dir"
json_info = []



for each_img_path in FileOperationUtil.re_all_file(img_dir, endswitch=['.jpg', '.JPG']):
    md5_str = HashLibUtil.get_file_md5(each_img_path)
    save_img_path = os.path.join(save_dir, '{0}.jpg'.format(md5_str))
    shutil.move(each_img_path, save_img_path)

    json_info.append({
        "originFileName": os.path.split(each_img_path)[1],
        "fileName": md5_str + '.jpg'
    })

    print(md5_str)

JsonUtil.save_data_to_json_file(json_info, r"C:\Users\14271\Desktop\pictureName.json")









