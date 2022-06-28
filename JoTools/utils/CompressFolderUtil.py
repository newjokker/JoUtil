# -*- coding: utf-8  -*-
# -*- author: jokker -*-


import os
import shutil
from JoTools.utils.FileOperationUtil import FileOperationUtil
from JoTools.utils.HashlibUtil import HashLibUtil


class CompressFolderUtil(object):
    """压缩文件夹"""

    @staticmethod
    def compress_folder(folder_path, save_folder, endswitch=None, is_clip=False):
        """压缩文件夹"""
        txt_path = os.path.join(save_folder, 'all_file_info.txt')
        data_folder = os.path.join(save_folder, 'data')
        os.makedirs(data_folder, exist_ok=True)
        with open(txt_path, 'w', encoding='utf-8') as txt_file:
            # save file info
            for each_file_path in FileOperationUtil.re_all_file(folder_path, endswitch=endswitch):
                each_md5 = HashLibUtil.get_file_md5(each_file_path)
                file_suffix = FileOperationUtil.bang_path(each_file_path)[2]
                txt_file.write(f'file,{each_md5},{each_file_path[len(folder_path):-len(file_suffix)]},{file_suffix}\n')
                each_save_path = os.path.join(data_folder, f'{each_md5}{file_suffix}')
                if is_clip:
                    shutil.move(each_file_path, each_save_path)
                else:
                    shutil.copy(each_file_path, each_save_path)
            # save folder info
            for each_folder_path in FileOperationUtil.re_all_folder(folder_path, recurse=True):
                txt_file.write(f'folder,{each_folder_path[len(folder_path):]}\n')

    @staticmethod
    def uncompress_folder(folder_path, save_folder_path, ignore_empty_folder=False, endswitch=None, is_clip=False):
        """解压缩文件夹"""
        txt_path = os.path.join(folder_path, 'all_file_info.txt')
        data_folder = os.path.join(folder_path, 'data')

        with open(txt_path, 'r') as txt_file:
            for each_line in txt_file:
                if each_line.startswith('file'):
                    # uncompress file
                    _, md5, file_path, suffix = each_line.strip().split(',')

                    # filter by suffix
                    if endswitch is not None:
                        if suffix not in endswitch:
                            continue

                    md5_path = os.path.join(data_folder, md5 + suffix)
                    save_file_path = os.path.join(save_folder_path, file_path.strip(os.sep) + suffix)
                    each_save_folder = os.path.split(save_file_path)[0]
                    os.makedirs(each_save_folder, exist_ok=True)
                    if is_clip:
                        shutil.move(md5_path, save_file_path)
                    else:
                        shutil.copy(md5_path, save_file_path)
                elif each_line.startswith('folder'):
                    # uncpress folder
                    _, folder_path = each_line.strip().split(',')
                    save_folder = os.path.join(save_folder_path, folder_path.strip(os.sep))
                    if not ignore_empty_folder:
                        os.makedirs(save_folder, exist_ok=True)
                else:
                    raise TypeError("* parse line error")

