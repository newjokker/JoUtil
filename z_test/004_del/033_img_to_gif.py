# -*- coding: utf-8  -*-
# -*- author: jokker -*-


from JoTools.utils.FileOperationUtil import FileOperationUtil
from JoTools.utils.GifUtil import GifUtil


img_dir = r"C:\Users\14271\Desktop\fake_face"

img_path_list = list(FileOperationUtil.re_all_file(img_dir, endswitch=['.jpg', '.JPG']))



img_dict = {}

for each_img in img_path_list:
    img_index = float(FileOperationUtil.bang_path(each_img)[1])
    img_dict[img_index] = each_img
    # print(img_index)

img_keys = list(img_dict.keys())
img_keys = sorted(img_keys)

img_list_new = []
for index, each_index in enumerate(img_keys):

    if index %2 != 0:
        continue

    if index > 200:
        continue

    img_list_new.append(img_dict[each_index])


GifUtil.img_list_to_gif(img_list_new, r"C:\Users\14271\Desktop\fack_img_face.gif", time_gap=0.2)

