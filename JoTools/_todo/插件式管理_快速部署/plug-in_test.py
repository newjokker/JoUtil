# -*- coding: utf-8  -*-
# -*- author: jokker -*-



class ModelPlug():
    """插件基类"""

    def __init__(self):
        pass




class FZC(ModelPlug):

    def __init__(self):
        super(FZC, self).__init__()

    def warm_up(self):
        """模型预热"""

        # todo 这里边是对所有子模型的 warm up


    def detect(self):
        """检测"""

    def read_cfg(self):
        """读取配置"""

    def do_test(self):
        """检测模型是否能正常运行，需要每一个子模型都进行检测"""

