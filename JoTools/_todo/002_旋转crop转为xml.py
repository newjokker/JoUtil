# -*- coding: utf-8  -*-
# -*- author: jokker -*-



import sys
import cv2
from JoTools.txkjRes.deteAngleXml import parse_xml, save_to_xml
from JoTools.txkjRes.deteAngleRes import DeteAngleRes
from JoTools.operateDeteRes import OperateDeteRes




img_dir = r"C:\Users\14271\Desktop\110kv标注\10kV_part2 - 副本\crop"
region_img_dir = r"C:\Users\14271\Desktop\110kv标注\10kV_part2 - 副本\img"
save_xml_dir = r"C:\Users\14271\Desktop\110kv标注\10kV_part2 - 副本\xml_new"

OperateDeteRes.get_xml_from_crop_img_angle(img_dir, region_img_dir=region_img_dir, save_xml_dir=save_xml_dir)
