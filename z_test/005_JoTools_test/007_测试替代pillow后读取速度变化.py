# -*- coding: utf-8  -*-
# -*- author: jokker -*-

from JoTools.txkjRes.deteRes import DeteRes
from JoTools.utils.DecoratorUtil import DecoratorUtil
import time

@DecoratorUtil.time_this
def main():
    xml_path = r"C:\Users\14271\Desktop\del\pillow_cv2\test_2.xml"
    img_path = r"C:\Users\14271\Desktop\del\pillow_cv2\test_2.jpg"

    a = DeteRes(xml_path)
    a.img_path = img_path

    # img_a = a.get_img_array(RGB=False)
    # img_b = a.get_img_array_new(RGB=False)

    start = time.time()
    # for each_dete_obj in a:
    #     print('-'*50)
    #     each_img_a = a.get_sub_img_by_dete_obj(each_dete_obj)
    #     each_img_b = a.get_sub_img_by_dete_obj_new(each_dete_obj)
    #     # print(each_img_a.shape)
    #     # print(each_img_b.shape)
    #     pass

    a.crop_dete_obj(r"C:\Users\14271\Desktop\del\pillow_cv2\crop")
    a.crop_dete_obj_new(r"C:\Users\14271\Desktop\del\pillow_cv2\crop")

    stop = time.time()

    print(stop - start)

if __name__ == "__main__":

    main()

