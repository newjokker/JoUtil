# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import os
from JoTools.utils.JsonUtil import JsonUtil
from JoTools.utils.HashlibUtil import HashLibUtil
from JoTools.utils.FileOperationUtil import FileOperationUtil
from JoTools.txkjRes.deteRes import DeteRes
from JoTools.operateDeteRes import OperateDeteRes

img_dir = r"C:\data\fzc_优化相关资料\dataset_fzc\000_train_data_step_1\Annotations"

for each in OperateDeteRes.get_class_count(img_dir).items():
    print(each)

exit()

index = 0
for each_xml_path in FileOperationUtil.re_all_file(img_dir, lambda x:str(x).endswith(('.xml'))):

    a = DeteRes()
    a.xml_path = each_xml_path

    # 替换字典
    # a.update_tags({"040303021":'broken', '040303022':'broken', '040303000':'fzc', '040303011':'fzc', '040303031':'fzc', '040303041':'fzc'})
    a.update_tags({"fzc_broken":'fzc_yt'})

    # a.do_nms(0.3, ignore_tag=True)


    a.save_to_xml(each_xml_path)

# res = OperateDeteRes.get_class_count(img_dir)
#
# for each in res.items():
#     print(each)