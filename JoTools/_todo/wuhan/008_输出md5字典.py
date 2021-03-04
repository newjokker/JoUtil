
import os
from JoTools.utils.HashlibUtil import HashLibUtil
from JoTools.utils.FileOperationUtil import FileOperationUtil
# from JoTools.utils.JsonUtil import JsonUtil

# img_dir = r"D:\算法培育-7月样本"
# save_dir = r"C:\Users\jokker\Desktop\md5_file"

img_dir = r"D:\集中培育-11月样本"
save_dir = r"C:\Users\jokker\Desktop\md5_file"

md5_dict = {"md5_list": []}

index = 0
for each_img_path in FileOperationUtil.re_all_file(img_dir, lambda x:str(x).endswith(('.jpg', '.JPG'))):
    each_md5 = HashLibUtil.get_file_md5(each_img_path)
    md5_dict["md5_list"].append(each_md5)
    index += 1
    print(index)

# 查看多少张图片
print(len(md5_dict["md5_list"]))
# 查看多少张不重复的图片
print(len(set(md5_dict["md5_list"])))




#
# save_path = os.path.join(save_dir, "md5_11.json")
# JsonUtil.save_data_to_json_file(md5_dict, save_path)


# a = JsonUtil.load_data_from_json_file(save_path)
#
# for each in a["md5_list"]:
#     print(each)
#

