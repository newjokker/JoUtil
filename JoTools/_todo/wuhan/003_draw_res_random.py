
import os
import random
from JoTools.operateDeteRes import OperateDeteRes
from JoTools.txkjRes.deteRes import DeteRes
from JoTools.utils.FileOperationUtil import FileOperationUtil
from JoTools.utils.RandomUtil import RandomUtil

# img_dir = r"D:\集中培育-11月样本\金具\耐张线夹"
# save_dir = r"D:\画图看结果\005_耐张线夹却垫片"

img_dir = r"D:\集中培育-11月样本\金具\小金具"
save_dir = r"D:\画图看结果\016_螺母松动"

img_path_list = FileOperationUtil.re_all_file(img_dir, lambda x:str(x).endswith(('.jpg', '.JPG')))
RandomUtil.shuffle(img_path_list)

index = 0
for each_img_path in img_path_list:
    each_img_dir, each_img_name = os.path.split(each_img_path)
    each_xml_path = os.path.join(each_img_dir, 'xml', each_img_name[:-3] + 'xml')

    a = DeteRes(each_xml_path)

    # todo 当存在指定才标签进行绘图操作，
    # ['040001041', '040001042']
    # print(a.count_tags())

    # a.filter_by_tages(need_tag=['040001041', '040001042'])
    # a.filter_by_tages(need_tag=['040101031', '040101032', '040101033'])
    # a.filter_by_tages(need_tag=['030000121', '030100121', '030200131', '030300091', '030300142'])
    # a.filter_by_tages(need_tag=['040000071'])
    # a.filter_by_tages(need_tag=['040303021', '040303022'])
    # a.filter_by_tages(need_tag=['030000011', '030000041', '030100011', '030100041'])


    # need_tag = ['030100021', '030100022', '030100023']
    need_tag = ['040501031', '040501032', '040501033']


    a.filter_by_tages(need_tag= need_tag)
    color_dict = {i: [0, 0, 255] for i in need_tag}

    if len(a.alarms) > 0:
        print(index)
        index += 1
        a.img_path = each_img_path
        save_path = os.path.join(save_dir, each_img_name)
        a.draw_dete_res(save_path, color_dict=color_dict)

    if index > 100:
        exit()



