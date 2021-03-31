# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import os
import copy
from JoTools.utils.CsvUtil import CsvUtil
from JoTools.utils.FileOperationUtil import FileOperationUtil
from JoTools.txkjRes.deteRes import DeteRes


def merge_xml_get_dete_res(xml_path_list):
    """将 xml 进行合并，获取 DeteRes"""
    if len(xml_path_list) == 1:
        a = DeteRes(xml_path=xml_path_list[0])
    elif len(xml_path_list) > 1:
        a = DeteRes(xml_path=xml_path_list[0])
        for each_assign_xml_path in xml_path_list[1:]:
            each_dete_res = DeteRes(xml_path=each_assign_xml_path)
            a += each_dete_res
    else:
        return None
    return a


def from_out_name_to_code(assign_dete_res):
    """将输出的 tag 映射为对应的 code"""

    new_alarms = []

    for each_dete_obj in assign_dete_res.alarms:
        each_tag = each_dete_obj.tag

        # --------------------------------------------------------------------------------------------------------------
        # 小金具单独处理
        if each_tag.startswith('K') or each_tag.startswith('Lm') or  each_tag.startswith('KG'):
            # 是合并小金具出来的结果
            each_tags = each_tag.split('_')
            # 开口销缺失
            if 'K' in each_tags:
                # 增加
                each_assign_tag_dete_obj = copy.deepcopy(each_dete_obj)
                each_assign_tag_dete_obj.tag = tag_code_dict['K']
                new_alarms.append(each_assign_tag_dete_obj)
            # 小金具锈蚀
            if 'rust' in each_tags:
                # 增加
                each_assign_tag_dete_obj = copy.deepcopy(each_dete_obj)
                if 'Lm' in each_tags:
                    each_assign_tag_dete_obj.tag = tag_code_dict['Lm_rust']
                    new_alarms.append(each_assign_tag_dete_obj)
                else:
                    each_assign_tag_dete_obj.tag = tag_code_dict['K_KG_rust']
                    new_alarms.append(each_assign_tag_dete_obj)
            # 开口销安装不规范
            if 'kkxTC' in each_tags or 'illegal' in each_tags or 'clearence' in each_tags:
                # 增加
                each_assign_tag_dete_obj = copy.deepcopy(each_dete_obj)
                each_assign_tag_dete_obj.tag = tag_code_dict['illegal']
                new_alarms.append(each_assign_tag_dete_obj)

        # --------------------------------------------------------------------------------------------------------------

        elif each_tag in tag_code_dict:
            each_dete_obj.tag = tag_code_dict[each_tag]
            new_alarms.append(each_dete_obj)

    assign_dete_res.reset_alarms(new_alarms)

    return assign_dete_res


