# -*- coding: utf-8  -*-
# -*- author: jokker -*-


from JoTools.operateDeteRes import OperateDeteRes


# fixme 将代码都改为并行的，这样在文件处理操作的时候要快很多！
# fixme 小文件处理并行
# todo 写一个并行的框架，别的函数能很好的直接用进去，或者将方法当做参数传进去

# img_dir = r"C:\Users\14271\Desktop\寻找未被发现的fzc_broken\JPEGImages"
# xml_dir = r"C:\Users\14271\Desktop\寻找未被发现的fzc_broken\Annotations"
# save_dir = r"C:\Users\14271\Desktop\寻找未被发现的fzc_broken\crop_0.1"

# img_dir = r"C:\data\fzc_优化相关资料\dataset_fzc\000_train_data_step_1\JPEGImages"
# xml_dir = r"C:\data\fzc_优化相关资料\dataset_fzc\000_train_data_step_1\Annotations"
# save_dir = r"C:\data\fzc_优化相关资料\dataset_fzc\001_train_data_step_1.5\fzc_v0.2.5.x_classify\crop_0.1"

img_dir = r"C:\Users\14271\Desktop\锈蚀"
xml_dir = r"C:\Users\14271\Desktop\fzc_v1.2.5.5-F_006_rust"
save_dir = r"C:\Users\14271\Desktop\crop"


# OperateDeteRes.crop_imgs(img_dir, xml_dir, save_dir, split_by_tag=True, augment_parameter=[0.3, 0.3, 0.3, 0.3], exclude_tag_list=['correct_fzc'])
# OperateDeteRes.crop_imgs(img_dir, xml_dir, save_dir, split_by_tag=True, augment_parameter=[0.3, 0.3, 0.3, 0.3])
# OperateDeteRes.crop_imgs(img_dir, xml_dir, save_dir, split_by_tag=True, exclude_tag_list=["correct_Fnormal", "miss_Fnormal"], augment_parameter=[0.1, 0.1, 0.1, 0.1])
OperateDeteRes.crop_imgs(img_dir, xml_dir, save_dir, split_by_tag=True, exclude_tag_list=["Fnormal"], augment_parameter=[0.1, 0.1, 0.1, 0.1])
# OperateDeteRes.crop_imgs(img_dir, xml_dir, save_dir, split_by_tag=True, augment_parameter=[0.1, 0.1, 0.1, 0.1])

