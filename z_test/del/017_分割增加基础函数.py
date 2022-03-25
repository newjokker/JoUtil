# -*- coding: utf-8  -*-
# -*- author: jokker -*-


from JoTools.txkjRes.segmentRes import SegmentRes, SegmentOpt
from JoTools.utils.FileOperationUtil import FileOperationUtil



json_dir = r"C:\Users\14271\Desktop\xj_train\002_数据汇总"
save_dir = r"C:\Users\14271\Desktop\xj_train\003_统一标签"


print(SegmentOpt.count_tag(save_dir))

# SegmentOpt.update_tags(json_dir=json_dir, save_dir=save_dir, update_dict={"ct": "chuanti", "gb":"guaban", "line":"chuanti", "xianjia":"guaban"})

# print(SegmentOpt.count_tag(save_dir))

# index = 0
# index_2 = 0
# index_0 = 0
#
# for each_json_path in FileOperationUtil.re_all_file(save_dir, endswitch=[".json"]):
#
#     index_0 += 1
#
#     a = SegmentRes(each_json_path)
#     a.parse_json_info()
#     each_count = a.count_tags()
#
#     if ("chuanti" not in each_count) or ("guaban" not in each_count):
#         print(each_count)
#         print("无标签", each_json_path)
#         index += 1
#     else:
#         if each_count["chuanti"] != each_count["guaban"]:
#             print("标签个数不等", each_json_path)
#             index_2 += 1
#
# print(index, index_2, index_0)





