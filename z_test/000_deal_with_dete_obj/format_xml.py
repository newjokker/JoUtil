# -*- coding: utf-8  -*-
# -*- author: jokker -*-
import os.path
import shutil
import sys
import argparse
import os
from JoTools.utils.FileOperationUtil import FileOperationUtil
from JoTools.utils.HashlibUtil import HashLibUtil


xml_dir = r"C:\Users\14271\Desktop\del\save_img\img"
save_dir = r"C:\Users\14271\Desktop\del\save_img\rename"

index = 0
for each_img_path in FileOperationUtil.re_all_file(xml_dir, endswitch=['.jpg', '.JPG', '.png', '.PNG']):
    index += 1
    print(index, each_img_path)
    md5 = HashLibUtil.get_file_md5(each_img_path)
    suffix = FileOperationUtil.bang_path(each_img_path)[2]
    save_path = os.path.join(save_dir, md5 +  suffix)
    shutil.move(each_img_path, save_path)








