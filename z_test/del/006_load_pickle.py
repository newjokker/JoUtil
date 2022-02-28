# -*- coding: utf-8  -*-
# -*- author: jokker -*-

from JoTools.utils.PickleUtil import PickleUtil


# fixme 这个结果是不是把大图进行了切分，变成了多个小图，然后使用小图进项检测 ？

result_pkl_path = r"C:\Users\14271\Desktop\del\result.pkl"

result = PickleUtil.load_data_from_pickle_file(result_pkl_path)

# print(result)


for i in range(15):

    print(result[i])

    print('-'*50)



