
* txkj:v3.5.0
	
	* 修改好 vit 

* txkj:v3.5.2 
	
	* 换为新的接口，一次发一张图 （替换调度代码中的 views.py 文件）
	* build 操作，可以直接 docker run 运行调度代码
	
* txkj:v3.5.4
	
	* 增加了新模型，专门用于检测风筝
	* 风筝缺陷和鸟巢放在一起，同属于一个缺陷（张一辰，他们不关心是什么缺陷，只关心能不能检测出来）
	
# ------ 读取文件夹，生成 log 个 csv -------



* txkj_v0.1
	
	* 修改好 vit
	
* txkj_v0.2.2 rust | broken 

* txkj_v0.2.4 (error)

* txkj_v0.2.5 broken 

* txkj_v0.2.7 rust 

* txkj_v0.3.2 : broken rust 

* txkj_v0.3.4 : broken

* txkj_v0.3.7 ：rust

* txkj_v0.3.7.5 增加 jyhQX

* txkj_v0.3.8.5 增加超时机制，消耗时间超过图片数目 * 9.5 后面的图片就不检测了；增加文件名对应的机制，找到文件名中的关键字才去检测对应的图片

* txkj_v0.3.9.2 增加多进程机制，在一个 GPU 中起多套模型，同时跑（需要优化的是，在解密模型的时候可能会报错，所以模型要错开启动）

* txkj_v0.3.9.4 修改 abs_detection.py 支持多线程，

* txkj_v0.3.11.2 修改未自动生成输出文件夹的 bug

* txkj_v0.4.0.1 开始重头打包模型，控制模型的大小，准备安装 docker

* txkj_v0.4.1.1 ，docker pull pytorch/pytorch:1.5-cuda10.1-cudnn7-runtime

* fangtian_v0.4.1.3，完成全部模型需要的环境，模型还未放进去，[将代码放在docker外面可能会导致代码运行速度非常慢][☆]

* fangtian_v0.4.1.4，模型放到根目录下了，模型 + 环境大小为 12.4G

* fangtian_v0.4.1.6，将 txkj_v0.3.11.2 的 allflow.py 拷贝到下面，解决之前的 bug

* todo 确认新修改的模型中解决了未生成文件夹就报 bug 的问题



---

* txkj_v0.3.7.6 增加并行脚本，在script 里面，需要修改对应的 lib/detelib/yolov5DetectionPtorch.py






