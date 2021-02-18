# -*- coding: utf-8  -*-
# -*- author: jokker -*-


from JoTools.operateDeteRes import OperateDeteRes


region_img_dir = r"C:\Users\14271\Desktop\fzc_train_new\img"
crop_img_dir = r"C:\Users\14271\Desktop\fzc_train_new\crop_new"
save_dir = r"C:\Users\14271\Desktop\fzc_train_new\xml_new"


OperateDeteRes.get_xml_from_crop_img(crop_img_dir, region_img_dir, save_xml_dir=save_dir)
