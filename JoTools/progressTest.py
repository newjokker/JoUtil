# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import progressbar
import time
import sys

a = progressbar.ProgressBar(100)

a.start()

for i in range(20):
    a.update(i * 5)

    time.sleep(0.2)
a.finish()
print("进度条完毕")
print("新的开始")


# print("test")
# #
# sys.stdout.write("# ")
# for i in range(20):  # 循环20次
#     # sys.stdout.write('\033[41;1m.\033[0m')  # 背景色为红色的点
#     sys.stdout.write('#')
#     # todo 进度条后面显示已经完成的比例
#     # print(sys.stdout.seek(i))
#     sys.stdout.seek(i + 1)
#     sys.stdout.flush()  # 边输出边刷新
#     time.sleep(0.1)
