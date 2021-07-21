# C 语言扩展


* 要使用 Ctypes 模块来访问 C 语言编写的程序，首先要确保 C 代码已经被编译为与 Python 解释器相兼容（即，采用相同的体系结构，字长，编译器等）的共享库了

* 编译
    * gcc -o test.dll -shared test.c , windows
    * gcc -o test.so -shared test.c , Linux
    * g++ -o test_001.so  -shared c++_python3.cpp -fPIC , C++ Linux

* 要是编译的文件有点多可以写一个 makefile 文件进行编译

* 调用

`    import ctypes
    # 使用ctypes很简单，直接import进来，然后使用ctypes.CDLL这个类来加载动态链接库
    # 如果在Windows上还可以使用ctypes.WinDLL。
    # 因为看ctypes源码的话，会发现WinDLL也是一个类并且继承自CDLL
    # 所以在linux上使用ctypes.CDLL，
    # 而在Windows上既可以使用WinDLL、也可以使用CDLL加载动态链接库
    lib = ctypes.CDLL("./mmp.dll")  # 加载之后就得到了动态链接库对象
    # 我们可以直接通过.的方式去调用里面的函数了，会发现成功打印
    lib.test()  # hello world
`





 