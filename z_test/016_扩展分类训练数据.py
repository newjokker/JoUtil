# -*- coding: utf-8  -*-
# -*- author: jokker -*-



from JoTools.txkj.imageAugmentation import ImageAugmentation
from JoTools.utils.FileOperationUtil import FileOperationUtil


img_dir = r"C:\Users\14271\Desktop\classify_step_1.5\fzc_broken\normal"
out_dir = r"C:\Users\14271\Desktop\classify_step_1.5\fzc_broken\normal_extend"
# 期望扩展的图片的数量
expect_img_num = 5000

imgs_list = FileOperationUtil.re_all_file(img_dir, lambda x: str(x).endswith('.jpg'))  # 遍历找到文件夹中符合要求的图片
# 计算得到为了达到期望扩展图片量，需要的 prob 值
img_count = len(imgs_list)
prob = expect_img_num/float(img_count * 12)

a = ImageAugmentation(imgs_list, out_dir, prob=prob)
a.mode = 0
a.do_process()



