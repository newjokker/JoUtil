
# 基于 Python 的 eagle 二次开发 


### 安装环境

#### Anaconda
* 官网下载，免费的
* 创建一个新的环境 conda create -n eagle python=3.5.6
* 查看环境 conda indo -e
* 切换环境 conda activate eagle

#### pycharm
* 官网下载，社区版，community 免费
* 自定义安装，设置项目的解释器 project interpreter 选着 eagle

### eagle 文件夹布局

* backup
    * backup-2020-08-05 17.07.01.883.json                                           # 用于恢复的文件
    
* images
    * KDH5EVWARA22B.info
    * 检修公司-500kV邹新线 #164右地线挂点歪斜-20190705.jpg                            # 源文件
    * 检修公司-500kV邹新线 #164右地线挂点歪斜-20190705_thumbnail.png                  # 缩略图
    * metadata.json                                                                  # 图像描述文件
    
* metadata.json                                                                      # 文件夹描述文件
* mtime.json                                                                         # 修改时间记录文件
* tags.json                                                                          # 标签记录文件

### 修改的原理

* eagle 软件初始化时，信息是存在 json 文件中的

* 我们只需要修改 json 文件，就能在 eagle 中给图片增加对应的信息，标签|所属文件夹|注释|矩形标注|缩略图

### 注意点

* id 的生成
    * 13 位 数字 + 字母
* 修改时间的生成
    * int(time.time() * 1000)
* 描述文件中每个参数的意义，矩形位置标签|标签|注释|最后修改时间


### 目前已完成的操作

* 对武汉规范的数据集，初始化为 eagle 项目
    * 获取图像 md5
    * 获取图像标签
    * xml 合并
    * xml --> json，tag|位置矩阵标签|标签|
    * 其他相应文件，修改描述文件，文件夹描述文件
    
* eagle 项目转为可以测试的数据集
    * 遍历 image 文件夹中的每一个图片数据
    * json --> xml
    * 将生成的 xml 和 json 按照一定的规范进行存放

### 进行自定义开发

#### 对任意规范的数据集初始化为 eagle 项目
* 晚上各个样式的数据集中 xml 和 img 的相对位置关系

#### 在不同的项目中也能唯一确定图像 id，
* 随机数 + 时间

#### 设置自定义规则进行文件夹划分，符合规定的文件放到一个文件夹中
* 找到指定的图像，修改配置文件中的文件夹选项
* 文件夹描述文件增加新增文件夹
* 如果不能直接更新需要强制 eagle 读取配置文件进行更新

#### 主动分析图像的颜色，不用手动使用 eagle 进行分析
* 推测 eagle 分析图像主要颜色的方法

#### 寻找数据库中是否存在某一个图像
* 将图像的 md5 值作为图像的注释，获取图像的 md5 值后，直接注释中搜索 md5 即可


## todo
* 最好能制作成视频，这样方便观看

---

### 操作实例

#### 平台检测结果 to eagle

* 将待检图片放到文件夹中，导入到平台进行检测
* 对平台检测结果人工进行修改
* 下载 xml
    * 切换到检测结果页面，点击 F12, 同时按住 ctrl + shift + R 
    * 点击出现的界面中的 queryABatchById 文件，找到 id 值
    * 后面的 url 补充 id，输入服务器自动下载 xml，http://192.168.3.109:8090/detection/test-result-img/builderXml?id=
    * 将下载的 url 和 图片放到一个文件夹中
* 修改代码中的图片文件夹地址和保存地址

    ```python
    eagle_library = r"C:\Users\14271\Desktop\del\test_fzc.library"
    imgDir = r"C:\Users\14271\Desktop\test_data\img"
    a = EagleOperate(eagle_library, imgDir)
    a.init_edgal_project(imgDir)   
    ```





 

























