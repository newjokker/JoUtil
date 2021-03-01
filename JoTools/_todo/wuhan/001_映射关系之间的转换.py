#

# todo 读取客户生成的 xml
# todo 获取 code ，找到字典中对应的我们的 code
# todo 输出为我们 xml 所用的 code

import os
from JoTools.txkjRes.deteRes import DeteRes
from JoTools.utils.FileOperationUtil import FileOperationUtil
from JoTools.operateDeteRes import OperateDeteRes
from JoTools.utils.CsvUtil import CsvUtil

tag_code = {'绝缘子自爆': ['030100021', '030100022', '030100023'],
            '均压环倾斜': ['030000121', '030100121', '030200131', '030300142'],
            '鸟巢蜂窝': ['010000021', '010000022', '010000023', '010100061', '010100062', '010100063', '010200111',
                     '010200112', '010200113', '010300091', '010300092', '010300093', '010400061', '010400062',
                     '010400063'],
            '金具锈蚀': ['040000031', '040000032', '040000033', '040000041', '040000042', '040100011', '040100012',
                     '040200011', '040200012', '040201011', '040201012', '040202011', '040202012', '040203011',
                     '040203012', '040204011', '040204012', '040205011', '040205012', '040206011', '040206012',
                     '040207011', '040207012', '040208011', '040208012', '040209011', '040209012', '040210011',
                     '040210012', '040302011', '040302012'],
            '开口销退出': ['040500021', '040500022', '040500023'],
            '线夹倾斜': ['040000071'],
            '防外破': ['060800011', '060800012', '060800013', '060800021', '060800022', '060800023', '060800031',
                    '060800032', '060800033'],
            '螺栓螺母锈蚀': ['040501011', '040501012', '040501013'],
            '导线松股': ['020000031', '020000041', '020000051', '020000052', '020000103', '040301021', '040301051'],
            '开口销缺失': ['040001051', '040001053', '040104031', '040104033', '040200061', '040200063', '040201061',
                      '040201063', '040202051', '040202053', '040203051', '040203053', '040204051', '040204053',
                      '040500011', '040500012', '040500013'],
            '防外破导线异物': ['020000111', '020000112', '020000113', '020001061', '020001062', '020001063', '020100051',
                        '020100052', '020100053'],
            '螺母松动': ['040501031', '040501032', '040501033'],
            '绝缘子污秽': ['030000011', '030000041', '030100011', '030100041'],
            '悬垂线夹缺垫片': ['040001041', '040001042'],
            '防振锤锈蚀': ['040303031', ],
            '防振锤破损': ['040303021', '040303022']}

# 字典之间的转换
code_dict = {}
for each_tag in tag_code:
    for each_code in tag_code[each_tag]:
        code_dict[each_code] = each_tag

# ----------------------------------------------------------------------------------------------------------------------

def wuhan_to_ours(customer_xml, save_xml):
    a = DeteRes(xml_path=customer_xml)
    for each_dete_obj in a.alarms:
        obj_name = each_dete_obj.tag
        obj_name = obj_name
        if obj_name in code_dict:
            obj_name = code_dict[obj_name]
        each_dete_obj.tag = obj_name
    # 保存为我们的格式
    a.save_to_xml(save_xml)



if __name__ == "__main__":


    # csv_list = CsvUtil.read_csv_to_list(r"C:\Users\jokker\Desktop\quexianzidian.csv")
    #
    # for each_line in csv_list:
    #     code, tag = each_line
    #     if tag in code_dict:
    #         code_dict[tag].append(code)
    #     else:
    #         code_dict[tag] = [code]


    xml_dir = r"C:\Users\jokker\Desktop\del\fzc\xml"
    save_xml_dir = r"C:\Users\jokker\Desktop\del\fzc\xml_new"


    # for each in OperateDeteRes.get_class_count(xml_dir).items():
    #     print(each)
    #
    # for each in OperateDeteRes.get_class_count(save_xml_dir).items():
    #     print(each)

    # exit()

    for each_xml in FileOperationUtil.re_all_file(xml_dir, lambda x:str(x).endswith('.xml')):
        each_xml_name = os.path.split(each_xml)[1]
        save_xml_path = os.path.join(save_xml_dir, each_xml_name)
        wuhan_to_ours(each_xml, save_xml_path)