if __name__ == "__main__":

    # todo 线夹倾斜是明显有问题的，
        # (1) xMin 等，其中的 M 是大写，其他的是小写，这个是有问题的，是否需要我这边进行改正
    # todo 均压环倾斜和线夹倾斜是一个问题，需要进行纠正
        # 均压环倾斜中的 object 的 name 存在中文，并不是一个标签
    # todo 看防振锤模型输出的 xml 是否正常，是不是有正常的 filename 等信息
        # 只需要在 drawbox 的 157 行增加下面信息即可，还未实验，应该是没有问题的
        # a.height = h
        # a.width = w
        # a.filename = name

    save_dir = r"C:\Users\18761\Desktop\del\res_xml\xml"
    save_xml_dir = os.path.join(save_dir, "xml")
    os.makedirs(save_xml_dir, exist_ok=True)

    xml_dir_list = [
        r"C:\Users\18761\Desktop\del\merge\merge_002",
        r"C:\Users\18761\Desktop\del\merge\merge_001",
        # r"C:\Users\18761\Desktop\all_merge_xml",
        # r"C:\Users\18761\Desktop\all_merge_xml\fzc",
                    ]
    tag_code_dict = {

        # --------------------------------------------------------------------------------------------------------------
        # 开口销缺失
        "K": "040500013",

        # 安装不规范
        "illegal": "040500023",

        # 销钉锈蚀
        "K_KG_rust": "040500033",

        # 螺母锈蚀
        "Lm_rust": "040501013",
        # --------------------------------------------------------------------------------------------------------------

        # fixme 验证一下 蜂巢输出的是不是 nc 关键字
        # 鸟巢蜂巢
        "nc": "010000023",

        # 玻璃绝缘子自爆
        "jyzzb": "030100023",

        # 绝缘子污秽
        "abnormal": "030100011",

        # 均压环倾斜
        "fail": "030200131",

        # 金具锈蚀
        "rust": "040000011",

        # 防振锤锈蚀
        "fzc_rust": "040303031",

        # 防振锤破损
        "fzc_broken": "040303021",

        # fixme 导线散股,看看这个标签是否正确
        "sg": "040402011",

        # --------------------------------------------------------------------------------------------------------------
        # 吊塔
        "TowerCrane": "060800013",

        # 推土机
        "Bulldozer": "060800023",

        # 挖掘机
        "Digger": "060800033",
        # --------------------------------------------------------------------------------------------------------------

        # 线夹缺垫片
        "dp_missed": "040001042",

        # 防鸟刺安装不规范
        "fncBGF": "070400031",

        # 防鸟刺未打开
        "weidakai": "070400021",

        # fixme 测试
        "XJnormal": "000xxx000",

                     }

    # 搜集所有的 xml ，将文件名相同的进行合并
    xml_path_dict = {}
    for each_xml_dir in xml_dir_list:
        for each_xml_path in FileOperationUtil.re_all_file(each_xml_dir, lambda x: str(x).endswith('.xml')):
            xml_name = os.path.split(each_xml_path)[1]
            if xml_name in xml_path_dict:
                xml_path_dict[xml_name].append(each_xml_path)
            else:
                xml_path_dict[xml_name] = [each_xml_path]

    # 读取每一个 xml 中的信息，将结果进行合并
    csv_list = [['filename', 'code', 'score', 'xmin', 'ymin', 'xmax', 'ymax']]
    for each_xml_name in xml_path_dict:

        try:

            # 合并相同文件名的 xml
            dete_res = merge_xml_get_dete_res(xml_path_dict[each_xml_name])
            # code 之间的映射
            dete_res = from_out_name_to_code(dete_res)
            # 保存结果
            each_xml_save_path = os.path.join(save_xml_dir, each_xml_name)

            # fixme 我们之前的代码 xml 输出的 filename 都没有文件的后缀
            if dete_res.file_name is not None:
                if not(dete_res.file_name.endswith('.jpg') or dete_res.file_name.endswith('.JPG')):
                    dete_res.file_name += '.jpg'
            #
            dete_res.save_to_xml(each_xml_save_path, is_wh_format=True)

            # 输出对应的 csv，filename,code,score,xmin,ymin,xmax,ymax
            for each_dete_obj in dete_res.alarms:
                each_csv_line = []
                each_csv_line.append(each_xml_name[:-3] + 'jpg')
                each_csv_line.append(each_dete_obj.tag)
                each_csv_line.append('1.0')
                each_csv_line.append(each_dete_obj.x1)
                each_csv_line.append(each_dete_obj.y1)
                each_csv_line.append(each_dete_obj.x2)
                each_csv_line.append(each_dete_obj.y2)
                csv_list.append(each_csv_line)

        except Exception as e:
            print('-'*100)
            print('GOT ERROR---->')
            print(e)
            print(e.__traceback__.tb_frame.f_globals["__file__"])
            print(e.__traceback__.tb_lineno)

    csv_path = os.path.join(save_dir, 'result.csv')
    CsvUtil.save_list_to_csv(csv_list, csv_path)




















