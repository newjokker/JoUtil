# -*- coding: utf-8  -*-
# -*- author: jokker -*-



txt_path = r"D:\Algo\jo_util\JoTools\for_csdn\translate\data\VGG.txt"




class Translate():

    def __init__(self, txt_path=None):
        self.txt_path = txt_path
        self.txt_info = []

    def load_data_from_txt(self):
        txt_info = []
        with open(self.txt_path, 'r') as txt_file:
            for each_line in txt_file:
                each_line = each_line.strip()
                if each_line:
                    txt_info.append(each_line)

    def do_format(self):
        for each in txt_info:
            print(each)

    def save_to_xml(self):
        pass



