# -*- coding: utf-8  -*-
# -*- author: jokker -*-


import os
from JoTools.utils.FileOperationUtil import FileOperationUtil
from JoTools.utils.PrintUtil import PrintUtil
from JoTools.utils.HashlibUtil import HashLibUtil
# todo 添加移动的记录，这样方便数据的还原

region_img_dir_list = [
    r"C:\data\fzc_优化相关资料\dataset_fzc\000_train_data_step_1\JPEGImages",
    r"C:\data\fzc_优化相关资料\dataset_fzc\000_0_标准测试集\JPEGImages",
    r"C:\data\003_塔下站人\train\JPEGImages"
]

new_img_dir = r"C:\data\003_塔下站人\train\td\JPEGImages"

index = 0
for each_img_path in FileOperationUtil.re_all_file(new_img_dir, endswitch=['.jpg', '.JPG', '.png', '.PNG']):
    # 计算 md5 值
    md5_str = HashLibUtil.get_file_md5(each_img_path)

    for each_img_dir in region_img_dir_list:
        # 数据集中的名字
        region_img_path = os.path.join(each_img_dir, md5_str + '.jpg')
        #
        if os.path.exists(region_img_path):
            os.remove(each_img_path)
            index += 1
            print("{0} remove : {1}".format(index, each_img_path))


