# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import pickle
import uuid
import os
try:
    from cryptography.fernet import Fernet
except ImportError:
    print("import cryptography error : PickleUtil")


class PickleUtil(object):

    @staticmethod
    def load_data_from_pickle_file(pickle_file_path):
        with open(pickle_file_path, 'rb') as pickle_file:
            return pickle.load(pickle_file)

    @staticmethod
    def save_data_to_pickle_file(data, pickle_file_path):
        with open(pickle_file_path, 'wb') as pickle_file:
            pickle.dump(data, pickle_file)

    @staticmethod
    def encrypt_pickle(pkl_path, save_path, assign_key=b'OoxJ5trGpWprm9GAZqP0iHo6xdjEqMapOe3EDZ-r3QU='):
        cipher = Fernet(assign_key)

        # 加密 pickle 文件
        with open(pkl_path, 'rb') as f:
            encrypted_data = cipher.encrypt(f.read())

        # 保存加密的文件
        with open(save_path, 'wb') as f:
            f.write(encrypted_data)

        return assign_key

    @staticmethod
    def decrypt(pkl_path, save_path=None, assign_key=b'OoxJ5trGpWprm9GAZqP0iHo6xdjEqMapOe3EDZ-r3QU='):
        cipher = Fernet(assign_key)
        file_dir, file_name = os.path.split(pkl_path)
        # 解密加密的 pickle 文件
        with open(pkl_path, 'rb') as f:
            decrypted_data = cipher.decrypt(f.read())

        # 保存解密后的数据为新文件
        if save_path:
            locked_file_path = save_path
        else:
            locked_file_path = os.path.join(file_dir, "locked_" + str(uuid.uuid1()) + file_name)

        with open(locked_file_path, 'wb') as f:
            f.write(decrypted_data)

        # 反序列化解密后的数据
        with open(locked_file_path, 'rb') as f:
            data = pickle.load(f)

        # 删除缓存文件
        if os.path.exists(locked_file_path) and (locked_file_path is None):
            os.remove(locked_file_path)

        return data

if __name__ == '__main__':

    # from JoTools.txkjRes.deteRes import DeteRes
    #
    # a = DeteRes(r"C:\Users\14271\Desktop\del\gt_xml\005305_jpg.rf.4bfbcf630358ee01c2a6a2c1da620f63.xml")
    #
    # a.print_as_fzc_format()
    #
    pickle_path = r'C:\Users\14271\Desktop\a.pkl'
    pickle_path_new = r'C:\Users\14271\Desktop\b.pkl'

    # PickleUtil.save_data_to_pickle_file(a, pickle_path)
    #
    # PickleUtil.encrypt_pickle(pickle_path, pickle_path)
    #
    # PickleUtil.decrypt(pickle_path, pickle_path_new)

    data = PickleUtil.load_data_from_pickle_file(pickle_path_new)

    data.print_as_fzc_format()

    print(data.__doc__)



