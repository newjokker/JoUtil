# -*- coding: utf-8  -*-
# -*- author: jokker -*-

from JoTools.txkj.eagleUtil import EagleOperate


# imgDir = r"D:\算法培育-7月样本"
# eagle_library = r"C:\Users\14271\Desktop\del\peiyu07.library"

# imgDir = r"D:\算法培育-6月样本"
# eagle_library = r"D:\peiyu06.library"

eagle_library = r"C:\Users\14271\Desktop\del\test_fzc2.library"
imgDir = r"C:\Users\14271\Desktop\test_data\img"

a = EagleOperate(eagle_library, imgDir)
a.init_edgal_project(imgDir)

# a.save_to_xml_img(r"C:\Users\14271\Desktop\del\new_res")


