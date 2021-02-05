# -*- coding: utf-8  -*-
# -*- author: jokker -*-

from JoTools.txkjRes.deteRes import DeteRes


xml_path = r"C:\Users\14271\Desktop\del\1522379753085-dachicun.xml"
img_path = r"C:\Users\14271\Desktop\del\1522379753085-dachicun.jpg"
save_img_path = r"C:\Users\14271\Desktop\del\1522379753085-dachicun_new.jpg"
save_json_path = r"C:\Users\14271\Desktop\del\1522379753085-dachicun_new.json"

a = DeteRes(xml_path, assign_img_path=img_path)
a.refresh_obj_id()


other_dete_obj = a.del_by_tages(['Other'])

# a.angle_obj_to_obj()

# a.do_nms(0.15, ignore_tag=True)
for each_other in other_dete_obj:
    a.filter_by_mask(each_other.get_points(), need_in=True)

a.draw_dete_res(save_img_path)

a.save_to_json()

for each in a.alarms:
    print(each.id)
