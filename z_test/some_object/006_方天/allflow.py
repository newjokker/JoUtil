# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import subprocess
import os
import time
import shutil
from JoTools.utils.FileOperationUtil import FileOperationUtil
from JoTools.txkjRes.deteRes import DeteRes
from JoTools.utils.CsvUtil import CsvUtil

# ----------------------------------------------------------------------------------------------------------------------
cmd_str_1 = r"python3 scripts/all_models_flow.py --scriptIndex 3-1"
cmd_str_2 = r"python3 scripts/all_models_flow.py --scriptIndex 3-2"
cmd_str_3 = r"python3 scripts/all_models_flow.py --scriptIndex 3-3"
# ----------------------------------------------------------------------------------------------------------------------
img_dir = r"/usr/input_picture"
res_dir = r"/usr/output_dir/save_res"
log_path = r"/usr/output_dir/log"
csv_path = r"/usr/output_dir/result.csv"
# ----------------------------------------------------------------------------------------------------------------------

obj_name = "_all_flow"
time_str = str(time.time())[:10]

bug_file_1 = open(os.path.join("./logs", "bug1_" + time_str + obj_name + ".txt"), "w+")
bug_file_2 = open(os.path.join("./logs", "bug2_" + time_str + obj_name + ".txt"), "w+")
bug_file_3 = open(os.path.join("./logs", "bug3_" + time_str + obj_name + ".txt"), "w+")

std_file_1 = open(os.path.join("./logs", "std1_" + time_str + obj_name + ".txt"), "w+")
std_file_2 = open(os.path.join("./logs", "std2_" + time_str + obj_name + ".txt"), "w+")
std_file_3 = open(os.path.join("./logs", "std3_" + time_str + obj_name + ".txt"), "w+")

pid_1 = subprocess.Popen(cmd_str_1.split(), stdout=std_file_1, stderr=bug_file_1, shell=False)
time.sleep(30)
pid_2 = subprocess.Popen(cmd_str_2.split(), stdout=std_file_2, stderr=bug_file_2, shell=False)
time.sleep(30)
pid_3 = subprocess.Popen(cmd_str_3.split(), stdout=std_file_3, stderr=bug_file_3, shell=False)

print('-'*50)
print("pid_1 : {0}".format(pid_1.pid))
print("pid_2 : {0}".format(pid_2.pid))
print("time str : {0}".format(time_str))
print('-'*50)

# ----------------------------------------------------------------------------------------------------------------------

class SaveLog():

    def __init__(self, log_path, img_count, csv_path=None):
        self.log_path = log_path
        self.img_count = img_count
        self.img_index = 1
        self.csv_path = csv_path
        self.csv_list = [['filename', 'name', 'score', 'xmin', 'ymin', 'xmax', 'ymax']]
        # empty log
        if os.path.exists(self.log_path):
            os.remove(self.log_path)

    def add_log(self, img_name):
        self.log = open(self.log_path, 'a')
        self.log.write("process:{0}/{1} {2}\n".format(self.img_index, self.img_count, img_name))
        self.img_index += 1
        self.log.close()

    def add_csv_info(self, dete_res, img_name):
        #
        for dete_obj in dete_res:
            self.csv_list.append([img_name, dete_obj.tag, dete_obj.conf, dete_obj.x1, dete_obj.y1, dete_obj.x2, dete_obj.y2])

    def read_img_list_finshed(self):
        self.log = open(self.log_path, 'a')
        self.log.write("Loading Finished\n")
        self.log.close()

    def close(self):
        self.log = open(self.log_path, 'a')
        self.log.write("---process complete---\n")
        self.log.close()
        # save csv
        CsvUtil.save_list_to_csv(self.csv_list, self.csv_path)

# ----------------------------------------------------------------------------------------------------------------------

img_name_dict = {}
img_path_list = list(FileOperationUtil.re_all_file(img_dir, endswitch=['.jpg', '.JPG', '.png', '.PNG']))

for each_img_path in img_path_list:
    img_name = FileOperationUtil.bang_path(each_img_path)[1]
    img_name_dict[img_name] = os.path.split(each_img_path)[1]


img_count = len(img_path_list)
save_log = SaveLog(log_path, img_count, csv_path)
# fixme fix 02
save_log.read_img_list_finshed()

start_time = time.time()
max_use_time = 9.5 * img_count

dete_img_index = 1
while True:

    now_time = time.time()

    # over time
    if now_time - start_time > max_use_time:
        break
    # dete end
    # fixme fix 01
    elif save_log.img_index > save_log.img_count:
        break

    xml_path_list = FileOperationUtil.re_all_file(res_dir, endswitch=['.xml'])

    time.sleep(5)

    for each_xml_path in xml_path_list:
        print("* {0} {1}".format(dete_img_index, each_xml_path))
        img_name = img_name_dict[FileOperationUtil.bang_path(each_xml_path)[1]]
        try:
            # wait for write end
            time.sleep(0.1)
            each_dete_res = DeteRes(each_xml_path)
            save_log.add_csv_info(each_dete_res, img_name)
        except Exception as e:
            print(e)
            save_log.add_log(img_name)
            if os.path.exists(each_xml_path):
                os.remove(each_xml_path)
        dete_img_index += 1


save_log.close()

end_time = time.time()
img_count = len(img_path_list)
use_time = end_time - start_time
print("* check img {0} use time {1} {2} s/pic".format(img_count, use_time, use_time/img_count))









