# python 调用 go 注意点

### 注意点

* go 中要 import "C"

![](../data/import_C.png)

* go 函数中，加入 export 语句

![](../data/export_语句.png)

### go 函数需要传入字符串

* go 中接受字符创使用 *C.char 代替 string

* go 中接受到 string 之后使用前需要先进行转换，C.GoString(analysis_dir)

* python 调用时候转为二进制，在字符串之前加入 b

### go 函数传出字符串

* 定义函数时输出为 (*C.char)

* 函数转为 C 格式的 return C.CString("hello word")

![](../data/返回str类型.png)

* python 调用的时候需要定义返回类型，fib.restype = ctypes.c_char_p

![](../data/指定返回类型.png)

### 编译

go build -buildmode=c-shared -o _py_go.so py_go.go

### 调用

![](../data/python调用go.png)







