# -*- coding: utf-8  -*-
# -*- author: jokker -*-
import os.path
import random
from JoTools.txkjRes.deteRes import DeteRes
from JoTools.txkjRes.deteObj import DeteObj
from JoTools.utils.FileOperationUtil import FileOperationUtil


img_dir             = r"E:\ucd_cache\img_cache"
xml_dir             = r"C:\Users\14271\Desktop\POC\dete_res"
dx_error            = r"C:\Users\14271\Desktop\POC\dete_dx\error"
correct_rrbb_eq_4   = r"C:\Users\14271\Desktop\POC\dete_dx\corr_rrbb_eq_4"
correct_rrbb_gt_4   = r"C:\Users\14271\Desktop\POC\dete_dx\corr_rrbb_gt_4"
correct_box         = r"C:\Users\14271\Desktop\POC\dete_dx\corr_box"
correct_plaque      = r"C:\Users\14271\Desktop\POC\dete_dx\corr_plaque"
correct_3_line      = r"C:\Users\14271\Desktop\POC\dete_dx\corr_3_line"
error_3_line        = r"C:\Users\14271\Desktop\POC\dete_dx\error_3_line"
corr_lt_3_line       = r"C:\Users\14271\Desktop\POC\dete_dx\corr_lt_3_line"


os.makedirs(correct_plaque, exist_ok=True)
os.makedirs(correct_rrbb_gt_4, exist_ok=True)
os.makedirs(correct_rrbb_eq_4, exist_ok=True)
os.makedirs(dx_error, exist_ok=True)
os.makedirs(correct_3_line, exist_ok=True)
os.makedirs(error_3_line, exist_ok=True)
os.makedirs(corr_lt_3_line, exist_ok=True)


def sort_by_obj_x(dete_res):
    # 根据对象的 x 轴大小进行排序
    obj_map = {}    # key: 中心点的 x value: obj 对象
    for obj in dete_res:
        if(isinstance(obj, DeteObj)):
            x, y = obj.get_center_point()
            if x in obj_map:
                x = x + random.random() * 0.001
            obj_map[x] = obj

    sorted_keys = sorted(obj_map)
    sorted_values = [obj_map[key].tag for key in sorted_keys]  # 获取对应排序的值
    return sorted_values

def sort_by_obj_x_dx(dete_res):
    # 根据对象的 x 轴大小进行排序

    obj_map = {}    # key: 中心点的 x value: obj 对象
    for obj in dete_res:
        x, y = obj.get_center_point()
        if x in obj_map:
            x = x + random.random() * 0.001
        obj_map[x] = obj

    sorted_keys = sorted(obj_map)
    sorted_values = [(obj_map[key].tag, obj_map[key].y1) for key in sorted_keys]  # 获取对应排序的值
    colors, ys = zip(*sorted_values)
    ys_sorted = sorted(ys)

    color_list = []

    if len(ys_sorted) < 4:
        return []
    elif len(ys_sorted) == 4:
        return [list(colors)]
    else:
        for each_ys in ys_sorted[3:]:
            each_color_list = []
            for index in range(len(colors)):
                if ys[index] <= each_ys:
                    each_color_list.append(colors[index])
            color_list.append(each_color_list)
    return color_list


def get_cable_type(dete_res):
    # 返回 cable 的各种类别
    pass




# a = DeteRes(r"C:\Users\14271\Desktop\POC\error_dx\Etp03fd.xml")
# a.filter_by_tags(need_tag=["red", "blue", "yellow", "black", "green"])
#
# # a.print_as_fzc_format()
#
# sort_by_obj_x(a)



