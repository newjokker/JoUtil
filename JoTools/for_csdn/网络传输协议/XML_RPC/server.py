# -*- coding: utf-8  -*-
# -*- author: jokker -*-

from xmlrpc.server import SimpleXMLRPCServer
import cv2
import os
import numpy as np
from JoTools.utils.HashlibUtil import HashLibUtil


class KeyValueServer(object):
    _rpc_methods = ['get', 'set', 'delete', 'exists', 'keys']

    def __init__(self, address, db_dir=None):
        self._data = {}
        self._servre = SimpleXMLRPCServer(address, allow_none=True)
        for name in self._rpc_methods:
            self._servre.register_function(getattr(self, name))
        self.db_dir = db_dir

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
        return {}

    # ------------------------------------------------------------------------------------------------------------------

    def post_img(self, img_data, img_title='untreated'):
        img_np_arr = np.fromstring(img_data, np.uint8)
        frame = cv2.imdecode(img_np_arr, cv2.COLOR_BGR2RGB)
        save_dir = os.path.join(self.db_dir, img_title)
        os.makedirs(save_dir, exist_ok=True)
        save_path = os.path.join()
        cv2.imencode('.jpg', frame)[1].tofile(save_path)

    # ------------------------------------------------------------------------------------------------------------------



if __name__ == "__main__":

    kvserv = KeyValueServer(('0.0.0.0', 11222))
    kvserv.servre_forever()







