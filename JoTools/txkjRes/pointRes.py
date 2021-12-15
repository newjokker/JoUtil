# -*- coding: utf-8  -*-
# -*- author: jokker -*-


from .resBase import ResBase


class PointRes(ResBase):

    def __init__(self, json_path=None, ):
        self._alarms = []
        self._log = log
        super().__init__(assign_img_path, json_dict, redis_conn_info=redis_conn_info, img_redis_key=img_redis_key, json_path=json_path)

    def __add__(self, other):
        if not isinstance(other, DeteRes):
            raise TypeError("should be DeteRes")

        res = self.deep_copy()
        for each_point_obj in other:
            if each_point_obj not in self:
                res.add_obj_2(each_point_obj)
        return res

    def __sub__(self, other):
        for each_dete_obj in other:
            self.del_dete_obj(each_dete_obj)
        return self

    def __contains__(self, item):
        if not(isinstance(item, DeteAngleObj) or isinstance(item, DeteObj)):
             raise TypeError("item should 被 DeteAngleObj or DeteObj")

        for each_point_obj in self._alarms:
            if item == each_point_obj:
                return True
        return False

    def __len__(self):
        return len(self._alarms)

    def __getitem__(self, item):
        return self._alarms[index]

    def __setattr__(self, key, value):
        object.__setattr__(self, key, value)
        #
        if key == 'img_path' and isinstance(value, str) and self.parse_auto:
            self._parse_img_info()
        elif key == 'json_path' and isinstance(value, str) and self.parse_auto:
            # self._parse_xml_info()
            pass
        elif key == 'json_dict' and isinstance(value, dict) and self.parse_auto:
            self._parse_json_info()

    @property
    def alarms(self):
        # return sorted(self._alarms, key=lambda x:x.id)
        return self._alarms

    def _parse_json_info(self):
        pass

    def save_to_json_file(self):
        pass

    def save_to_json_str(self):
        pass

    def draw_res(self):
        pass

    def print_as_fzc_format(self):
        pass

    def add_obj(self):
        pass

    def add_obj_2(self):
        pass

    def deep_copy(self, copy_img=False):

        if copy_img:
            return copy.deepcopy(self)
        else:
            a = DeteRes()
            a.parse_auto = False
            a.height = self.height
            a.width = self.width
            a.json_path = self.json_path
            a.img_path = self.img_path
            a.file_name = self.file_name
            a.folder = self.folder
            # img 是不进行深拷贝的，因为不会花很长的时间
            a.img = self.img
            a.json_dict = copy.deepcopy(self.json_dict)
            a.reset_alarms(copy.deepcopy(self.alarms))
            a.redis_conn_info = self.redis_conn_info
            a.img_redis_key = self.img_redis_key
            a.parse_auto = True
            return a

    def del_point_obj(self, assign_dete_obj):
        #
        for each_point_obj in copy.deepcopy(self._alarms):
            if each_point_obj == assign_dete_obj:
                # del each_dete_obj # 使用 del 删除不了
                self._alarms.remove(each_point_obj)
                # break or not
                if not del_all:
                    return







