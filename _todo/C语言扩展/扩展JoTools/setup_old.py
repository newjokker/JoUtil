# 韦亦贵写的版本，需要指定 python 的文件夹和名字

from setuptools import setup, find_packages, Extension

module = Extension(
    # name 模块的名字，要求是 模块的名字等于 .so 的名字 等于代码里面的名字
    name = "deteXml", 

    # C 的代码
    sources = [
        "src/deteXml.c", 
        "src/str_tools/charTools.c"
        ],

     # 头文件所在的目录 
    include_dirs=[
        "src/str_tools",
    ],

    # 编译
    extra_compile_args= [
        "-O3",
    ],

    # 链接
    extra_link_args = [
        "-O3",                             # 按照最高级别进行优化
        #"-lpython3.8"
        "-L/root/anaconda3/envs/py36/lib",   # 指定链接的目录 
        "-lpython3.6m"				# 指定链接的文件 libpython3.7m.so --> python3.7m 去掉lib和.so
    ],
    )


if __name__ == "__main__":
    
    setup(
        name = "JTool_c",
        version = "1.0",
        description = "this is JTool lib by using C/C++",
        ext_modules = [module]
    )
