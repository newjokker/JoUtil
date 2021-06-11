# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import os
import shutil
from JoTools.for_csdn.word_pic.word_pic import WordImage
from PIL import Image
from JoTools.operateDeteRes import OperateDeteRes
from JoTools.txkjRes.deteRes import DeteRes
from JoTools.utils.FileOperationUtil import FileOperationUtil



img_dir = r"C:\Users\14271\Desktop\updata_step_1_train_data\crop_fix_by_ldq\fzc"


for each_img_path in FileOperationUtil.re_all_file(img_dir, endswitch=['.jpg']):
    img_name = os.path.split(each_img_path)[1]
    real_img_name = "_".join(img_name.split("_")[1:])

    real_img_path = os.path.join(img_dir, real_img_name)

    print(real_img_name)

    shutil.move(each_img_path, real_img_path)
