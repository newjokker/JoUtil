# -*- coding: utf-8  -*-
# -*- author: jokker -*-

"""

辅助标图：我觉得我们可以尝试一下使用半自动化标图，在 labelimg 中画一个框，框对应的图片被截图，在服务器上跑出结果返回 labelimg 作为候选项等待被选中，类似于打字的联想功能

修改 labelImg 代码，

* 如何选择候选框，（1）在之前选择标签的位置显示候选项（2）在鼠标旁边选择候选项（3）当图片在界面放大缩小时需要不报 bug

*



"""