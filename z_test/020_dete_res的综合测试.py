# -*- coding: utf-8  -*-
# -*- author: jokker -*-

from JoTools.txkjRes.deteRes import DeteRes
from JoTools.operateDeteRes import OperateDeteRes

xml_path = r"C:\Users\14271\Desktop\del\1522379753085-dachicun.xml"
img_path = r"C:\Users\14271\Desktop\del\1522379753085-dachicun.jpg"
save_dir = r"C:\Users\14271\Desktop\del\crop"
save_img_path = r"C:\Users\14271\Desktop\del\1522379753085-dachicun_new.jpg"
save_json_path = r"C:\Users\14271\Desktop\del\1522379753085-dachicun_new.json"
save_xml_path = r"C:\Users\14271\Desktop\del\1522379753085-dachicun_new.xml"

a = DeteRes(xml_path, assign_img_path=img_path)
a.refresh_obj_id()


a.crop_and_save(save_dir, augment_parameter=[0.3,0.3,0.3,0.3])

crop_dir = r"C:\Users\14271\Desktop\del\crop\crop"
region_img_dir = r"C:\Users\14271\Desktop\del"
save_xml_dir = crop_dir
OperateDeteRes.get_xml_from_crop_img(crop_dir, region_img_dir, save_xml_dir)