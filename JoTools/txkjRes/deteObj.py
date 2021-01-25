# -*- coding: utf-8  -*-
# -*- author: jokker -*-


class DeteObj(object):
    """检测结果的一个检测对象，就是一个矩形框对应的信息"""

    def __init__(self, x1, y1, x2, y2, tag, conf=-1, assign_id=-1):
        """(x1,y1), (x2,y2) 左下角右上角"""
        self.conf = conf
        self.tag = tag
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.id=assign_id

    def do_offset(self, offset_x, offset_y):
        """对结果进行偏移"""
        self.x1 += offset_x
        self.x2 += offset_x
        self.y1 += offset_y
        self.y2 += offset_y

    def get_rectangle(self):
        """获取矩形范围"""
        return [self.x1, self.y1, self.x2, self.y2]

    def get_center_point(self):
        """得到中心点坐标"""
        return float(self.x1+self.x2)/2, float(self.y1+self.y2)/2

    def get_format_list(self):
        """得到标准化的 list 主要用于打印"""
        return [str(self.tag), int(self.x1), int(self.y1), int(self.x2), int(self.y2), format(float(self.conf), '.4f')]

    def get_area(self):
        """返回面积，面积大小按照像素个数进行统计"""
        return int(self.x2 - self.x1) * int(self.y2 - self.y1)

    def format_check(self):
        """类型检查和调整"""
        self.conf = float(self.conf)
        self.tag = str(self.tag)
        self.x1 = int(self.x1)
        self.y1 = int(self.y1)
        self.x2 = int(self.x2)
        self.y2 = int(self.y2)

    # ------------------------------------------------------------------------------------------------------------------

    def to_name_str(self):
        """信息保存为文件名"""
        name_str = "[{0},{1},{2},{3},{4}]_{5}_{6}".format(self.x1, self.y1, self.x2, self.y2, "'" + self.tag + "'", self.conf, self.id)
        return name_str

    def load_from_name_str(self, name_str):
        """从文件名获取信息"""
        conf_str, index_str = name_str.split('_')[-2:]
        loc_list_str = '_'.join(name_str.split('_')[:-2])
        self.x1, self.y1, self.x2, self.y2, self.tag = eval(loc_list_str)
        self.conf = float(conf_str)
        self.id = int(index_str)


if __name__ == "__main__":

    a = DeteObj(10,10,30,30,'ok_good')
    b = a.to_name_str()
    print(b)
    a.load_from_name_str(b)
    print(a.get_format_list())
