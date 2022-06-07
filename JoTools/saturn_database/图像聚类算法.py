# -*- coding: utf-8  -*-
# -*- author: jokker -*-
import os
import shutil
import numpy as np
from sklearn.cluster import KMeans, DBSCAN
from JoTools.txkjRes.deteRes import DeteRes
from JoTools.utils.FileOperationUtil import FileOperationUtil
from JoTools.utils.PickleUtil import PickleUtil
from JoTools.utils.DecoratorUtil import DecoratorUtil

# todo 根据图像 prebase 的检测结果，进行聚类

# 两个特征矩阵之间的距离的计算（1）考虑种类的相似性（2）考虑相同种类个数的相似性
# 特征矩阵的维度为 M * N * K ， M N 为 空间上 M * N 个格子空间， K 为 有 K 个类型的标签，每一个格子中的值代表在一块格子空间中某一种要素的个数

def get_feature_from_dete_res(dete_res, K_list, M=5, N=5):
    """从dete_res拿到特征矩阵"""

    feature_array = np.zeros((M, N, len(K_list)), dtype=np.int)
    width, height = dete_res.width, dete_res.height
    for each_obj in dete_res:
        c_x = ((each_obj.x1 + each_obj.x2)/2.0) / width
        c_y = ((each_obj.y1 + each_obj.y2)/2.0) / height
        tag = each_obj.tag
        feature_array[int(c_x * M), int(c_y * N), K_list.index(tag)] += 1
    return feature_array.flatten()

@DecoratorUtil.time_this
def get_k_means_model(xml_dir, cluser_res, K_list, M=5, N=5):

    feature_list = []
    uc_list = []
    index = 0
    for each_xml_path in FileOperationUtil.re_all_file(xml_dir, endswitch=['.xml'], func=lambda x: 'flip' not in x):
        index += 1
        uc_list.append(FileOperationUtil.bang_path(each_xml_path)[1])
        print(index, each_xml_path)
        a = DeteRes(xml_path=each_xml_path)
        featuer_array = get_feature_from_dete_res(a, K_list, M=M, N=N)
        feature_list.append(featuer_array)
    y_pred = KMeans(n_clusters=5, random_state=9).fit_predict(feature_list)
    #
    cluster_res = {}
    for i in range(len(uc_list)):
        each_uc = uc_list[i]
        each_type = y_pred[i]
        if each_type not in cluster_res:
            cluster_res[each_type] = [each_uc]
        else:
            cluster_res[each_type].append(each_uc)
    PickleUtil.save_data_to_pickle_file(cluster_res, cluser_res)



if __name__ == "__main__":

    imgDir = r"F:\输电基础前置数据\JPEGImages1"
    xmlDir = r"C:\Users\14271\Desktop\del\cluser_test"
    cluserRes = r"C:\Users\14271\Desktop\del\k_means_model.pkl"
    save_dir = r"C:\Users\14271\Desktop\cluser_test\test_004"

    # K_list = ['hdjyz', 'bilei', 'fuse', 'fuseht_miss', 'byq', 'byqht_miss', 'cpb', 'bg', 'tower_top', 'light',
    #           'tcjyz', 'NZXJ_sub', 'ZGB_sub', 'WTGB_sub', 'BGXJ_sub', 'byqht_nor', 'XXJ_sub', 'NXJ_sub', 'fuseht_nor',
    #           'switch', 'switchht_miss', 'bljyz', 'fhjyz', 'nc', 'switchht_nor']

    K_list = ['fzc', 'LXJT_set', 'UGH_sub', 'YJXJ_sub', 'ZHGH_sub', 'tower_hd', 'UBGB_sub', 'BGXJ_sub', 'tower_fnqn',
              'PGB_sub', 'ULS_sub', 'XCXJCT_sub', 'fhjyz', 'nc', 'ring', 'ringL', 'SXJ_set', 'WTGB_sub', 'L_set', 'LSJ_set',
              'SJB_sub', 'ZGB_sub', 'tower_yw', 'DBTZB_sub', 'LZC_set', 'PTDB_set', 'tcjyz', 'TXXJ_sub', 'tower_fn',
              'fzc_ps', 'XXXJ_sub', 'bljyz', 'tower_bhm', 'tower_td', 'tower_tj', 'dxjyz', 'LSSXJ_sub', 'TLH_set', 'fw',
              'XXH_sub', 'QYB_sub', 'tower_sign', 'LQ_set', 'TLX_set', 'PTTZB_sub', 'fzc_pair', 'LK_set', 'ccb',
              'TLD_set', 'GDGZ_sub', 'LLB_set', 'tower_zwdj']

    get_k_means_model(xmlDir, cluserRes, K_list=K_list, M=1, N=1)

    cluser_res = PickleUtil.load_data_from_pickle_file(cluserRes)
    #
    for each in cluser_res:
        each_save_dir = os.path.join(save_dir, str(each))
        os.makedirs(each_save_dir, exist_ok=True)
        for index, each_uc in enumerate(cluser_res[each]):
            region_img_path = os.path.join(imgDir, each_uc + '.jpg')
            save_img_path = os.path.join(each_save_dir, each_uc + '.jpg')
            shutil.copy(region_img_path, save_img_path)

            if index > 50:
                break
        print(each)

