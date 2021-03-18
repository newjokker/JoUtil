# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import os
import shutil
from JoTools.txkjRes.deteRes import DeteRes
from JoTools.txkj.eagleUtil import EagleMetaData
from JoTools.utils.FileOperationUtil import FileOperationUtil


# 读取 image 文件夹中的信息，查看 json 文件中是否有需要的类型，有的话直接

# todo 将一个 image 文件转为一个 DeteRes 信息

# todo 需要的 code，040500021,040500022,040500023,040501031,040501032,040501033

# assign_code_list = ['040500021','040500022','040500023','040501031','040501032','040501033']
assign_code_list = ['040303021', '040303022']

save_dir = r"C:\Users\14271\Desktop\del\新防振锤数据武汉电科院"

img_dir_list = [r"\\192.168.3.80\数据\9eagle数据库\peiyu_06.library\images",
                r"\\192.168.3.80\数据\9eagle数据库\peiyu_07.library\images",
                r"\\192.168.3.80\数据\9eagle数据库\peiyu_11.library\images"]


for dir_index, img_dir in enumerate(img_dir_list):

    for index, each_json_path in enumerate(FileOperationUtil.re_all_file(img_dir, lambda x:str(x).endswith('.json'))):

        try:

            print(dir_index, index, each_json_path)
            b = DeteRes()
            a = EagleMetaData()
            a.load_atts_from_json(each_json_path)
            b.img_path = os.path.join(os.path.dirname(each_json_path), a.name + '.jpg')

            if not os.path.exists(b.img_path):
                continue

            if a.comments is None:
                continue

            for each_comment in a.comments:
                x1 = int(each_comment['x'])
                y1 = int(each_comment['y'])
                x2 = int(each_comment['width']) + x1
                y2 = int(each_comment['height']) + y1
                tag = str(each_comment['annotation']).split('_')[0]
                b.add_obj(x1,y1,x2,y2,tag=tag,conf=-1)


            if b.has_tag('040303021') or b.has_tag('040303022'):
                # 存在防振锤，需要进行复制文件
                each_xml_name = os.path.split(b.file_name)[1][:-3] + 'xml'
                each_save_img_name = os.path.split(b.file_name)[1][:-3] + 'jpg'
                each_xml_path = os.path.join(save_dir, each_xml_name)
                each_save_img_path = os.path.join(save_dir, each_save_img_name)

                # print(each_xml_path)
                # print(each_save_img_path)

                b.filter_by_tages(need_tag=['040303021', '040303022', '040303000', '040303011', '040303031', '040303041'])
                b.save_to_xml(each_xml_path)
                shutil.copy(b.img_path, each_save_img_path)

            # b.crop_and_save(r"C:\Users\14271\Desktop\del\crop", split_by_tag=True, include_tag_list=assign_code_list, augment_parameter=[0.1,0.1,0.1,0.1])

        except Exception as e:
            print(e)

    # print(a.name)
    # print(a.comments)



