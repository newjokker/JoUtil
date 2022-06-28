# -*- coding: utf-8  -*-
# -*- author: jokker -*-


from JoTools.utils.CompressFolderUtil import CompressFolderUtil




if __name__ == "__main__":

    folderPath = r"C:\Users\14271\Desktop\del\FCOS"
    saveFolder = r"C:\Users\14271\Desktop\compress_dir"
    new_folder = r"C:\Users\14271\Desktop\compress_new_dir"

    # CompressFolderUtil.compress_folder(folderPath, saveFolder)
    #
    # CompressFolderUtil.uncompress_folder(saveFolder, new_folder, endswitch=['.jpg', '.cpp'], ignore_empty_folder=True)
    CompressFolderUtil.uncompress_folder(saveFolder, new_folder, ignore_empty_folder=True)

