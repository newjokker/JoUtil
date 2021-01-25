# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import cv2
import math
import numpy as np
from .deteObj import DeteObj

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

    def to_dete_obj(self):
        """dete_angle_obj 转为 dete_obj"""
        cx, cy, w, h, angle = self.cx, self.cy, self.w, self.h, self.angle
        angle=angle*np.pi/180
        p0x,p0y = self.rotate_point(cx, cy, cx - w / 2, cy - h / 2, -angle)
        p1x,p1y = self.rotate_point(cx, cy, cx + w / 2, cy - h / 2, -angle)
        p2x,p2y = self.rotate_point(cx, cy, cx + w / 2, cy + h / 2, -angle)
        p3x,p3y = self.rotate_point(cx, cy, cx - w / 2, cy + h / 2, -angle)
        # 转为 dete_obj
        x1 = math.ceil(min(p0x, p1x, p2x, p3x))
        y1 = math.ceil(min(p0y, p1y, p2y, p3y))
        x2 = math.ceil(max(p0x, p1x, p2x, p3x))
        y2 = math.ceil(max(p0y, p1y, p2y, p3y))
        a = DeteObj(x1=x1, y1=y1, x2=x2, y2=y2, tag=self.tag, conf=self.conf, assign_id=self.id)
        return a

    @staticmethod
    def rotate_point(xc, yc, xp, yp, theta):
        xoff = xp-xc
        yoff = yp-yc
        cosTheta = np.cos(theta)
        sinTheta = np.sin(theta)
        pResx = cosTheta * xoff + sinTheta * yoff
        pResy = - sinTheta * xoff + cosTheta * yoff
        return xc+pResx, yc+pResy






