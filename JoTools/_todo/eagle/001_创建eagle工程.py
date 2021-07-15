# -*- coding: utf-8  -*-
# -*- author: jokker -*-

from JoTools.txkj.eagleUtil import EagleOperate


# imgDir = r"D:\算法培育-7月样本"
# eagle_library = r"C:\Users\14271\Desktop\del\peiyu07.library"

# imgDir = r"D:\算法培育-6月样本"
# eagle_library = r"D:\peiyu06.library"

eagle_library = r"D:\WuHan_05.library"
imgDir = r"D:\国网四川省电力公司地市公司2016年9-12月巡检影像02\2021年5月算法培育1"

a = EagleOperate(eagle_library, imgDir)
# 指定当前项目的前缀，不同的项目用不同的前缀就能合并了
a.assign_id_pre = "WH05"
a.init_edgal_project(imgDir)

