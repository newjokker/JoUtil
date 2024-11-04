# 说明

### 能引用包的几个关键点

* 设置环境
* 函数文件的 package 关键字
* import 
* 函数名

#### 设置环境

* 运行 go env
* 查看  GOROOT 和 GOPATH 信息
* 需要引用的包必须在这两个文件夹，或者他们的子文件夹下面，我一般放在 GOPATH 下面
  * GOPATH 的修改 refer : https://studygolang.com/articles/17598

* 我自己的解决方案
  * 包的名字叫做 jogo 放在 GOPATH 目录下的 src 文件夹

#### package 关键字

* 当准备使用下述方式调用函数的时候，需要指定 包含 Test1() 函数的 *.go 文件第一行 package function 
  * import "jogo"
  * function.Test1()

#### import

* import 的是文件夹的名字
* A.B 中 A 是 package A 中 A 的名字 B 是函数的名字

#### 函数名

* 函数名的首字母要是大写，否则无法运行
