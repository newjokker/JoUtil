
# 按照 cookbook 中的内容进行编写

from distutils.core import setup, Extension

modules = Extension(
'deteXml',
["src/deteXml.c", "src/str_tools/charTools.c"],
include_dirs=["src/str_tools"],
#extra_compile_args = ["-lrt"],
)

setup(
    name='JTool_c',
    ext_modules=[modules])


