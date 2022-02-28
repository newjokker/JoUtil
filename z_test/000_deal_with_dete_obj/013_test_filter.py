# -*- coding: utf-8  -*-
# -*- author: jokker -*-


from JoTools.txkjRes.deteRes import DeteObj, DeteRes


a = DeteRes(r"C:\Users\14271\Desktop\del\del.xml")

a[2].tag = 'fzc_broken'
a[4].tag = 'test'
a[1].conf = 0.6


# b = a.filter_by_attr("x1", 1155, update=False)
# b = a.update_attr_for_all_obj("x1", 1155, update=False)

# for each_dete_obj in a:
#     print(each_dete_obj.get_area())


b = a.filter_by_area(10650, update=False, mode='lt')
# b = a.filter_by_tags(remove_tag=['Fnormal'], update=True)
# b = a.filter_by_conf(0.5, update=False, mode='gt')

b.print_as_fzc_format()

print('-'*100)

a.print_as_fzc_format()
