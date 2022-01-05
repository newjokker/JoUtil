#from setuptools import setup, find_packages, Extension
from distutils.core import setup, Extension




modules = Extension(
'jo_test',
["src/jo_test.c"],
include_dirs=[],
#extra_compile_args = ["-lrt"],
)

setup(
    name='JTool_c',
    ext_modules=[modules])


