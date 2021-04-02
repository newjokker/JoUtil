# -*- coding: utf-8  -*-
# -*- author: jokker -*-


from JoTools.txkjRes.deteRes import DeteRes

img_path = r"C:\Users\14271\Desktop\del\kkx_demo\test\test.jpg"
xml_path = r"C:\Users\14271\Desktop\del\kkx_demo\test\test.xml"

a = DeteRes()
a.xml_path = xml_path
a.img_path = img_path


# a.draw_dete_res(r"C:\Users\14271\Desktop\res.jpg")


xk = a.get_dete_obj_by_id(1)

Lm = a.get_dete_obj_by_id(0)


a.filter_by_mask(mask=xk.get_points(), cover_index_th=0.5, need_in=True)


for each in a.get_fzc_format():
    print(each)


print("ok")

