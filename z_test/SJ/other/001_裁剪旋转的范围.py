# -*- coding: utf-8  -*-
# -*- author: jokker -*-


from JoTools.txkjRes.todo.deteAngleRes import DeteAngleRes
from JoTools.operateDeteRes import OperateDeteRes


# img_path  = r"C:\Users\14271\Desktop\del\crop"
# xml_path = r"C:\Users\14271\Desktop\del\test.xml"
# save_dir = r"C:\Users\14271\Desktop\del\crop"


img_dir = r"C:\Users\14271\Desktop\110kv标注\10kV_part2 - 副本\img"
xml_dir = r"C:\Users\14271\Desktop\110kv标注\10kV_part2 - 副本\xml"
save_dir = r"C:\Users\14271\Desktop\110kv标注\10kV_part2 - 副本\crop"

# a = DeteAngleRes(xml_path=xml_path, assign_img_path=img_path)
# a.crop_and_save(save_dir)

# OperateDeteRes.get_xml_from_crop_img_angle(img_path, r"C:\Users\14271\Desktop\del", r"C:\Users\14271\Desktop\del\new_res")

OperateDeteRes.crop_imgs_angles(img_dir=img_dir, xml_dir=xml_dir, save_dir=save_dir)