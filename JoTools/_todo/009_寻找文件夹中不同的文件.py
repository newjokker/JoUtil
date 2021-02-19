# -*- coding: utf-8  -*-
# -*- author: jokker -*-

from JoTools.utils.FileOperationUtil import FileOperationUtil


crop_old_dir = r"C:\Users\14271\Desktop\del\test001"
crop_new_dir = r"C:\Users\14271\Desktop\del\test002"


def test(each_file_name):
    a = each_file_name[each_file_name.rfind("-+-"):]
    b = a.split(",")
    each_file_name = each_file_name[:each_file_name.rfind("-+-")] + ",".join(b[:5])
    # print(each_file_name)
    return each_file_name

res = FileOperationUtil.find_diff_file(
    FileOperationUtil.re_all_file(crop_old_dir, lambda x:str(x).endswith('.jpg')),
    FileOperationUtil.re_all_file(crop_new_dir, lambda x:str(x).endswith('.jpg')),
    func = test
)


for each in res['inanotb']:
    print(each)

print('-'*20)

for each in res['inbnota']:
    print(each)


# print(len(res['inanotb']))
# print(len(res['inbnota']))

# FileOperationUtil.move_file_to_folder(res['inanotb'], r"C:\Users\14271\Desktop\fzc_train_new\diff_crop", is_clicp=False)
#
#
# # print(res)
# print("ok")