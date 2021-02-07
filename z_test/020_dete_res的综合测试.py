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

a = DeteRes()

a.xml_path = xml_path
a.height = 21
a.width = 20

a.img_path = img_path

print(a.width)
print(a.height)


a.refresh_obj_id()


# a.crop_and_save(save_dir, augment_parameter=[0.3,0.3,0.3,0.3])

a.crop_angle_and_save(save_dir, augment_parameter=[0.5, 0.5], split_by_tag=True)

crop_dir = r"C:\Users\14271\Desktop\del\crop\crop"
region_img_dir = r"C:\Users\14271\Desktop\del"
save_xml_dir = crop_dir
# OperateDeteRes.get_xml_from_crop_img(crop_dir, region_img_dir, save_xml_dir)



