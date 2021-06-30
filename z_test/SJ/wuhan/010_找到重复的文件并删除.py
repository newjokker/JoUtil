# -*- coding: utf-8  -*-
# -*- author: jokker -*-


from JoTools.utils.JsonUtil import JsonUtil
import os
from JoTools.utils.HashlibUtil import HashLibUtil
from JoTools.utils.FileOperationUtil import FileOperationUtil
# from JoTools.utils.JsonUtil import JsonUtil

# img_dir = r"D:\算法培育-7月样本"
# save_dir = r"C:\Users\jokker\Desktop\md5_file"

# img_dir = r"C:\data\fzc_优化相关资料\dataset_fzc\000_train_data_step_1\img"
# save_dir = r"C:\Users\14271\Desktop\del\md5"
#
# md5_dict = {"md5_list": []}
#
# index = 0
# for each_img_path in FileOperationUtil.re_all_file(img_dir, lambda x:str(x).endswith(('.jpg', '.JPG'))):
#     each_md5 = HashLibUtil.get_file_md5(each_img_path)
#     md5_dict["md5_list"].append(each_md5)
#     index += 1
#     print(index)
#
# save_path = os.path.join(save_dir, "md5_old_train_data.json")
# JsonUtil.save_data_to_json_file(md5_dict, save_path)
#


wh = JsonUtil.load_data_from_json_file(r"C:\Users\14271\Desktop\del\md5\md5_old_train_data.json")["md5_list"]



img_dir = r"C:\Users\14271\Desktop\del\新防振锤数据武汉电科院"

index = 0
for each_img_path in FileOperationUtil.re_all_file(img_dir, lambda x:str(x).endswith(('.jpg', '.JPG'))):
    each_md5 = HashLibUtil.get_file_md5(each_img_path)

    # 如果文件 md5 已存在，就删除这个文件

    if each_md5 in wh:
        os.remove(each_img_path)

        each_xml_path = each_img_path[:-3] + 'xml'
        if os.path.exists(each_xml_path):
            os.remove(each_xml_path)

        print("remove file : {0}".format(each_img_path))
