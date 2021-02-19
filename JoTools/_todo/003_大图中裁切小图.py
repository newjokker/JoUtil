# -*- coding: utf-8  -*-
# -*- author: jokker -*-



import os
from JoTools.txkjRes.deteObj import DeteObj
from JoTools.txkjRes.deteRes import DeteRes
from JoTools.operateDeteRes import OperateDeteRes



xml_dir = r"C:\Users\14271\Desktop\fzc_train_new\xml_new"
img_dir = r"C:\Users\14271\Desktop\fzc_train_new\img"
save_dir = r"C:\Users\14271\Desktop\fzc_train_new\crop"


OperateDeteRes.crop_imgs(img_dir, xml_dir, save_dir, split_by_tag=True)
# OperateDeteRes.crop_imgs(img_dir, xml_dir, save_dir, split_by_tag=True, augment_parameter=[0.3, 0.3, 0.3, 0.3], exclude_tag_list=["fzc_yt", "fzc_gt", "fzc_sm", "qx_gt", "qx_sm", "qx_yt"])
