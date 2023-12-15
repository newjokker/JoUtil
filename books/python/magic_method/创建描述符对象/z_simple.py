# -*- coding: utf-8  -*-
# -*- author: jokker -*-

# refer : https://blog.csdn.net/Leafage_M/article/details/54960432


class Meter(object):
    '''米的描述符。'''

    def __init__(self, value=0.0):
        self.value = float(value)

    def __get__(self, instance, owner):
        print("* 获取 meter 的值")
        return self.value

    def __set__(self, instance, value):
        print(" * meter 设置值")
        self.value = float(value)

class Foot(object):
    '''英尺的描述符。'''

    def __get(self, instance, owner):
            return instance.meter * 3.2808

    def __set(self, instance, value):
            instance.meter = float(value) / 3.2808

class Distance(object):
    '''用于描述距离的类，包含英尺和米两个描述符。'''
    meter = Meter()
    foot = Foot()



if __name__ == "__main__":



    a = Distance()

    b = Distance()

    a.meter = 12
    a.foot = 13

    b.meter = 22

    print(a.foot)

    print(a.meter)



