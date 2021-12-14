# -*- coding: utf-8  -*-
# -*- author: jokker -*-


from JoTools.txkjRes.deteRes import DeteRes


img_path = r"C:\Users\14271\Desktop\rustDebug\test.jpg"
xml_path = r"C:\Users\14271\Desktop\rustDebug\test.xml"
save_path = r"C:\Users\14271\Desktop\rustDebug\res.jpg"


a = DeteRes(xml_path=xml_path, assign_img_path=img_path)

mask = a.deep_copy()
mask.filter_by_tags(need_tag=['mask'])


mask.print_as_fzc_format()

print('-'*100)

a.print_as_fzc_format()

b = a - mask

print('-'*100)


b.print_as_fzc_format()
