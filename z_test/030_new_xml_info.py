# -*- coding: utf-8  -*-
# -*- author: jokker -*-

from JoTools.txkjRes.deteRes import DeteRes, DeteObj, DeteAngleObj

a = DeteRes()
a.height = 300
a.width = 300
a.file_name = 'test'
#
a.add_obj(100, 100, 200, 200, '001', 0.5, -1)
a.add_obj(100, 100, 200, 200, '001', 0.5, -1, 'describe_002')
a.add_obj(100, 100, 200, 200, '001', 0.5, -1, 'describe_003')
# a.save_to_xml('./001.xml')


# a.print_as_fzc_format()

json_info = a.save_to_json()

b = DeteRes(json_dict=json_info)

b.print_as_fzc_format()




# b = DeteRes(xml_path='./001.xml')
#
# for each in b:
#     print(each.des)
