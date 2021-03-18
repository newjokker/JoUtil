# -*- coding: utf-8  -*-
# -*- author: jokker -*-

M = None    # 为该算法对应的测试图像中标准框总数
M1 = None   # 为识别算法输出正确框总数
M2 = None   # 为识别算法输出框总数

discovery_rate =  M1/M          # 发现率
false_alarm_rate = (M2-M1)/M2   # 误报率
output_quality = None           # 输出质量
recognition_efficiency = None   # 识别效率


def get_discovery_rate(M, M1):
    """计算发现率"""
    return M1/M

def get_false_alarm_rate(M1, M2):
    """计算误报率"""
    return (M2-M1)/M2

def get_output_quality(M, M1, M2):
    """获取输出质量分"""
    c = (M2 - M1) / M       # 错误率

    if c <= 1:
        return 20
    elif c <= 2:
        return 16
    elif c <= 3:
        return 12
    elif c <= 4:
        return 8
    elif c <= 5:
        return 4
    else:
        return 0

def get_recognition_efficiency(img_count, use_time):
    """计算识别效率得分"""
    avg_time = use_time / img_count

    if avg_time <= 2:
        return 5
    elif avg_time <= 3:
        return 4
    elif avg_time <= 4:
        return 3
    elif avg_time <= 5:
        return 2
    elif avg_time <= 6:
        return 1
    else:
        return 0

def get_score(M, M1, M2, img_count, use_time):
    """计算最后的得分"""
    dr = get_discovery_rate(M, M1)
    far = get_false_alarm_rate(M1, M2)
    oq = get_output_quality(M, M1, M2)
    re = get_recognition_efficiency(img_count, use_time)
    score = dr*65 + (1-far)*10 + oq + re
    return score
