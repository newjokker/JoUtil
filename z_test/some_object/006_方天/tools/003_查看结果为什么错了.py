# -*- coding: utf-8  -*-
# -*- author: jokker -*-


from JoTools.utils.JsonUtil import JsonUtil
import numpy as np
from JoTools.txkjRes.deteRes import DeteRes
import os

json_path = r"D:\AppData\baiduwangpan\lyy\defect20211015.json"

save_dir = r"D:\AppData\baiduwangpan\lyy\xml_gt"

a = JsonUtil.load_data_from_json_file(json_path)

task_list = a['taskList']


algo_list = set()

code_dict = {}



for i in range(len(task_list)):
    each_img = task_list[i]

    if 'imgList' not in each_img:
        continue

    img_list = each_img['imgList']

    for each_img_list in img_list:

        each_dete_res = DeteRes()
        img_name = each_img_list['imgName']
        # img_name = each_img_list['id']
        img_id = each_img_list['id']

        # each_dete_res.file_name = img_name
        # each_dete_res.file_name = img_id + '.JPG'
        # each_dete_res.img_path = os.path.join(r"D:\AppData\baiduwangpan\lyy\pic", img_id + '.JPG')

        if 'defectList' not in each_img_list:
            continue

        default_list= each_img_list['defectList']

        for each in default_list:
            # fixme 有土星的，有其他厂家的，其他厂家的也是对的
            if 'algorithmFactoryId' in each:

                algo_id = each['algorithmFactoryId']

                # if algo_id == "tuxingkeji":

                x_min, y_min, x_max, y_max = each['xMin'], each['yMin'], each['xMax'], each['yMax']
                code = {"3ADC":'lyy', "D220":'yk', '8898':'ft', 'tuxi':'txkj'}[algo_id[:4]] + '_' + each['defectType']
                box_type = each['boxType']

                if box_type != 1:
                    print(algo_id, box_type, img_id, img_name)
                    # print(img_id)
                else:
                    pass
                    # print(algo_id, box_type, img_id, img_name)

        #         if code in code_dict:
        #             code_dict[code].append(((x_max - x_min)/(y_max - y_min)))
        #         else:
        #             code_dict[code] = [((x_max - x_min)/(y_max - y_min))]
        #
        #
        #         each_dete_res.add_obj(x1=x_min, y1=y_min, x2=x_max, y2=y_max, tag=code, describe=algo_id)
        #
        # save_xml_path = os.path.join(save_dir, each_dete_res.file_name[:-4] + '.xml')
        #
        # if os.path.exists(save_xml_path):
        #     aa = DeteRes(save_xml_path)
        #     each_dete_res += aa
        #     print("* 重复")
        #     if len(each_dete_res) > 0:
        #         each_dete_res.save_to_xml(save_xml_path)
        # else:
        #     if len(each_dete_res) > 0:
        #         each_dete_res.save_to_xml(save_xml_path)
        #









# print(algo_list)
#
# for each in code_dict:
#     print(each, np.mean(code_dict[each]))
#
#
# # print(img_1)
#
# print(len(img_1))
#



