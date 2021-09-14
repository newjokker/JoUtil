# -*- coding: utf-8  -*-
# -*- author: jokker -*-


from JoTools.utils.FileOperationUtil import FileOperationUtil


seg_dir = r"E:\jyz_data_segment\data"


ok_file_path_list = []
error_file_path_list = []

for each_json_path in FileOperationUtil.re_all_file(seg_dir, endswitch=['.json']):
    json_name = FileOperationUtil.bang_path(each_json_path)[1]
    if '[' in json_name and ']' in json_name:
        ok_file_path_list.append(each_json_path)
    else:
        error_file_path_list.append(each_json_path)


FileOperationUtil.move_file_to_folder(ok_file_path_list, r"E:\jyz_data_segment\train_json")
FileOperationUtil.move_file_to_folder(error_file_path_list, r"E:\jyz_data_segment\val_json")














