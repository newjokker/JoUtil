# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import os
from JoTools.utils.JsonUtil import JsonUtil
from JoTools.utils.FileOperationUtil import FileOperationUtil




class UCI(object):

    def __init__(self, ucd_path=None):

        self.json_path = None
        self.save_dir = ""
        self.save_name = ""

        if ucd_path is None:
            return

        if os.path.exists(ucd_path):
            if str(ucd_path).endswith(".json"):
                self.json_path = ucd_path
            elif str(ucd_path).endswith(".uci"):
                pass


















