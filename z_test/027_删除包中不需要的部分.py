# -*- coding: utf-8  -*-
# -*- author: jokker -*-


# from ..shapely.geometry.polygon import Polygon
# from shapely.geometry.polygon import Polygon
from JoTools.shapely.geometry.polygon import Polygon


def polygon_iou(poly_points_list_1, poly_points_list_2):
    """计算任意两个凸多边形之间的 IOU"""
    #
    poly1 = Polygon(poly_points_list_1).convex_hull  # 凸多边形
    poly2 = Polygon(poly_points_list_2).convex_hull  # 凸多边形
    poly3 = poly1.intersection(poly2)
    #
    area_1 = poly1.area
    area_2 = poly2.area
    area_3 = poly3.area
    #
    iou = area_3 / (area_1 + area_2 - area_3)
    return iou



if __name__ == "__main__":


    points_1 = [(0,0), (100,0), (100,100), (0,100)]
    points_2 = [(50,50), (150,50), (150,150), (50,150)]


    iou = polygon_iou(points_1, points_2)
    print(iou)
    print(1/7)



