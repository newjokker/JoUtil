# -*- coding: utf-8  -*-
# -*- author: jokker -*-

from setuptools import setup, find_packages

setup(

    name='JoUtil',                                                                          # 打包起来的包的文件名
    version='0.1.4',                                                                        # 版本
    description='a tools for TXKJ algo',                                                    # 描述
    author='jokker',                                                                        # 作者
    author_email='18761609908@163.com',                                                     # 邮箱
    requires=['numpy', 'pillow', 'pandas', 'easydict', 'matplotlib', 'imagehash'],          # 定义依赖哪些模块
    # 打包的python文件夹
    packages=['JoTools', 'JoTools/utils', 'JoTools/txkj', 'JoTools/for_csdn',
              'JoTools/for_csdn/word_pic', 'JoTools/for_csdn/find_same_img'],
    # packages=find_packages('JoTools'),          # 包含所有 JoTools 中的包
    package_data={
        'JoTools/for_csdn/word_pic': ['data/*.pkl'],
    },
    )


# 打包的命令
# 切换到 setup.py 文件所在文件夹
# python setup.py bdist_wheel

# 注意
# 需要将用到的包全部写到 packages 参数后
# 需要在 setup.py 同级目录创建一个 test.py 文件用于测试

# setuptools 的进一步学习参考：https://www.jianshu.com/p/ea9973091fdf
