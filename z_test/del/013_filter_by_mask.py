# -*- coding: utf-8  -*-
# -*- author: jokker -*-

from JoTools.txkjRes.deteRes import DeteRes
from JoTools.txkjRes.deteObj import DeteObj


xml_path = r"C:\Users\14271\Desktop\del\del\00fa186e8d4d6660b49ddef8a35a77de.xml"
img_path = r"C:\Users\14271\Desktop\del\del\00fa186e8d4d6660b49ddef8a35a77de.jpg"

a = DeteRes(xml_path=xml_path, assign_img_path=img_path)


a.add_obj(10,10,100,100,'test')
a.add_obj(50,50,70,70,'test')


mask = DeteObj(20,20, 80, 80, 'all')

a.filter_by_mask(mask.get_points(), update=True, cover_index_th=0.5, need_in=True)

a.print_as_fzc_format()










