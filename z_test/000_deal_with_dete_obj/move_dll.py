# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import os
import shutil


# ----------------------------------------------------------------------------
require_txt_path = r"C:\Users\14271\Desktop\del\require.txt"
save_dir = r"./dlls"
# ----------------------------------------------------------------------------

os.makedirs(save_dir, exist_ok=True)

with open(require_txt_path, 'r') as txt_path:

    for each in txt_path:

        each = each.strip()
        #
        if "=>" in each:
            each = each.split("=>")[1]

        each = each.split(" (")[0].strip()

        # save_path = os.path.join(save_dir, os.path.split(each)[1])
        # shutil.copy(each, save_path)

        print(each)







