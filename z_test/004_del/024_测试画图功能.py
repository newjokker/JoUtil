# -*- coding: utf-8  -*-
# -*- author: jokker -*-


from JoTools.txkjRes.deteRes import DeteRes

img_path = r"C:\Users\14271\Desktop\del\斜框\test.jpg"
xml_path = r"C:\Users\14271\Desktop\del\斜框\test.xml"

a = DeteRes()
a.xml_path = xml_path
a.img_path = img_path


a.draw_dete_res(r"C:\Users\14271\Desktop\del\res.jpg")