# -*- coding: utf-8  -*-
# -*- author: jokker -*-


from JoTools.utils.FileOperationUtil import FileOperationUtil


assign_dir = r"\\192.168.3.80\大金具-算法\qfm\连接件训练数据集"
save_dir = r"C:\Users\14271\Desktop\连接件"


FileOperationUtil.move_file_to_folder(FileOperationUtil.re_all_file(assign_dir, endswitch=['.xml']), save_dir, is_clicp=False)



config_path = r"D:\Algo\saturn_database\config.ini"

