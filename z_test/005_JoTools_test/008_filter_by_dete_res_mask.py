# -*- coding: utf-8  -*-
# -*- author: jokker -*-

from JoTools.txkjRes.deteRes import DeteRes


img_path = r"C:\Users\14271\Desktop\rustDebug\test.jpg"
xml_path = r"C:\Users\14271\Desktop\rustDebug\test.xml"
save_path = r"C:\Users\14271\Desktop\rustDebug\res.jpg"


a = DeteRes(xml_path=xml_path, assign_img_path=img_path)

mask = a.deep_copy()
mask.filter_by_tags(need_tag=['mask'])
ljc = a.deep_copy()
ljc.filter_by_tags(need_tag=['ljc'])

ljc.filter_by_dete_res_mask(mask)

ljc.draw_dete_res(save_path)


