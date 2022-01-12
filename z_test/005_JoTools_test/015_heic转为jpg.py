# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import os
from JoTools.utils.LivpUtil import LivpUtil
from JoTools.utils.FileOperationUtil import FileOperationUtil


livp_dir = r"/home/ldq/livp2jpg/img/heic"
temp_folder = r"C:\Users\14271\Desktop\del\livp\tmp"
save_folder = r"/home/ldq/livp2jpg/res"


for each_heic_path in FileOperationUtil.re_all_file(livp_dir, endswitch=['.heic']):
    save_path = os.path.join(save_folder, each_heic_path[:-4] + 'jpg')
    LivpUtil.heic_to_jpg(each_heic_path, save_path)