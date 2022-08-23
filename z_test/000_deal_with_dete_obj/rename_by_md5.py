# -*- coding: utf-8  -*-
# -*- author: jokker -*-
import os
import shutil
from JoTools.utils.FileOperationUtil import FileOperationUtil
from JoTools.utils.HashlibUtil import HashLibUtil

img_dir = r"C:\Users\14271\Desktop\缺陷图片-del20220820"

for each_img_path in FileOperationUtil.re_all_file(img_dir, endswitch=[".jpg", ".JPG"]):

    md5 = HashLibUtil.get_file_md5(each_img_path)
    new_path = os.path.split(each_img_path)[0] + os.sep + md5 + each_img_path[-4:]
    shutil.move(each_img_path, new_path)
    print(new_path)