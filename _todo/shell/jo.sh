#PATH="$PATH:/home/zhengb66/bin"
#export PATH

# todo 对参数进行自动补全
# todo 维护好 --help

shell_str=""

for i in $@
do
if [ "$i" != "$1" ];then
shell_str="$shell_str $i"
fi
done

cmd_str="python3 ./data/$1.py $shell_str"
echo "--------------"
#echo $cmd_str
#echo $shell_str
$cmd_str