if __name__ == "__main__":

    # TODO: 截取 cable 范围，对每一个 cable 范围进行处理

    for each_xml_path in FileOperationUtil.re_all_file(xml_dir, endswitch=[".xml"]):

        a = DeteRes(each_xml_path)
        dete_res_cable = a.filter_by_tags(need_tag=["cable"], update=False)

        if len(dete_res_cable) != 1:
            # FIXME 先不处理多个 cable 表的情况
            continue

        a.filter_by_tags(need_tag=["red", "blue", "yellow", "black", "green"])
        # 去掉 200 个像素以内的目标
        a.filter_by_area(200)
        a.do_nms(0.1, ignore_tag=True)
        save_path_correct_plaque    = os.path.join(correct_plaque, os.path.split(each_xml_path)[1])
        save_path_correct_rrbb_gt_4 = os.path.join(correct_rrbb_gt_4, os.path.split(each_xml_path)[1])
        save_path_correct_rrbb_eq_4 = os.path.join(correct_rrbb_eq_4, os.path.split(each_xml_path)[1])
        save_path_correct_box       = os.path.join(correct_box, os.path.split(each_xml_path)[1])
        save_error_path             = os.path.join(dx_error, os.path.split(each_xml_path)[1])
        save_path_correct_3_line    = os.path.join(correct_3_line, os.path.split(each_xml_path)[1])
        save_path_error_3_line      = os.path.join(error_3_line, os.path.split(each_xml_path)[1])
        save_path_corr_lt_3_line    = os.path.join(corr_lt_3_line, os.path.split(each_xml_path)[1])
        count_tags = a.count_tags()

        if a.has_tag("box"):
            a += dete_res_cable
            a.save_to_xml(save_path_correct_box)
            print("* 存在 box 标签，默认认为正确")

        if len(a) < 3:
            # 小于三个 默认是正确的
            a += dete_res_cable
            a.save_to_xml(save_path_corr_lt_3_line)
            print("* 识别到小于三个标签，默认认为正确")

        elif len(a) ==3:

            if "Etj0f0m" in each_xml_path:
                print("watch")

            # 单独处理三个线的情况， rrb, rbb, bbr, brr 只存在四种情况
            correct_mode = [["red", "red", "blue"], ["red", "blue", "blue"], ["blue", "red", "red"], ["blue", "blue", "red"]]
            colorList = sort_by_obj_x(a)
            if colorList in correct_mode:
                a += dete_res_cable
                a.save_to_xml(save_path_correct_3_line)
                print("* 检测到三个标签，符合 三标签通过的 4 中情况之一")
            else:
                a += dete_res_cable
                a.save_to_xml(save_path_error_3_line)
                print("* 检测到三个标签，不符合通过条件，判断为错误")

        elif 4<= len(a) <= 6:
            if "blue" in count_tags and "red" in count_tags:
                if (count_tags["blue"] + count_tags["red"]) >= (0.665 * len(a)):

                    if "Etj0a30" in each_xml_path:
                        print("watch")

                    # 是否需要改为 存在 bbrr, rrbb 就是正常的，为了防止边缘多检出其他的线
                    colorList = sort_by_obj_x_dx(a)
                    correct_dx = False

                    for eachColorList in colorList:
                        # 当已经是正确的时候不在继续下去了
                        if correct_dx:
                            break

                        if len(eachColorList) >= 4:
                            for i in range(0, len(eachColorList) - 3):
                                if eachColorList[i:i + 4] == ["red", "red", "blue", "blue"] or eachColorList[i:i + 4] == ["blue", "blue", "red", "red"]:
                                    correct_dx = True

                                    # 查看放出去的那些是不是就是对的（目前来看是很好地解决了模型检测不准，出现多检的情况的，rrbb 中间出现多余的框的话还是有 rrbb这个模式）
                                    if len(eachColorList) != 4:
                                        a += dete_res_cable
                                        a.save_to_xml(save_path_correct_rrbb_gt_4)
                                    else:
                                        a += dete_res_cable
                                        a.save_to_xml(save_path_correct_rrbb_eq_4)

                                    print("* 符合 rrbb 模式，判断为单相线序正确")
                                    break

                    # FIXME 去掉那些框（1）比较接近正方形，而且（2）在比较下面的地方的情况（多检）（3）去掉这个框之后就正常了（默认只会有一个多检）
                    # FIXME 在有多余框的情况下（1）红色或者蓝色（2）左上角 y 值小于其他目标的中心点均值（3）去掉就好了 ，那这个框基本就是下界的横管多检

                    # 有且仅有两个色块，对应的是 三个红的一个蓝的，三个蓝的一个红的，等情况
                    if not correct_dx:
                        for eachColorList in colorList:
                            color_plaque_num = 0
                            for i in range(1, len(eachColorList)):
                                if eachColorList[i - 1] != eachColorList[i]:
                                    color_plaque_num += 1

                            if color_plaque_num == 1:
                                correct_dx = True
                                a += dete_res_cable
                                a.save_to_xml(save_path_correct_plaque)
                                print("* 符合双色块模式，判断为单向线顺序正确")

                    if not correct_dx:
                        a += dete_res_cable
                        a.save_to_xml(save_error_path)

                else:
                    print("* 非单相线，忽略")
            else:
                print("* 返回三相线")










