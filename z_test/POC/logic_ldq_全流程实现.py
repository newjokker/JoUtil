# -*- coding: utf-8  -*-
# -*- author: jokker -*-
import os.path
import random
from JoTools.txkjRes.deteRes import DeteRes
from JoTools.txkjRes.deteObj import DeteObj
from JoTools.utils.FileOperationUtil import FileOperationUtil


img_dir             = r"E:\ucd_cache\img_cache"
xml_dir             = r"C:\Users\14271\Desktop\POC\dete_res"
save_dir            = r"C:\Users\14271\Desktop\POC\dete_dx"
save_draw_crop      = r"C:\Users\14271\Desktop\POC\dete_dx_draw"
save_draw_region    = r"C:\Users\14271\Desktop\POC\dete_dx_draw\draw_img"

os.makedirs(save_dir, exist_ok=True)
os.makedirs(save_draw_crop, exist_ok=True)
os.makedirs(save_draw_region, exist_ok=True)

def sort_by_obj_x(dete_res):
    # 根据对象的 x 轴大小进行排序
    obj_map = {}  # key: 中心点的 x value: obj 对象
    for obj in dete_res:
        x, y = obj.get_center_point()
        if x in obj_map:
            x = x + random.random() * 0.001
        obj_map[x] = obj

    sorted_keys = sorted(obj_map)
    sorted_values = [obj_map[key].tag for key in sorted_keys]  # 获取对应排序的值
    return sorted_values

def sort_by_obj_x_dx(dete_res):
    # 根据对象的 x 轴大小进行排序

    obj_map = {}  # key: 中心点的 x value: obj 对象
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

def sort_by_obj_x_sx(dete_res):
    # 根据对象的 x 轴大小进行排序

    obj_map = {}  # key: 中心点的 x value: obj 对象
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

    if len(ys_sorted) < 6:
        return []
    elif len(ys_sorted) == 6:
        return [list(colors)]
    else:
        for each_ys in ys_sorted[5:]:
            each_color_list = []
            for index in range(len(colors)):
                if ys[index] <= each_ys:
                    each_color_list.append(colors[index])
            color_list.append(each_color_list)
    return color_list

def similar_x_index(obj1, obj2, ignore_tag=False):
    # 两个对象在 x 轴上的相似度，可以选择是否忽略 tag 的一致性
    if (not ignore_tag) and (obj1.tag != obj2.tag):
        return 0
    else:
        range1_start, range1_end = obj1.x1, obj1.x2
        range2_start, range2_end = obj2.x1, obj2.x2
        if range1_end < range2_start or range2_end < range1_start:
            return 0
        overlap_start = max(range1_start, range2_start)
        overlap_end = min(range1_end, range2_end)
        # 计算重叠长度
        total_length = max(range1_end, range2_end) - min(range1_start, range2_start)
        overlap_length = overlap_end - overlap_start
        return overlap_length / total_length

def drop_obj_by_y_and_tag(dete_res, similar_index=0.6, ignore_tag=False):
    # 去除上下 x 轴，方向上有重叠，同时属于同一个标签的中 y1 比较小的 obj
    dete_res_new = DeteRes()
    drop_dete_res = DeteRes()
    for each_obj1 in dete_res:
        for each_obj2 in dete_res:
            if each_obj1 != each_obj2:
                if similar_x_index(each_obj1, each_obj2, ignore_tag=ignore_tag) > similar_index:
                    if each_obj1.y1 <= each_obj2.y1:
                        drop_dete_res.add_obj_2(each_obj2)
                    else:
                        drop_dete_res.add_obj_2(each_obj1)

    for each_obj in dete_res:
        if each_obj not in drop_dete_res.alarms:
            dete_res_new.add_obj_2(each_obj)
    return dete_res_new

