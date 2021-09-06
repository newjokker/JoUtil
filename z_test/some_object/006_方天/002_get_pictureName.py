# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import shutil
import os
import random
from JoTools.txkjRes.deteRes import DeteRes
from JoTools.utils.FileOperationUtil import FileOperationUtil
from JoTools.utils.JsonUtil import JsonUtil
from JoTools.utils.RandomUtil import RandomUtil


img_dir = r"C:\Users\14271\Desktop\方天测试集准备"
save_json_path = r"C:\Users\14271\Desktop\pictureName.json"

json_info = []

key_word_list = ["杆塔", "导地线", "绝缘子", "大金具", "小金具", "基础", "通道环境", "接地装置", "附属设施", ""]

def get_key_word_str():
    key_word_set = set()
    repeat_num = RandomUtil.randrange(1, 5)
    for _ in range(repeat_num):
        key_word_set.add(random.choice(key_word_list))
    return "_".join(key_word_set)


index = 0
for each_img_path in FileOperationUtil.re_all_file(img_dir, endswitch=['.jpg']):
    index += 1
    each_img_name = os.path.split(each_img_path)[1]

    json_info.append({
        "originFileName":each_img_name,
        "fileName": each_img_name[:-4] + "_" + get_key_word_str() + each_img_name[-4:]
    })

JsonUtil.save_data_to_json_file(json_info, save_json_path)



















