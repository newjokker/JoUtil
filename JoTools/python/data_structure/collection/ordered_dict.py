# -*- coding: utf-8  -*-
# -*- author: jokker -*-

"""
* 可以用于指定 xml 中各个项目的顺序
*
"""



from collections import OrderedDict

d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['samp'] = 3
d['grok'] = 4


for k,v in d.items():
    print(k, v)










