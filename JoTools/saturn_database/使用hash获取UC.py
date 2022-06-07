# -*- coding: utf-8  -*-
# -*- author: jokker -*-

# 看使用 python 实现数据结构中的 dict 部分代码

# 不使用一个专门的值用于记录分配了多少个 UC，而是根据指定的 MD5 直接分配碰撞得到的 UC 已分配的话再次碰撞

# 数据库中的表
    # md5 - UC 表
    #

# 图片还是不是按照现在这样文件夹的组织方式，还是说一个文件就是一个文件夹存放

# 需要有被动缓存的文件存在，小图，文件之类的

# 其他文件，除了 json 之外，也使用 一个 json 文件进行描述，json 文件中记录了此文件的类型之类的，UC 中也记录了文件的类型

#

from JoTools.utils.HashlibUtil import HashLibUtil
from JoTools.utils.FileOperationUtil import FileOperationUtil

img_dir = r"C:\Users\14271\Desktop\del_test"
size = 100000



for each_img in FileOperationUtil.re_all_file(img_dir, endswitch=['.jpg', '.JPG']):

    each_md5 = HashLibUtil.get_file_md5(each_img)

    each_hash = hash(each_md5) % size

    print(each_hash)





