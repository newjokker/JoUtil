# -*- coding: utf-8  -*-
# -*- author: jokker -*-


class DeteObj(object):
    """检测结果的一个检测对象，就是一个矩形框对应的信息"""

    def __init__(self, x1=None, y1=None, x2=None, y2=None, tag="", conf=-1, assign_id=-1):
        """(x1,y1), (x2,y2) 左下角右上角"""
        self.conf = conf
        self.tag = tag
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.id=assign_id

    def __eq__(self, other):
        """等于"""

        # 类型不同返回 false
        if not isinstance(other, DeteObj):
            return False

        if self.x1 == other.x1 and self.x2 == other.x2 and self.y1 == other.y1 and self.y2 == other.y2 and self.tag == other.tag:
            return True
        else:
            return False

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

    def get_points(self):
        """返回四边形顺序上的四个点"""
        return [[self.x1,self.y1], [self.x2,self.y1], [self.x2,self.y2], [self.x1, self.y2]]

    def format_check(self):
        """类型检查和调整"""
        self.conf = float(self.conf)
        self.tag = str(self.tag)
        self.x1 = int(self.x1)
        self.y1 = int(self.y1)
        self.x2 = int(self.x2)
        self.y2 = int(self.y2)

    def deep_copy(self):
        """返回深拷贝对象"""
        return copy.deepcopy(self)

    def get_name_str(self):
        """信息保存为文件名"""
        name_str = "[{0},{1},{2},{3},{4},{5},{6}]".format(self.x1, self.y1, self.x2, self.y2, "'" + self.tag + "'", self.conf, self.id)
        return name_str

    def load_from_name_str(self, name_str):
        """从文件名获取信息"""
        self.x1, self.y1, self.x2, self.y2, self.tag, self.conf, self.id = eval(name_str)


if __name__ == "__main__":

    a = DeteObj(10,10,30,30,'ok_good')
    b = a.get_name_str()
    print(b)
    a.load_from_name_str(b)
    print(a.get_format_list())
