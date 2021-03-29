# -*- coding: utf-8  -*-
# -*- author: jokker -*-



import os
import shutil

img_dir = r"C:\Users\14271\Desktop\10kV_part3"

all_data_dir = r"C:\Users\14271\Desktop\10kV_total_data"


for each_name in os.listdir(img_dir):
    # each_img_path = os.path.join(img_dir, each_name)
    each_xml_path = os.path.join(all_data_dir, each_name[:-4] + '.xml')
    new_xml_path = os.path.join(img_dir, each_name[:-4] + '.xml')

    if os.path.exists(each_xml_path):
        shutil.copy(each_xml_path, new_xml_path)


