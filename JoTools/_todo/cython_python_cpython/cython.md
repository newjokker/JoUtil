# cython 

* cython, python, cpython 区别

    * cpython 是 python 语言使用 c 语言进行实现，还有 jython ironpython PyPy（胶水语言）
    * python 是解释型编程语言，需要 python 解析是将 python 代码转为机器代码，cython 是编译型程序语言，cython 代码不需要解释器能直接运行？
    * Cython被设计为Python的C扩展。开发人员可以使用Cython加快Python代码执行速度。但是他们仍然可以在不使用Cython的情况下编写和运行Python程序。但是，程序员必须同时安装Python和C编译器，才能运行Cython程序。
    * Cython 源文件的后缀是 .pyx，它是 Python 的一个超集，语法是 Python 语法和 C 语法的混血。
    * 当我们编写完 Cython 代码时，需要先将 Cython 代码翻译成高效的 C 代码，然后再将 C 代码编译成 Python 的扩展模块。
    * Cython 代码翻译成 C 代码，则依赖于相应的编译器，这个编译器本质上就是 Python 的一个第三方模块。它就相当于是一个翻译官，既然用 C 写扩展是一件痛苦的事情，那就拿 Cython 去写，写完了再帮你翻译成 C。
    * Python 和 C 语言大相径庭，为什么要将它们融合在一起呢？答案是：因为这两者并不是对立的，而是互补的。
    * Cython 是一门语言，可以通过 Cython 源代码生成高效的 C 代码，再将 C 代码编译成扩展模块，同样需要 CPython 来进行调用。

### cython 的出现是为什么解决什么问题？
    * 在早期，编写 Python 扩展都是拿 C 去写，但是这对开发者有两个硬性要求：一个是熟悉 C，另一个是要熟悉解释器提供的 C API，这对开发者是一个非常大的挑战。
    * 拿 C 编写代码，开发效率也非常低。
        * Python 是高阶语言、动态、易于学习，并且灵活。但这些优秀的特性是需要付出代价的，因为 Python 的动态性、以及它是解释型语言，导致其运行效率比静态编译型语言慢了好几个数量级。
        * 而 C 语言是最古老的静态编译型语言之一，并且至今也被广泛使用。从时间来算的话，其编译器已有将近半个世纪的历史，在性能上做了足够的优化，因此 C 语言是非常低级、同时又非常强大的。然而不同于 Python 的是，C 语言没有提供保护措施（没有 GC、容易内存泄露），以及使用起来很不方便。


### cython HelloWord

* refer : https://cython.readthedocs.io/en/latest/src/quickstart/build.html

```python
# hello.pyx

def say_hello_to(name):
    print("hello %s", name)
```

```python
# setup.py

from setuptools import setup
from Cython.Build import cythonize

setup(
    name='Hello world app',
    # refer : https://zhuanlan.zhihu.com/p/276461821
    ext_modules=cythonize("hello.pyx"),
    zip_safe=False,
)
```

* python setup.py build_ext --inplace , ignore build-lib and put compiled extensions into the source directory alongside your pure Python modules

```python
# main.py

import hello
say_hello_to("jokker")
```


### cython 现实中的使用例子

* /home/jenkins/BGL-Release/BGL-platform/testdir/modeldata/dxSG/v1.0.2.0/lib/faster_libs

* make 的作用

* 计算 nms 的版本

* setup.py 中具体描述了些啥？其中的链接是什么意思，可以从链接的基础开始讲起

* setup.py 文件的作用，使用的场景
    * 打包为 exe
    * 打包为 whl 文件，python 的包

* 当是在用不了编译的代码的时候，可以使用 python 版本进行替代


### 什么是 setup.py 

* refer : https://blog.csdn.net/asdfgh0077/article/details/103578535

* setup.py是一个python文件，通常告诉您要安装的模块/软件包已与Distutils打包并分发，Distutils是分发Python模块的标准。
* setup.py是Python对多平台安装程序和make文件的回答。 如果您熟悉命令行安装，则将make && make install转换为python setup.py build && python setup.py install 。
* python setup.py develop，此命令将在站点包内创建到源目录的符号链接，而不是复制内容。 因此，它非常快（特别是对于大包装），在系统环境中创建一个软链接指向包实际所在目录
* python setup.py install，通过源码进行安装，与之对应的是通过二进制软件包的安装

### 为什么在 docker 中编译不了

* docker runtime 版本的 cuda 是阉割版本的，只能用于跑不能用于编， nvcc --version 都看不到结果
* 所有都是将需要编译的文件在 devel 版本的 docker 上编译好了，在挪到 runtime 版本的 docker 中进行使用

* 之前 faster rcnn 中，make 的作用

* 不同环境就要重新编译的 so 文件是什么（好像是 swintransform）,里面是什么内容，为什么要这么搞




