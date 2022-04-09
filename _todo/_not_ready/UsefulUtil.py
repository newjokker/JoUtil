# -*- coding: utf-8  -*-
# -*- author: jokker -*-

"""那些还未整理，但是很有用的部分"""


class UsefulUtil(object):

    @staticmethod
    def enumerate_assign_num(ele_list, assign_num=2):
        """每次去除指定个数的元素，写一个生成器"""
        while len(ele_list)>0:
            if len(ele_list) <= assign_num:
                yield ele_list
                ele_list = []
            else:
                res = ele_list[:assign_num]
                ele_list = ele_list[assign_num:]
                yield res

    @staticmethod
    def enumerate_index(ele_num, assign_num=2):
        """返回每次遍历使用的切片的左右边界"""
        for i in range(0, ele_num, assign_num):
            j = i + assign_num if (i + assign_num) <= ele_num else ele_num
            yield [i, j]


if __name__ == "__main__":

    # for each in UsefulUtil.enumerate_assign_num(list(range(200)), 13):
    #     print(each)
    #
    for each in UsefulUtil.enumerate_index(200, 37):
        print(each)