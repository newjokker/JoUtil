# -*- coding: utf-8  -*-
# -*- author: jokker -*-

from JoTools.txkjRes.deteRes import DeteRes


xml_path = r"C:\Users\14271\Desktop\del\1522379753085-dachicun.xml"
img_path = r"C:\Users\14271\Desktop\del\1522379753085-dachicun.jpg"
save_img_path = r"C:\Users\14271\Desktop\del\1522379753085-dachicun_new.jpg"

a = DeteRes(xml_path, assign_img_path=img_path)
a.refresh_obj_id()


# a.angle_obj_to_obj()

a.do_nms(0.15, ignore_tag=True)

a.draw_dete_res(save_img_path)


for each in a.alarms:
    print(each.id)
