# -*- coding: utf-8  -*-
# -*- author: jokker -*-


# refer : https://zhuanlan.zhihu.com/p/139771390

# 通过内置装饰器 @calssmethod 可以实现直接用类调用函数方法，不必通过实例来调用, 类方法只是给类使用(无论是否存在实例)，只能访问实例属性(变量)，不能访问实例的方法

# 注意 : 只能访问实例属性(变量)


class fruit:
    fruit_name = 'apple'
    def __init__(self,color, shape):
        self.color = color
        self.shape = shape

    def fruit_color(self):
        self.color = "red"
        print(self.color)

    # 函数fruit_info变为类方法，该函数只能访问到类的数据属性，不能获取实例的数据属性
    @classmethod
    def fruit_info(cls):  #python自动传入位置参数cls就是类本身
        print('This is an %s'%cls.fruit_name)   #cls.fruit_name调用类自己的数据属性


if __name__ == "__main__":

    fruit.fruit_info()

    # fruit.fruit_color()






