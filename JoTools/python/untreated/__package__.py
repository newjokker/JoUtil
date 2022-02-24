# -*- coding: utf-8  -*-
# -*- author: jokker -*-


# __package__主要是为了相对引用而设置的一个属性, 如果所在的文件是一个package的话, 它和__name__的值是一样的, 如果是子模块的话, 它的值就跟父模块一致

# 在包里面的文件中打印 __package__ 的话出来的就是模块的路径


from JoTools.txkjRes.deteRes import DeteRes, DeteObj


print(__package__)

