# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import os

class ShellUtil():

    @staticmethod
    def shell_str(shell_str, interpreter='python3'):

        py_path = r"D:\Algo\jo_util\z_test\000_deal_with_dete_obj\001_count_tags.py"

        cmd_str = "{0} {1} {2}".format(interpreter, py_path, shell_str)
        os.system(cmd_str)



if __name__ == "__main__":


    ShellUtil.shell_str(r"--xml_dir C:\Users\14271\Desktop\del\old_output_dir")










