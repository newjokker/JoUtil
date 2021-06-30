# -*- coding: utf-8  -*-
# -*- author: jokker -*-


import hashlib
import shutil
import os
import datetime


class FileOperationUtil(object):
    """文件操作类"""

    @staticmethod
    def delete_folder(dir_path):
        """删除一个路径下的所有文件"""
        # todo 这个一般都是最后一步，所以如何解决删除文件报错的问题，可能是文件被程序在占用
        shutil.rmtree(dir_path)

    @staticmethod
    def create_folder(folder_path):
        """如果文件夹不存在创建文件夹，如果文件夹存在选择是否清空文件夹"""
        os.makedirs(folder_path, exist_ok=True)

    @staticmethod
    def bang_path(file_path):
        """将文件名给bang开，这样省的麻烦，只能是文件地址，文件夹不好 bang 开"""
        if not os.path.isfile(file_path):
            raise EOFError ("need correct file path")

        folder_path = os.path.split(file_path)
        file_name = os.path.splitext(folder_path[1])[0]
        file_suffix = os.path.splitext(folder_path[1])[1]
        return folder_path[0], file_name, file_suffix

    @staticmethod
    def re_all_file(file_path, func=None, endswitch=None):
        """返回文件夹路径下的所有文件路径（搜索文件夹中的文件夹）"""

        if not os.path.isdir(file_path):
            print("* not folder path")
            raise EOFError

        # result = []
        for i, j, k in os.walk(file_path):
            for each_file_name in k:

                # 过滤后缀不符合的路径
                if endswitch is not None:
                    _, end_str = os.path.splitext(each_file_name)
                    if end_str not in endswitch:
                        continue

                abs_path = i + os.sep + each_file_name
                if func is None:
                    # result.append(abs_path)
                    yield abs_path
                else:
                    if func(abs_path):
                        # result.append(os.path.join(i, each_file_name))
                        yield os.path.join(i, each_file_name)
        # return result

    @staticmethod
    def re_all_folder(folder_path):
        """返回找到的所有文件夹的路径"""
        # fixme 可以用生成器写，这样就不用等扫描完了再去操作了
        if not os.path.isdir(folder_path):
            print(" 不是文件夹路径 ")
            raise EOFError

        # result = []
        for i, j, k in os.walk(folder_path):
            for each_dir_name in j:
                abs_path = i + os.sep + each_dir_name
                # result.append(abs_path)
                yield abs_path
        # return result

    @staticmethod
    def get_file_describe_dict(file_path):
        """文件描述，返回需要的文件描述信息"""
        desrb = {'_size_': str(round(float(os.path.getsize(file_path)) / 1024 ** 2, 4)) + ' M',
                 'a_time': datetime.datetime.utcfromtimestamp(os.path.getatime(file_path)),
                 'c_time': datetime.datetime.utcfromtimestamp(os.path.getctime(file_path)),
                 'm_time': datetime.datetime.utcfromtimestamp(os.path.getmtime(file_path))}
        return desrb

    @staticmethod
    def move_file_to_folder(file_path_list, assign_folder, is_clicp=False):
        """将列表中的文件路径全部拷贝或者剪切到指定文件夹下面，is_clip 是否剪切，否就是复制"""
        for each_file_path in file_path_list:
            # 过滤掉错误的文件路径
            if not os.path.isfile(each_file_path):
                print("file not exist : {0}".format(each_file_path))
                continue
            #
            new_file_path = os.path.join(assign_folder, os.path.split(each_file_path)[1])
            #
            new_file_dir = os.path.dirname(new_file_path)
            if not os.path.exists(new_file_dir):
                os.makedirs(new_file_dir)
            #
            if is_clicp:
                shutil.move(each_file_path, new_file_path)
            else:
                shutil.copyfile(each_file_path, new_file_path)

    @staticmethod
    def merge_root_dir(root_dir_1, root_dir_2, is_clip=False):
        """对 root 文件夹进行合并，两个 root 文件夹及其包含的子文件夹，A(a,b,c), B(b,c,d) 那么将 A B 中的 b,c 文件夹中的内容进行合并，并复制 a, d , is_clip 是否使用剪切的方式进行合并"""
        for each_name in os.listdir(root_dir_2):
            each_path = os.path.join(root_dir_2, each_name)
            each_releate_path = os.path.join(root_dir_1, each_name)

            if os.path.isdir(each_path):
                if os.path.exists(each_releate_path):
                    FileOperationUtil.merge_root_dir(each_releate_path, each_path)
                else:
                    shutil.move(each_path, each_releate_path)   # 递归
            else:
                if os.path.exists(each_releate_path):
                    print("* {0} has exists".format(each_releate_path))
                else:
                    if is_clip is False:
                        shutil.copy(each_path, each_releate_path)
                    else:
                        shutil.move(each_path, each_releate_path)

    # ------------------------------------ need repair -----------------------------------------------------------------

    @staticmethod
    def get_father_path(str_temp):
        """ 查找父文件夹，mac 和 windows 环境下都能运行"""
        # 去掉末尾的 '\' 和 '/'
        # str_temp = str_temp.rstrip(r'/')
        # str_temp = str_temp.rstrip(r'\\')
        str_temp = str_temp.rstrip(os.sep)
        return os.path.split(str_temp)[0]

    @staticmethod
    def clear_empty_folder(dir_path):
        """删除空文件夹, 考虑文件夹中只有空文件夹的情况，出现的话需要再次跑一遍程序，遍历删除文件夹"""
        del_num = 0
        for each_folder_path in FileOperationUtil.re_all_folder(dir_path):
            if not os.listdir(each_folder_path):
                shutil.rmtree(each_folder_path)
                del_num += 1
                print("* del {0}".format(each_folder_path))
                if del_num >= 1:
                    FileOperationUtil.clear_empty_folder(dir_path)

    @staticmethod
    def find_diff_file(file_list_1, file_list_2, func=None):
        """根据文件名是否相同定义文件是否相同，对比两个列表中的文件的差异"""
        file_name_dict_1, file_name_dict_2 = dict(), dict()
        #
        for each_file_path in file_list_1:
            each_file_name = os.path.split(each_file_path)[1]
            each_file_name = func(each_file_name) if func is not None else each_file_name
            file_name_dict_1[each_file_name] = each_file_path
        #
        for each_file_path in file_list_2:
            each_file_name = os.path.split(each_file_path)[1]
            each_file_name = func(each_file_name) if func is not None else each_file_name
            file_name_dict_2[each_file_name] = each_file_path

        # 那些 a 不在 b 中 , b 不在 a 中的，都记下来
        res = {"inanotb":[], "inbnota":[]}
        #
        for each_name_1 in file_name_dict_1:
            if each_name_1 not in file_name_dict_2:
                res["inanotb"].append(file_name_dict_1[each_name_1])
        #
        for each_name_2 in file_name_dict_2:
            if each_name_2 not in file_name_dict_1:
                res["inbnota"].append(file_name_dict_2[each_name_2])

        return res

    @staticmethod
    def divide_file_equally(file_dir, save_dir, divide_count=1, need_endswitch=None, assign_name='part_', is_clip=False):
        """均分文件"""

        # 初始化数据结构
        file_dict = {}
        for i in range(divide_count):
            file_dict[i] = []

        # 遍历分配数据
        index = 0
        for each_file in FileOperationUtil.re_all_file(file_dir, endswitch=need_endswitch):
            file_dict[index].append(each_file)
            if index < divide_count-1:
                index += 1
            else:
                index = 0
            print(index)

        # 移动数据
        for each_key in file_dict:
            each_save_dir = os.path.join(save_dir, assign_name+str(each_key+1))
            os.makedirs(each_save_dir, exist_ok=True)
            FileOperationUtil.move_file_to_folder(file_dict[each_key], assign_folder=each_save_dir, is_clicp=is_clip)


