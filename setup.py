# -*- coding: utf-8  -*-
# -*- author: jokker -*-

from setuptools import setup, find_packages

setup(

    name='SaturnTools',                                                                          # 打包起来的包的文件名
    version='2.0.2',                                                                        # 版本
    description='a tools for Saturn dete algo',                                             # 描述
    author='jokker',                                                                        # 作者
    author_email='18761609908@163.com',                                                     # 邮箱
    url='https://github.com/newjokker/JoUtil.git',

    install_requires=['numpy', 'pillow', 'pandas', 'easydict', 'matplotlib', 'imagehash', 'prettytable', 'progress',
              'progressbar', 'requests', 'imageio', 'pyexiv2', 'opencv-python', 'exifread', 'whatimage', 'pyheif',
              'pymysql', 'pytesseract', 'beautifulsoup4', 'Crypto', 'flask', 'shapely'
              ],          # 定义依赖哪些模块, https://pypi.tuna.tsinghua.edu.cn/simple

    # 打包的python文件夹AZ
    # packages=['SaturnTools/utils', 'SaturnTools/txkj', 'SaturnTools/txkjRes',
    #           # 'for_csdn/word_pic', 'for_csdn/find_same_img', 'for_csdn/the_art_of_war',
    #           ],
    packages=find_packages(include=['SaturnTools']),
    package_data={
        # 'JoTools/for_csdn/word_pic': ['data/*.pkl'],
        # 'JoTools/for_csdn/the_art_of_war': ['data/*.txt'],
    },
    long_description="""
    * jokker 常用的功能组成的包
    """,
    )

# ----------------------------------------------------------------------------------------------------------------------
# refer : https://zhuanlan.zhihu.com/p/276461821
# 打包的命令
# 切换到 setup.py 文件所在文件夹
# python setup.py bdist_wheel, 构建分法 build-distribution wheel 文件？
# python setup.py sdist ，打包为 zip 文件

# 注意
# 需要将用到的包全部写到 packages 参数后
# 需要在 setup.py 同级目录创建一个 test.py 文件用于测试
# requires 不能出现 *-* 格式的写法 如 scikit-image，否则会报错

# setuptools 的进一步学习参考：https://www.jianshu.com/p/ea9973091fdf

# ----------------------------------------------------------------------------------------------------------------------i
# 发布到 pypi 上去，refer : https://blog.csdn.net/Mecaly/article/details/135829634

# 生成一个文件 .pypirc 内容如下
"""
[pypi]
  username = __token__
  password = pypi-AgEIcHlwaS5vcmcCJDRjYzBkMTI2LTI4ZDQtNDU4NS1iOWVhLTE2OTJlNzBiM2Y3MwACDlsxLFsiam91dGlsIl1dAAIsWzIsWyIwZWRiNDIwZi03ZGFiLTQzYWQtYTdkYy05NDBmNzcwZTAyYzMiXV0AAAYgfalWTt82bgSIy2eVsONyBpX3_srxwPuYR3iFPOfZtww
"""

# 拷贝到 $HOME 目录下面，我的windows 的目录是 C:\Users\14271
# 执行 twine upload .\dist\JoUtil-1.4.4-py3-none-any.whl

# PyPI recovery codes
# 81a8baec0ca68ae9
# 989551ea0d8f01c0
# 9b0249c4aeedf415
# ee5ce4447fab224d
# 5abe9efe3a18d69d
# 4a6a9c17667526a6
# 334b903e4380ffe1
# 96f2af64d069c5a0


# token
# pypi-AgEIcHlwaS5vcmcCJDRjYzBkMTI2LTI4ZDQtNDU4NS1iOWVhLTE2OTJlNzBiM2Y3MwACDlsxLFsiam91dGlsIl1dAAIsWzIsWyIwZWRiNDIwZi03ZGFiLTQzYWQtYTdkYy05NDBmNzcwZTAyYzMiXV0AAAYgfalWTt82bgSIy2eVsONyBpX3_srxwPuYR3iFPOfZtww

# ----------------------------------------------------------------------------------------------------------------------
# pip freeze > requirements.txt，环境导出
# pip install -r requirements.txt，环境安装
# ----------------------------------------------------------------------------------------------------------------------

