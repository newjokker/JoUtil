# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import cv2
import numpy as np
from JoTools.txkjRes.deteRes import DeteRes
import matplotlib.pyplot as plt


img_path = r"C:\Users\14271\Desktop\del\test\00fa186e8d4d6660b49ddef8a35a77de.jpg"
xml_path = r"C:\Users\14271\Desktop\del\test\00fa186e8d4d6660b49ddef8a35a77de.xml"
save_xml_path = r"C:\Users\14271\Desktop\del\test\save_002.xml"

a = DeteRes(xml_path)
# a.img_path = img_path

img_ndarry = cv2.imdecode(np.fromfile(img_path, dtype=np.uint8), 1)
img_ndarry = cv2.cvtColor(img_ndarry, cv2.COLOR_BGR2RGB)
a.img_ndarry = img_ndarry


for each_dete_obj in a:

    b = a.get_sub_img_by_dete_obj_new(each_dete_obj, RGB=True)
    # b = a.get_sub_img_by_dete_obj(each_dete_obj, RGB=True)

    plt.imshow(b)
    plt.show()









