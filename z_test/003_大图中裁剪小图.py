# -*- coding: utf-8  -*-
# -*- author: jokker -*-


import os
import shutil
from JoTools.operateDeteRes import OperateDeteRes



xml_dir = r"C:\Users\14271\Desktop\del\img_xml"
img_dir = r"C:\Users\14271\Desktop\del\img_xml"
save_dir = r"C:\Users\14271\Desktop\del\crop"


OperateDeteRes.crop_imgs(img_dir, xml_dir, save_dir, split_by_tag=True, exclude_tag_list=['correct_K', 'correct_K_Lm', 'correct_Xnormal'], augment_parameter=[0.3,0.3,0.3,0.3])

