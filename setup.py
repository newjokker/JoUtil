# -*- coding: utf-8  -*-
# -*- author: jokker -*-

"""
* pip install opencv-python : 安装 cv2
* conda install shapely : 安装 shapely, pip 安装比较容易报错
"""



from setuptools import setup, find_packages

setup(

    name='JoUtil',                                                                          # 打包起来的包的文件名
    version='1.0.1',                                                                        # 版本
    description='a tools for TXKJ algo',                                                    # 描述
    author='jokker',                                                                        # 作者
    author_email='18761609908@163.com',                                                     # 邮箱
    url='https://github.com/newjokker/JoUtil.git',
    requires=['numpy', 'pillow', 'pandas', 'easydict', 'matplotlib', 'imagehash', 'prettytable', 'progress',
              'progressbar', 'requests', 'imageio', 'pyexiv2', 'cv2', 'exifread', 'whatimage', 'pyheif',
              'pymysql', 'pytesseract', 'beautifulsoup4', 'Crypto', 'flask'
              ],          # 定义依赖哪些模块

    # 打包的python文件夹
    packages=['JoTools', 'JoTools/utils', 'JoTools/txkj', 'JoTools/for_csdn', 'JoTools/txkjRes',
              'JoTools/for_csdn/word_pic', 'JoTools/for_csdn/find_same_img', 'JoTools/for_csdn/the_art_of_war',
              ],
    # packages=find_packages('JoTools'),          # 包含所有 JoTools 中的包
    package_data={
        'JoTools/for_csdn/word_pic': ['data/*.pkl'],
        'JoTools/for_csdn/the_art_of_war': ['data/*.txt'],
    },
    long_description="""
    * jokker 常用的功能组成的包
    """,
    )


# 打包的命令
# 切换到 setup.py 文件所在文件夹
# python setup.py bdist_wheel

# 注意
# 需要将用到的包全部写到 packages 参数后
# 需要在 setup.py 同级目录创建一个 test.py 文件用于测试
# requires 不能出现 *-* 格式的写法 如 scikit-image，否则会报错

# setuptools 的进一步学习参考：https://www.jianshu.com/p/ea9973091fdf

# 发布到 pypi 上去，refer : https://www.justdopython.com/2020/05/13/Python-pip/
# python -m twine upload --repository pypi dist/*
# 或者
# python -m twine upload --repository pypi dist/JoUtil-0.2.21-py3-none-any.whl
# 账号：jokker
# 密码：*u@%Uu.#PU8ty,w


