# -*- coding: utf-8  -*-
# -*- author: jokker -*-

from JoTools.txkjRes.deteRes import DeteRes


xml_path = r"C:\Users\14271\Desktop\merge\8555a4902f5f9a1a28b3bf1373e4c285.xml"

a = DeteRes(xml_path)

a.do_nms(0.3)

print(len(a))

a.print_as_fzc_format()


