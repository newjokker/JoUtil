# -*- coding: utf-8  -*-
# -*- author: jokker -*-


from JoTools.utils.HashlibUtil import HashLibUtil
from JoTools.utils.PickleUtil import PickleUtil


img_dir = r"C:\data\fzc_优化相关资料\防振锤优化\000_标准测试集\img"
save_pkl_path = r"C:\Users\14271\Desktop\del\hash_test\456.pkl"


# HashLibUtil.save_file_img_to_pkl(file_dir=img_dir, save_pkl_path=save_pkl_path, each_file_count=200)
# HashLibUtil.save_file_img_to_pkl(file_dir=img_dir, save_pkl_path=save_pkl_path)
#


pkl_path = r"C:\Users\14271\Desktop\del\20210217_yuanshishuju.pkl"

md5_dict= PickleUtil.load_data_from_pickle_file(pkl_path)

index = 0
for each_md5 in md5_dict:
    if len(md5_dict[each_md5]) > 1:
        index += 1
        print(md5_dict[each_md5])


print(index)
# print(len(md5_dict))



