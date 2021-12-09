# awk


# todo 编写可执行文件，放到环境变量中去，然后自定义关键字如 jo -devide img_dir   


* refer : https://www.runoob.com/linux/linux-comm-awk.html

* awk '{print $1,$4}' log.txt, 每行按空格或TAB分割，输出文本中的1、4项

* awk -F, '{print $1,$2}'   log.txt, 使用","分割

* awk -va=1 '{print $1,$1+a}' log.txt, 设置变量

* awk -f {awk脚本} {文件名}， 运行 awk 脚本

* 