# -*- coding: utf-8  -*-
# -*- author: jokker -*-

"""
* json 分析系统
* 分析 json 太慢了，最好分析基于 json 数据的 pkl 数据，
* 分析结果写到一个标准的 json 中，作为推荐结果的输入数据
* 所有的分析只在一次遍历中实现，不需要多次遍历 pkl 中的 json 信息

"""
from collections import Counter
from JoTools.utils.PickleUtil import PickleUtil
from JoTools.utils.FileOperationUtil import FileOperationUtil
from JoTools.utils.PrintUtil import PrintUtil

# pkl 数据文件夹
pkl_dir = r"C:\Users\14271\Desktop\del\buffer"


def get_info_from_json_info(json_info):
    """从 json_info 中获取基础统计信息"""
    tag_list = []           # 每个标签的个数
    tag_type_list = []      # 每种标注类型的个数，斜框，矩形
    #
    for each_obj in json_info.objects:
        shape_type = each_obj.shape_type
        label = each_obj.label
        tag_list.append(label)
        tag_type_list.append(shape_type)

    return Counter(tag_list), Counter(tag_type_list)


uc_index = 0
tag_counter = Counter()
shape_type_counter = Counter()
#
for each_pkl_path in FileOperationUtil.re_all_file(pkl_dir, endswitch='.pkl'):
    print(each_pkl_path)
    pkl_info = PickleUtil.load_data_from_pickle_file(each_pkl_path)

    for each_uc in pkl_info:
        uc_index += 1
        json_info = pkl_info[each_uc]
        each_tag_counter, each_shape_type_counter = get_info_from_json_info(json_info)
        tag_counter += each_tag_counter
        shape_type_counter += each_shape_type_counter


# print(tag_counter)
# print(shape_type_counter)

PrintUtil.print(tag_counter)
PrintUtil.print(shape_type_counter)

print(f'{uc_index}-' * 5)

# todo 分析每个标签的个数

# todo 分析各个标签的迫切指数

# todo 有多少数据标注了，有多少数据没标注

# todo 每张图标注框的个数的分布，画图

# todo 分析斜框数据和非斜框数据的个数

# todo 分析每天入库数据个数

# todo 增加进度条，作为查看各个部分的进度

# todo 分析图像的长宽分布

# todo 目标的大小分布，目标的中心点分布 (这个在普通分析中不去做，在指定分析中去完善，需要重新遍历一次)



