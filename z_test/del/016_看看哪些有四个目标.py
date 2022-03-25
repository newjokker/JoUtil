# -*- coding: utf-8  -*-
# -*- author: jokker -*-


from JoTools.txkjRes.segmentRes import SegmentRes
from JoTools.utils.FileOperationUtil import FileOperationUtil


json_dir = r"C:\Users\14271\Desktop\annotations"


for index, each_json_path in enumerate(FileOperationUtil.re_all_file(json_dir, endswitch=['.json'])):

    # print(each_json_path)

    a = SegmentRes(json_path=each_json_path)
    a.parse_json_info()         # json_path=each_json_path

    print(a.shapes)

    if len(a.shapes) > 2:
        print(each_json_path)
    else:
        # print(index, "OK")
        pass

    exit()




