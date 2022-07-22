# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import os
import random
from JoTools.utils.TxtUtil import TxtUtil

txt_path = r"C:\Users\14271\Desktop\del\mapdepot\uc.txt"

save_dir = r"C:\Users\14271\Desktop\del\mapdepot\random_url"

txt_table = TxtUtil.read_as_tableread_as_table(txt_path)


for i in range(10):
    random.shuffle(txt_table)
    save_path = os.path.join(save_dir, f"random_{i}" + os.path.split(txt_path)[1])
    TxtUtil.write_table_to_txt(txt_table, save_path, end_line='\n')






