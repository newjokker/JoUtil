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

intersection = mask.intersection(a)

union = ljc.union(mask)

diff = a.difference(ljc)

diff.print_as_fzc_format()


print(a.issubset(ljc))
print(a.isupperset(ljc))

mask.add_obj_2(ljc.alarms[0])

ljc.print_as_fzc_format()
print('-'*100)
mask.print_as_fzc_format()
print('-'*100)
# ljc.intersection_update(mask)

ljc.difference_update(mask)

ljc.print_as_fzc_format()



















