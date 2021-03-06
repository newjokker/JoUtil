# 段子收集

## 问题

* 导入数据太慢了
* 数据结构搜索太慢了，试试使用数据库的方法


-------------

* 使用 OCRUtil 识别图片中的段子
* 编写一个专门的数据结构用于存储段子和操作段子（json，字典结构比较符合我的需求）
    * 增加段子
    * 编辑段子
    * 给段子加标签
    * 对段子进行关键词搜索（使用结巴分词把段子进行分词，作为标签）
    * 对段子进行分类，聚类，段子推送
    * 段子文字转图片，方便发送，
    * 段子文字转图片，接在图片下面，或者写在图片上面。
    * 使用爬虫每天去固定的网站找到喜欢的段子图片或者段子文字，自动进行识别和整理（FML 和 2ch 4ch 死宅网站比较好）
    * 段子要分文件进行存放，不能将所有的段子全部放在一个文件下面
    * 使用 pandas 对段子进行操作 

* 分享
    * 写一个网页，将段子分享在网页里面，能导入导出编辑修改，等等，能找到喜欢的段子
    * 后期使用数据库存储段子，使用数据库的方式对段子进行操作，这样比较方便
    
---------------------------

## 场景

* 通过手机给服务器发一个段子图片，返回给我段子原文，并将原文保存在服务器中等待处理

* 在网页上搜索，编辑段子，不同的账号有不同的等级，管理员的账号是可以登录并修改段子的，其他人只能看

* 可以根据关键词，标签，所包含的文字对段子进行筛选

* 可以将选中的段子进行导出，也可以导入段子，用于后期的编辑

* 段子在网页上友好的展示出来

