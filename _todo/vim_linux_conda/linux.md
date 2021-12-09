# linux

* 学习 ： https://www.runoob.com/linux/linux-command-manual.html



* man : 查询命令的使用

* alias 
* unalias

* history

* ls -l | wc -l 









# ---












* cp -r /home/fbc/serv/old_nc_serv/models  /home/ldq/nc_serv ，拷贝文件夹
* cp  /home/fbc/serv/old_nc_serv/models  /home/ldq/nc_serv，拷贝文件
* scp -r ldq@192.168.3.202:/home/ldq/a.py   /home/ldq  拷贝远程文件夹
* su ldq， 切换用户到 ldq
* touch a.py 新建文件
* mkdir new_folder 新建文件夹
* rm a.py 删除文件
* rm -r new_floder 删除文件夹
* chmod file_path 777，更改文件权限
* chmod  777 ./ -R , 递归修改每一个文件的权限
* du -sh 查看文件总和大小

* find  -name “*.so” | xargs rm -f ，删除目录下制定格式的文件
* find -name "*.jpg" | xargs cp -t /home/ldq/ 复制选中文件到指定目录 ：https://blog.csdn.net/qq_42321328/article/details/83019685

* 文件太多难以删除：ls | xargs -n 10 rm -fr ls
----------------------------------- 调试模型常用 --------------------------------------------
* nvidia-smi , 查询 GPU 状态
* ps -ef 所有进程，连带命令行
* ps -ef | grep pid 根据 pid 对进程进行删选
* kill -9 pid , 彻底杀死进程 pid
* python3 main_manage.py > need_log.txt，将打印内容重定向，输出到文件
* lsof -i :8083，（list open files）查询端口的 ID，然后使用 kill 杀掉对应进程就能解决端口占用
* conda info -e 找到 python 环境的地址
* find 文件夹路径 -name "python3.5m" 在指定的python 环境地址下面，找到 python3.5m python环境指定的文件，用于编译 .so 文件
----------------------------------------------------------------------------------------------
命令行快捷键

* ctrl + a , 移动到命令行的开头
* ctrl + e , 移动到命令行结尾

* ctrl + l , 清屏
* ctrl + r , 历史命令查询 
 
* ctrl + u，删除当前光标前面的文字
* ctrl + k，删除当前光标后面的文字

----------------------------------------------------------------------------------------------
* find /home/ldq  -name "a.py" ， 递归查找指定目录下符合名字规范的文件
----------------------------------------------------------------------------------------------
* ls -l|grep "^-"| wc -l ， 查看文件夹中文件的个数，“^-” 是以 - 开头的意思，不加 ^， “-”  是 存在 - 的意思
* ls -l|grep "^d"| wc -l ，查看文件夹中文件夹的个数
* ls -lR|grep "^-" 
----------------------------------------------------------------------------------------------
* find 和 cp 共用
* （1）find -name "*.py" | xargs cp -t ./new/     ,  
* （2）cp $(find -name "*.py") ./new/                ,  
* （3）find -name "*.py" | xargs -i cp {} ./new/  , xargs 有一个参数 -i 可以把捕获的结果放入{}中
----------------------------------------------------------------------------------------------

* grep image *.py，查找 py 文件中存在字符串 image 的行