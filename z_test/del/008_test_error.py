# -*- coding: utf-8  -*-
# -*- author: jokker -*-

from JoTools.txkjRes.deteRes import DeteRes

xml_path = r"C:\Users\14271\Desktop\del\del\0a4dd4915abc8d675ce190eef87e38ca.xml"


a = DeteRes(xml_path)


for each_obj in a:
    each_obj.tag = "hehe"
    # each_obj.like = "hehe"
    each_obj.name = "jokker"

a.print_as_fzc_format()

b = DeteRes(json_dict=a.save_to_json())
b.print_as_fzc_format()
