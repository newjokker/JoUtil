# -*- coding: utf-8  -*-
# -*- author: jokker -*-


from JoTools.txkj.parseXml import parse_xml
from JoTools.detectionResult import DeteRes
from JoTools.for_csdn.word_pic.word_pic import WordImage
from JoTools.utils.FileOperationUtil import FileOperationUtil
import os



xml_dir = r"C:\Users\14271\Desktop\优化开口销第二步\000_标准测试集\NM_standerd_xml"
img_dir = r"C:\Users\14271\Desktop\优化开口销第二步\000_标准测试集\NM_standerd_pic"
save_dir = r"C:\Users\14271\Desktop\优化开口销第二步\017_新增数据后的结果对比\002_第二步使用验证集进行对比\000_验证集截图"

# xml_path = r"C:\Users\14271\Desktop\del\get_max_range\res\35kV迪洋线017号塔右相大号侧横担端U型挂环销钉缺失-+-[1480_1556_3171_1835].xml"
# DeteRes.get_region_xml_from_cut_xml(xml_path, save_dir)


# exit()

for each_xml_path in FileOperationUtil.re_all_file(xml_dir, lambda x:str(x).endswith('.xml')):
    print((each_xml_path))
    each_img_name = os.path.split(each_xml_path)[1][:-4] + '.JPG'
    each_img_path = os.path.join(img_dir, each_img_name)
    #
    a = DeteRes(each_xml_path, each_img_path)

    if len(a.alarms) >= 2:
        max_range = a.get_max_range()
        a.save_assign_range(max_range, save_dir=save_dir)




# for each_xml_path in FileOperationUtil.re_all_file(xml_dir, lambda x:str(x).endswith('.xml')):
#     DeteRes.get_region_xml_from_cut_xml(each_xml_path, save_dir)
#
#
