# -*- coding: utf-8  -*-
# -*- author: jokker -*-


from JoTools.utils.HashlibUtil import HashLibUtil
from JoTools.utils.FileOperationUtil import FileOperationUtil
from JoTools.utils.PickleUtil import PickleUtil

img_dir = r"F:\绝缘子数据\jyz_data\crop_0.5"
pkl_path = r"F:\绝缘子数据\crop_images\all_data_md5.pkl"

a = PickleUtil.load_data_from_pickle_file(pkl_path)

for each_img_path in FileOperationUtil.re_all_file(img_dir, endswitch=['.jpg']):
    each_md5 = HashLibUtil.get_file_md5(each_img_path)

    if each_md5 in a:
        print(each_img_path, each_md5)


# img_dir = r"F:\绝缘子数据\crop_images"
# save_dir = r"F:\绝缘子数据\crop_images\all_data_md5.pkl"
#
# HashLibUtil.save_file_md5_to_pkl(file_dir=img_dir, save_pkl_path=save_dir)
#
#
# HashLibUtil.get_file_md5()