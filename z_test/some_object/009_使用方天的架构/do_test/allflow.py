# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import os
import subprocess

time_str = "001"
obj_name = "test"

for i in range(5):
    each_cmd_str = r"python D:\Algo\jo_util\z_test\some_object\009_使用方天的架构\do_test\model.py"
    each_bug_file = open(os.path.join(r"C:\Users\14271\Desktop\logs", "bug{0}_".format(i) + time_str + obj_name + ".txt"), "w+")
    each_std_file = open(os.path.join(r"C:\Users\14271\Desktop\logs", "std1{0}_".format(i) + time_str + obj_name + ".txt"), "w+")
    each_pid = subprocess.Popen(each_cmd_str.split(), stdout=each_bug_file, stderr=each_std_file, shell=False)
    print("pid : {0}".format(each_pid.pid))
    print(each_cmd_str)