class HashLibUtil(object):

    @staticmethod
    def get_file_md5(file_path):
        """获取文件的 MD5 值"""
        md5 = hashlib.md5()
        with open(file_path, 'rb') as xml_file:
            md5.update(xml_file.read())
            return md5.hexdigest()

    @staticmethod
    def is_the_same_file(file_path_1, file_path_2):
        """判断两个文件是否是一个文件"""
        md5_1 = HashLibUtil.get_file_md5(file_path_1)
        md5_2 = HashLibUtil.get_file_md5(file_path_2)
        return True if md5_1 == md5_2 else False

    @staticmethod
    def duplicate_checking(file_path_list):
        """文件查重，输出重复的文件，放在一个列表里面
        DS : [[file_path_1, file_path_2], []]"""
        file_md5 = {}
        res = []
        # 计算所有文件的 md5 值
        for index, each_file_path in enumerate(file_path_list):
            print(index, each_file_path)
            md5 = HashLibUtil.get_file_md5(each_file_path)
            if md5 in file_md5:
                file_md5[md5].append(each_file_path)
            else:
                file_md5[md5] = [each_file_path]
        # 将有重复的文件放到列表中
        for each_md5 in file_md5:
            if len(file_md5[each_md5]) > 1:
                res.append(file_md5[each_md5])
        return res

    @staticmethod
    def leave_one(img_dir, save_dir=None, endswith=(".jpg", ".png", ".JPG", ".PNG"), del_log_path=None):
        """检查路径下面有没有重复的文件，把所有不重复的文件复制到指定文件夹，或者直接在当前文件夹删除"""
        md5_set = set()
        del_list = []
        file_count_sum = 0
        del_file_count = 0
        for each_img_path in FileOperationUtil.re_all_file(img_dir, lambda x:str(x).endswith(endswith)):
            each_md5 = HashLibUtil.get_file_md5(each_img_path)
            file_count_sum += 1
            if each_md5 not in md5_set:
                md5_set.add(each_md5)
                if save_dir is not None:
                    each_save_path = os.path.join(save_dir, os.path.split(each_img_path)[1])
                    shutil.copyfile(each_img_path, each_save_path)
            else:
                if save_dir is None:
                    # 不另存为文件夹，就直接在当前文件夹中将重复的图片删除
                    print("remove : {0}".format(each_img_path))
                    del_list.append((each_md5, each_img_path))
                    os.remove(each_img_path)
                    del_file_count += 1
        # 保存删除的 log
        if del_log_path:
            with open(del_log_path, 'a') as log_txt:
                for each_line in del_list:
                    log_txt.write(each_line[0] + ' : ' + each_line[1])
                    log_txt.write('\n')
        return file_count_sum, del_file_count

    # @staticmethod
    # def save_file_md5_to_pkl(file_dir, save_pkl_path, need_file_type=None, assign_file_path_file=None, each_file_count=1000):
    #     """将制定路径下面的所有文件的 md5 和 路径组成的字典保存到 pkl 文件中"""
    #
    #     # 执行需要计算 md5 值的数据的类型
    #     if need_file_type is None:
    #         need_file_type = ['.jpg', '.JPG', '.png', '.PNG']
    #     # 可以指定过滤已经扫描过的目录
    #     if assign_file_path_file:
    #         md5_dict = PickleUtil.load_data_from_pickle_file(assign_file_path_file)
    #         file_path_set = set()
    #         for each_file_Path_set in md5_dict.values():
    #             file_path_set = set.union(each_file_Path_set, file_path_set)
    #     else:
    #         file_path_set = set()
    #         md5_dict = {}
    #
    #     print('-'*50)
    #     print("start file_path_set length   : ", len(file_path_set))
    #     print("start md5 dict length        : ", len(md5_dict))
    #
    #     try:
    #         find_index = 0
    #         for each_file_path in FileOperationUtil.re_all_file(file_dir, endswitch=need_file_type):
    #             # 过滤已经扫描过的目录
    #             if each_file_path not in file_path_set:
    #                 file_path_set.add(each_file_path)
    #             else:
    #                 continue
    #
    #             find_index += 1
    #             print(find_index, each_file_path)
    #
    #             # save file
    #             if find_index % each_file_count == 0:
    #                 PickleUtil.save_data_to_pickle_file(md5_dict, save_pkl_path)
    #
    #             each_md5 = HashLibUtil.get_file_md5(each_file_path)
    #
    #             if each_md5 not in md5_dict:
    #                 md5_dict[each_md5] = set()
    #                 md5_dict[each_md5].add(each_file_path)
    #             else:
    #                 md5_dict[each_md5].add(each_file_path)
    #
    #     except Exception as e:
    #         print('GOT ERROR---->')
    #         print(e)
    #         print(e.__traceback__.tb_frame.f_globals["__file__"])
    #         print(e.__traceback__.tb_lineno)
    #
    #     finally:
    #         # save_to_pickle
    #         PickleUtil.save_data_to_pickle_file(md5_dict, save_pkl_path)
    #         print("stop file_path_set length    : ", len(file_path_set))
    #         print("stop md5 dict length         : ", len(md5_dict))


if __name__ == "__main__":

    # 需要去重的文件夹路径
    img_dir = r"C:\Users\14271\Desktop\del\del_test"
    # 需要去重的文件路径
    endswith=(".JPG", ".PNG", ".jpg", ".png")
    # 删除日志
    del_log_path=r"C:\Users\14271\Desktop\del\del_test\del_log.txt"


    HashLibUtil.leave_one(img_dir=img_dir, endswith=endswith, del_log_path=del_log_path)

