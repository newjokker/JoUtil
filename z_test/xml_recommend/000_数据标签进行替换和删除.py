# -*- coding: utf-8  -*-
# -*- author: jokker -*-


from JoTools.txkjRes.deteRes import DeteRes
from JoTools.utils.FileOperationUtil import FileOperationUtil
from JoTools.operateDeteRes import OperateDeteRes

# --------------------------------------------

xml_dir = r"C:\Users\14271\Desktop\xml_recommend\Annonations_extra"

# fzc, nc, (LXJT_set, YJXJ_sub, XCXJCT_sub, ), (fhjyz, bljyz, tcjyz), (ring, ringL)
update_dict = {"LXJT_set": "xj", "YJXJ_sub": "xj", "XCXJCT_sub": "xj", "fhjyz":"jyz", "bljyz":"jyz", "tcjyz":"jyz", "ring":"ring", "ringL":"ringL"}

need_tags = ["fzc", "nc", "xj", "jyz", "ring"]

# --------------------------------------------

for each_xml_path in FileOperationUtil.re_all_file(xml_dir, endswitch=['.xml']):
    a = DeteRes(each_xml_path)
    a.update_tags(update_dict=update_dict)
    a.filter_by_tags(need_tag=need_tags)
    a.save_to_xml(each_xml_path)

OperateDeteRes.get_class_count(xml_dir, print_count=True)













