# -*- coding: utf-8  -*-
# -*- author: jokker -*-

from setuptools import setup


setup(

    name='JoUtil',                              # 打包起来的包的文件名
    version='0.0.1',                            # 版本
    description='a tools for TXKJ algo',        # 描述
    author='jokker',                            # 作者
    author_email='18761609908@163.com',         # 邮箱
    packages=['JoTools'],                       # 打包的python文件夹
    requires=[]                                 # 定义依赖哪些模块
    )


# 打包的命令
# 切换到 setup.py 文件所在文件夹
# python setup.py bdist_wheel