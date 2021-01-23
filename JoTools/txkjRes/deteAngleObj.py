# -*- coding: utf-8  -*-
# -*- author: jokker -*-


class DeteAngleObj(object):
    """检测结果的一个检测对象，就是一个矩形框对应的信息"""

    def __init__(self, cx, cy, w, h, angle, tag, conf=-1, assign_id=-1):
        self.conf = conf
        self.tag = tag
        self.cx = cx
        self.cy = cy
        self.w = w
        self.h = h
        self.angle = angle
        self.id=assign_id

    def do_offset(self, offset_x, offset_y):
        """对结果进行偏移"""
        self.cx += offset_x
        self.cy += offset_y

    def get_center_point(self):
        """得到中心点坐标"""
        return float(self.cx), float(self.cy)

    def get_format_list(self):
        """得到标准化的 list 主要用于打印"""
        return [str(self.tag), float(self.cx), float(self.cy), float(self.w), float(self.h), float(angle), format(float(self.conf), '.4f')]

    def get_area(self):
        """返回面积，面积大小按照像素个数进行统计"""
        return float(self.w) * float(self.h)

    # def format_check(self):
    #     """类型检查和调整"""
    #     self.conf = float(self.conf)
    #     self.tag = str(self.tag)
    #     self.x1 = int(self.x1)
    #     self.y1 = int(self.y1)
    #     self.x2 = int(self.x2)
    #     self.y2 = int(self.y2)
