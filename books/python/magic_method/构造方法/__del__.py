# -*- coding: utf-8  -*-
# -*- author: jokker -*-

# __new__ 和 __init__ 是对象的构造器， __del__ 是对象的销毁器。它并非实现了语句 del x (因此该语句不等同于 x.__del__())。而是定义了当对象被垃圾回收时的行为。
# 当对象需要在销毁时做一些处理的时候这个方法很有用，比如 socket 对象、文件对象。但是需要注意的是，当Python解释器退出但对象仍然存活的时候，
# __del__ 并不会 执行。 所以养成一个手工清理的好习惯是很重要的，比如及时关闭连接。


from os.path import join


class FileObject:
    '''文件对象的装饰类，用来保证文件被删除时能够正确关闭。'''

    def __init__(self, filepath='~', filename='sample.txt'):
        # 使用读写模式打开filepath中的filename文件
        self.file = open(join(filepath, filename), 'r+')

    def __del__(self):
        self.file.close()
        del self.file