def get_cable_type(dete_res_cable, has_box=False, drop_sililar_obj=False):
    # 返回 cable 的各种类别

    dete_res_cable = dete_res_cable.deep_copy(copy_img=False)

    if has_box:
        return "cor_dx_box"

    # dete_res_cable.print_as_fzc_format()
    # print("-" * 50)

    # 去掉非常小的目标
    dete_res_cable.filter_by_area(200)
    if drop_sililar_obj:
        dete_res_cable = drop_obj_by_y_and_tag(dete_res_cable, similar_index=0.6, ignore_tag=False)

    # count_tags = dete_res_cable.count_tags()

    if len(dete_res_cable) < 3:
        # 小于三个 默认是正确的
        return "cor_dx_lt_3_line"

    elif len(dete_res_cable) == 3:
        # 单独处理三个线的情况， rrb, rbb, bbr, brr 只存在四种情况
        colorList = sort_by_obj_x(dete_res_cable)
        if ((colorList[0] == colorList[1]) or ((colorList[1] == colorList[2]))) and (colorList[0] != colorList[2]):
            return "cor_dx_3_line"
        else:
            return "err_dx_3_line"

    # FIXME 这边适当放宽到 7 个，但是对于七个的需要特殊处理
    elif 4 <= len(dete_res_cable) <= 6:
        # if "blue" in count_tags and "red" in count_tags:
        # if (count_tags["blue"] + count_tags["red"]) >= (0.665 * len(dete_res_cable)):
        # 是否需要改为 存在 bbrr, rrbb 就是正常的，为了防止边缘多检出其他的线

        colorList = sort_by_obj_x_dx(dete_res_cable)

        for eachColorList in colorList:
            # 当已经是正确的时候不在继续下去了
            if len(eachColorList) >= 4:
                for i in range(0, len(eachColorList) - 3):
                    # if eachColorList[i:i + 4] == ["red", "red", "blue", "blue"] or eachColorList[i:i + 4] == ["blue", "blue", "red", "red"]:
                    if (eachColorList[i] == eachColorList[i + 1]) and (
                    (eachColorList[i + 2] == eachColorList[i + 3])) and (eachColorList[i] != eachColorList[i + 2]):
                        # 查看放出去的那些是不是就是对的（目前来看是很好地解决了模型检测不准，出现多检的情况的，rrbb 中间出现多余的框的话还是有 rrbb这个模式）
                        if len(eachColorList) != 4:
                            return "cor_dx_rrbb_gt_4"
                        else:
                            return "cor_dx_rrbb_eq_4"

        # FIXME 去掉那些框（1）比较接近正方形，而且（2）在比较下面的地方的情况（多检）（3）去掉这个框之后就正常了（默认只会有一个多检）
        # FIXME 在有多余框的情况下（1）红色或者蓝色（2）左上角 y 值小于其他目标的中心点均值（3）去掉就好了 ，那这个框基本就是下界的横管多检

        # 有且仅有两个色块，对应的是 三个红的一个蓝的，三个蓝的一个红的，等情况
        for eachColorList in colorList:
            color_plaque_num = 0
            for i in range(1, len(eachColorList)):
                if eachColorList[i - 1] != eachColorList[i]:
                    color_plaque_num += 1
            # 出现一次变化是两个斑块，属于对的
            if color_plaque_num == 1:
                return "cor_dx_plaque"

        return "err_dx_miss_all"

    # 三相电表的情况
    # 只判断完美的正确的情况，就是序列中出现了 yyggrr 的情况
    if len(dete_res_cable) <= 10:
        colorList = sort_by_obj_x_sx(dete_res_cable)
        for eachColorList in colorList:

            # 当已经是正确的时候不在继续下去了
            for i in range(0, len(eachColorList) - 5):
                if eachColorList[i:i + 6] == ["yellow", "yellow", "green", "green", "red", "red"]:
                    # 查看放出去的那些是不是就是对的（目前来看是很好地解决了模型检测不准，出现多检的情况的，rrbb 中间出现多余的框的话还是有 rrbb这个模式）
                    if len(eachColorList) != 6:
                        return "cor_sx_yyggrr_gt_6"
                    else:
                        return "cor_sx_yyggrr_eq_6"

            # 三相实现斑块模式，出现 ygr 斑块，同时板块中个数最小不能小于 2

            # 斑块合并模式，连续出现 黄 绿 红 中间没有其他颜色，而且每个颜色个数 >= 2
            colorNumDict = {"yellow": 0, "green": 0, "red": 0}
            find_y = False
            for colorIndex in range(0, len(eachColorList) - 1):
                eachColor = eachColorList[colorIndex]

                if eachColor == "yellow":
                    find_y = True

                if not find_y:
                    continue

                nextColor = eachColorList[colorIndex + 1]
                if nextColor not in ["yellow", "green", "red"]:
                    break

                if eachColor == nextColor:
                    colorNumDict[eachColor] += 1
                else:
                    # 从黄色开始，有一个值对不上就不处理了
                    if eachColor == "yellow" and nextColor != "green":
                        break
                    if eachColor == "green" and nextColor != "red":
                        break
                    if eachColor == "red" and nextColor != "red":
                        break
                    colorNumDict[eachColor] += 1

            if colorNumDict["yellow"] >= 2 and colorNumDict["green"] >= 2 and colorNumDict["red"] >= 2:
                return "cor_sx_plaque"
    else:
        return "cor_sx_gt_10"

    return "unkoow_error"


