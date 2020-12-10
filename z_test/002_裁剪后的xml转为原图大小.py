# -*- coding: utf-8  -*-
# -*- author: jokker -*-



from JoTools.txkj.parseXml import parse_xml
from JoTools.operateResXml import OperateResXml
from JoTools.detectionResult import OperateDeteRes, DeteRes
from JoTools.for_csdn.word_pic.word_pic import WordImage
from JoTools.utils.FileOperationUtil import FileOperationUtil
import os



xml_dir = r"C:\Users\14271\Desktop\优化开口销第二步\018_循环优化训练数据\001_未优化前裁剪xml"
img_dir = r"C:\Users\14271\Desktop\优化开口销第二步\000_原始数据_Part_CY-JTM_OrignalPic-Xml20200515\img_002"
save_dir = r"C:\Users\14271\Desktop\优化开口销第二步\018_循环优化训练数据\000_转为原图大小xml"


for each_xml_path in FileOperationUtil.re_all_file(xml_dir, lambda x:str(x).endswith('.xml')):
    print((each_xml_path))
    # each_img_name = os.path.split(each_xml_path)[1][:-4] + '.JPG'
    # each_img_path = os.path.join(img_dir, each_img_name)

    DeteRes.get_region_xml_from_cut_xml(each_xml_path, save_dir, img_dir)

