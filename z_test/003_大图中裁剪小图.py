# -*- coding: utf-8  -*-
# -*- author: jokker -*-


import os
import shutil
from JoTools.operateDeteRes import OperateDeteRes



xml_dir = r"C:\Users\14271\Desktop\compare\old_compare"
img_dir = r"C:\Users\14271\Desktop\优化开口销第二步\000_标准测试集\NM_standerd_pic"
save_dir = r"C:\Users\14271\Desktop\compare\old_crop"


OperateDeteRes.crop_imgs(img_dir, xml_dir, save_dir, split_by_tag=True, exclude_tag_list=['correct_K', 'correct_K_Lm', 'correct_Xnormal'])