if __name__ == "__main__":

    # TODO: 截取 cable 范围，对每一个 cable 范围进行处理

    for each_xml_path in FileOperationUtil.re_all_file(xml_dir, endswitch=[".xml"]):
        each_img_path = os.path.join(img_dir, os.path.split(each_xml_path)[1][:-4] + ".jpg")
        if not os.path.exists(each_img_path):
            print("* 不存在原图，跳过")

        if "Egf02di" in each_xml_path:
            print("check")

        a = DeteRes(each_xml_path)
        a.do_nms(0.1, ignore_tag=False)
        deteResCable = a.filter_by_tags(need_tag=["cable"], update=False)

        hasBox = a.has_tag("box")
        a.filter_by_tags(need_tag=["red", "blue", "yellow", "black", "green"], update=True)
        for each_cabel_obj in deteResCable:
            eachDeteRes = a.filter_by_mask(each_cabel_obj.get_points(), cover_index_th=0.1, need_in=True, update=False)
            each_cable_type = get_cable_type(eachDeteRes, hasBox, drop_sililar_obj=False)
            each_cabel_obj.tag = "cable_" + each_cable_type

        deteResCable += a
        deteResCable.save_to_xml(os.path.join(save_dir, os.path.split(each_xml_path)[1]))

        # if len(deteResCable) > 0:
        #     deteResCable.img_path = each_img_path
        #     save_draw_path = os.path.join(save_draw_region, os.path.split(each_xml_path)[1][:-4] + ".jpg")
        #     draw_img = deteResCable.draw_dete_res(save_draw_path, color_dict={"black":[0,0,0], "blue":[255,0,0], "green":[0,255,0], "red":[0,0,255], "yellow":[0,255,255],
        #                                                                       "cable_cor_dx_3_line":[0,255,0],
        #                                                                       "cable_cor_dx_box":[0,255,0],
        #                                                                       "cable_cor_dx_lt_3_line":[0,255,0],
        #                                                                       "cable_cor_dx_plaque":[0,255,0],
        #                                                                       "cable_cor_dx_rrbb_eq_4":[0,255,0],
        #                                                                       "cable_cor_dx_rrbb_gt_4":[0,255,0],
        #                                                                       "cable_cor_sx_yyggrr_eq_6":[0,255,0],
        #                                                                       "cable_cor_sx_yyggrr_gt_6":[0,255,0],
        #                                                                       "cable_err_dx_3_line":[0,0,255],
        #                                                                       "cable_err_dx_miss_all":[0,0,255],
        #                                                                       "cable_unkoow_error":[0,0,255],
        #                                                                       })
        #     deteResCable.img_ndarry = draw_img
        #     deteResCable.filter_by_tags(remove_tag=["red", "blue", "yellow", "black", "green"])
        #     # deteResCable.filter_by_tags(need_tag=["cable_unkoow", "cable_err_dx_miss_all", "cable_err_dx_3_line", "cable_cor_sx_yyggrr_gt_6", "cable_cor_sx_yyggrr_eq_6"])
        #     deteResCable.crop_dete_obj(save_draw_crop, split_by_tag=True)
        #








