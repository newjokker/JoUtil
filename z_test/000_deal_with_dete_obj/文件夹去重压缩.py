# -*- coding: utf-8  -*-
# -*- author: jokker -*-


from JoTools.utils.CompressFolderUtil import CompressFolderUtil




if __name__ == "__main__":

    # fixme 没有后缀的文件好像处理的不对，重点看一下


    folderPath = r"C:\Users\14271\Desktop\del\test_no_suffix"
    saveFolder = r"C:\Users\14271\Desktop\compress_dir"

    # CompressFolderUtil.compress_folder(folderPath, saveFolder, is_clip=False)
    CompressFolderUtil.uncompress_folder(saveFolder, folderPath, ignore_empty_folder=True, is_clip=False)

