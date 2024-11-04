# -*- coding: utf-8  -*-
# -*- author: jokker -*-

# refer : https://blog.csdn.net/Leafage_M/article/details/54960432

"""

是时候坦白真正详细的属性查找策略 了，对于obj.attr（注意：obj可以是一个类）：

1.如果attr是一个Python自动产生的属性，找到！(优先级非常高！)

2.查找obj.__class__.__dict__，如果attr存在并且是data descriptor，返回data descriptor的__get__方法的结果，如果没有继续在obj.__class__的父类以及祖先类中寻找data descriptor

3.在obj.__dict__中查找，这一步分两种情况，第一种情况是obj是一个普通实例，找到就直接返回，找不到进行下一步。第二种情况是obj是一个类，依次在obj和它的父类、祖先类的__dict__中查找，如果找到一个descriptor就返回descriptor的__get__方法的结果，否则直接返回attr。如果没有找到，进行下一步。

4.在obj.__class__.__dict__中查找，如果找到了一个descriptor(插一句：这里的descriptor一定是non-data descriptor，如果它是data descriptor，第二步就找到它了)descriptor的__get__方法的结果。如果找到一个普通属性，直接返回属性值。如果没找到，进行下一步。

5.很不幸，Python终于受不了。在这一步，它raise AttributeError

"""



class Descriptor(object):
    def __get__(self, obj, type=None):
        return 'get', self, obj, type
    def __set__(self, obj, val):
        print('set', self, obj, val)
    def __delete__(self, obj):
        print('delete', self, obj)

class T(object):


    d = Descriptor()

    def __init__(self):

        self.a = Descriptor()


t = T()

print(t.d)

t.d = 12

print(t.a)

t.a = 123
