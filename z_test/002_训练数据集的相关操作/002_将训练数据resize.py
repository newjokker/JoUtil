# -*- coding: utf-8  -*-
# -*- author: jokker -*-


from JoTools.operateDeteRes import OperateDeteRes

img_dir = r"C:\Users\14271\Desktop\del\resize\img"
xml_dir = r"C:\Users\14271\Desktop\del\resize\xml"
save_dir = r"C:\Users\14271\Desktop\del\resize\res"



OperateDeteRes.resize_train_data(img_dir=img_dir, xml_dir=xml_dir, save_dir=save_dir, resize_ratio=0.5)



