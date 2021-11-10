# -*- coding: utf-8  -*-
# -*- author: jokker -*-


from JoTools.txkjRes.deteRes import DeteRes

# img_path = r"C:\Users\14271\Desktop\del\del"

xml_path = r"C:\Users\14271\Desktop\del\del\test.xml"


a = DeteRes(xml_path)

# print(a[0])

dete_obj = a[0]

# a.del_dete_obj(dete_obj)

# a.filter_by_tags(remove_tag=['del', 'ok'])
a.filter_by_tags(need_tag=['del', 'ok'])

a.print_as_fzc_format()




