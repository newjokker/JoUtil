# -*- coding: utf-8  -*-
# -*- author: jokker -*-

from xmlrpc.server import SimpleXMLRPCServer
import cv2
import os
import numpy as np
from JoTools.utils.HashlibUtil import HashLibUtil
from labelme import utils
import hashlib
import pickle
import uuid

def get_str_md5(assign_str):
    md5 = hashlib.md5()
    md5.update(assign_str)
    return md5.hexdigest()

# fixme 关闭的时候，文件保存到缓存文件夹中去

# fixme 可以指定日期进行查找

# fixme 每天的数据进行备份之类的

# fixme 搞一个定时服务，定时备份之类的

# fixme 有一个信息板，可以每个人看每天重要的信息



class KeyValueServer(object):
    _rpc_methods = ['get', 'set', 'delete', 'exists', 'keys',
                    'post_img']

    def __init__(self, address, user='any_one', db_dir=None):
        self._data = {}
        self._servre = SimpleXMLRPCServer(address, allow_none=True)
        for name in self._rpc_methods:
            self._servre.register_function(getattr(self, name))
        if db_dir is None:
            self.db_dir = './'
        else:
            self.db_dir = db_dir
        # --------
        self.user = user

    def get(self, name):
        return self._data[name]

    def set(self, name, value):
        self._data[name] = value

    def delete(self, name):
        del self._data[name]

    def exists(self, name):
        return name in self._data

    def keys(self):
        return list(self._data)

    def servre_forever(self):
        self._servre.serve_forever()

    def help(self):
        # todo 返回一个说明字典，这样能比较好地去使用其中的函数
        info_dict = {
            "get": None,
            "set": None,
            "delete": None,
            "exists": None,
            "keys": None,
            # --------------------
            "post_img": None,
            # --------------------
        }
        return info_dict

    # ------------------------------------------------------------------------------------------------------------------

    def post_img(self, img_data, img_title='untreated'):
        try:
            frame = pickle.loads(img_data.data)
            save_dir = os.path.join(self.db_dir, img_title)
            os.makedirs(save_dir, exist_ok=True)
            img_name = get_str_md5(img_data.data)
            save_path = os.path.join(save_dir, img_name + '.jpg')
            cv2.imencode('.jpg', frame)[1].tofile(save_path)
            return 200
        except Exception as e:
            print(e)
            print(e.__traceback__.tb_frame.f_globals["__file__"])
            print(e.__traceback__.tb_lineno)
            return 500

    # ------------------------------------------------------------------------------------------------------------------

    def get_todays_presentation(self):
        # 返回今天提交的所有内容
        pass

    def tack_board(self, message):
        # 布告板
        # 记录发布的人，时间
        # 能不能获取连接机器的 IP 地址
        pass



if __name__ == "__main__":

    kvserv = KeyValueServer(('0.0.0.0', 11222))
    kvserv.servre_forever()







