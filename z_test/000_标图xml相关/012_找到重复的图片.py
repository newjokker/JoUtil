# -*- coding: utf-8  -*-
# -*- author: jokker -*-


from JoTools.utils.HashlibUtil import HashLibUtil
from JoTools.utils.FileOperationUtil import FileOperationUtil
from JoTools.utils.PickleUtil import PickleUtil


img_dir = r"C:\data\fzc_优化相关资料\dataset_fzc\000_train_data_step_1\JPEGImages"

save_pkl_path = r"C:\Users\14271\Desktop\del\save_pkl\fzc_train_data.pkl"

# img_path_list = FileOperationUtil.re_all_file(img_dir, endswitch=['.jpg', '.JPG', '.png', '.PNG'])

# res = HashLibUtil.duplicate_checking( img_path_list)

# res = HashLibUtil.save_file_md5_to_pkl(img_dir, save_pkl_path=save_pkl_path)
#
#
# for each in res:
#     if len(res[each]) > 1:
#         print(each)

img_list = []

res = PickleUtil.load_data_from_pickle_file(save_pkl_path)

for each in res:
    if len(res[each]) > 1:

        for each_img in list(res[each])[1:]:
            img_list.append(each_img)

        # print(res[each])

FileOperationUtil.move_file_to_folder(img_list, r"C:\data\fzc_优化相关资料\dataset_fzc\000_train_data_step_1\999.找到的重复的数据", is_clicp=True)

# print(len(a))


