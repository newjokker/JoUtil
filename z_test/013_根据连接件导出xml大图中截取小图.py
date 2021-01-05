# -*- coding: utf-8  -*-
# -*- author: jokker -*-


from JoTools.txkjRes.detectionResult import DeteRes
from JoTools.utils.FileOperationUtil import FileOperationUtil
import os



xml_dir = r"C:\Users\14271\Desktop\优化开口销第二步\019_训练图中增加按照连接件进行截取的图\add_other_训练图\Annotations"
img_dir = r"C:\Users\14271\Desktop\优化开口销第二步\019_训练图中增加按照连接件进行截取的图\add_other_训练图\JPEGImages"
save_dir = r"C:\Users\14271\Desktop\优化开口销第二步\019_训练图中增加按照连接件进行截取的图\截取连接件后的训练图"

# 记录图像中需要截取的范围
region_xml_dir = r"C:\Users\14271\Desktop\优化开口销第二步\019_训练图中增加按照连接件进行截取的图\kkx_训练图_连接件_02"

index = 0
for each_xml_path in FileOperationUtil.re_all_file(xml_dir, lambda x:str(x).endswith('.xml')):
    index += 1
    print(index, each_xml_path)
    each_img_name = os.path.split(each_xml_path)[1][:-4] + '.JPG'
    each_img_path = os.path.join(img_dir, each_img_name)
    # 找到对应的截取区域 xml
    each_region_xml_path = os.path.join(region_xml_dir, each_img_name[:-4] + '.xml')
    # xml_info = parse_xml(each_region_xml)

    if not os.path.exists(each_img_path):
        raise ValueError('path error : {0}'.format(each_img_path))

    if not os.path.exists(each_region_xml_path):
        print("loss {0}".format(each_region_xml_path))
        continue

    region_dete_res = DeteRes(each_region_xml_path)
    a = DeteRes(each_xml_path, each_img_path)

    for each_region in region_dete_res.alarms:
        assign_region = each_region.get_rectangle()
        # print(assign_region)
        a.save_assign_range(assign_region, save_dir=save_dir)
