# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import os
from JoTools.utils.LivpUtil import LivpUtil


livp_dir = r"C:\Users\14271\Desktop\del\livp\img"
temp_folder = r"C:\Users\14271\Desktop\del\livp\tmp"
save_folder = r"C:\Users\14271\Desktop\del\livp\res"

for each_name in os.listdir(livp_dir):
    file_path = os.path.join(livp_dir, each_name)
    # 解压为 .heic 文件
    uzip_path = LivpUtil.unzip_to_heic(file_path, temp_folder)
    # 继续解析为 jpg 文件
    uzip_name = os.path.split(uzip_path)[1]
    save_path = os.path.join(save_folder, uzip_name[:-4] + 'jpg')
    LivpUtil.heic_to_jpg(uzip_path, save_path)