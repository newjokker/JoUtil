# -*- coding: utf-8  -*-
# -*- author: jokker -*-

"""
* uc 推荐系统，用于辅助标注，
* 根据当前已有标签的分布情况，和每个标签的权重，决定哪些数据标注的优先级比较大
* 推荐指数 = 迫切指数 * 权重
* 迫切指数 = abs（标签数量平均值 - 指定标签数量）/ 指定标签数量
"""



# 保存 json 数据的 pkl 文件
pkl_dir = r""
# 需要进行推荐的数据的 xml_dir
xml_dir = r""
# 权重文件路径
weight_path = r""

# todo 读取 json 分析结果的 json，获得 推荐指数












