# -*- coding: utf-8  -*-
# -*- author: jokker -*-



from JoTools.txkj.imageAugmentation import ImageAugmentation
from JoTools.utils.FileOperationUtil import FileOperationUtil


img_dir = r"C:\Users\14271\Desktop\classify_step_1.5\zd_yt\zd_yt"
out_dir = r"C:\Users\14271\Desktop\classify_step_1.5\zd_yt\zd_yt_extend"

# for each_dir in os.listdir(out_folder):
#     each_dir_path = os.path.join(out_folder, each_dir)
#     imgs_list = FileOperationUtil.re_all_file(each_dir_path, lambda x:str(x).endswith('.jpg'))  # 遍历找到文件夹中符合要求的图片
#     a = ImageAugmentation(imgs_list, each_dir_path)
#     a.mode = 0
#     a.do_process()


imgs_list = FileOperationUtil.re_all_file(img_dir, lambda x: str(x).endswith('.jpg'))  # 遍历找到文件夹中符合要求的图片
a = ImageAugmentation(imgs_list, out_dir, prob=1)
a.mode = 1
a.do_process()



