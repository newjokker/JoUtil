# -*- coding: utf-8  -*-
# -*- author: jokker -*-

from JoTools.txkjRes.segmentJson import SegmentJson
from JoTools.utils.FileOperationUtil import FileOperationUtil



json_dir = r"C:\data\004_绝缘子污秽\val\json"

a = SegmentJson()

for each_json_path in list(FileOperationUtil.re_all_file(json_dir, endswitch=['.json']))[20:]:
    a.parse_json_info(each_json_path)

    break

a.print_as_fzc_format()


