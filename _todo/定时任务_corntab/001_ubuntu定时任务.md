

# 参考文献：https://blog.csdn.net/katyusha1/article/details/78619549

# 参考：https://cloud.tencent.com/developer/article/1690718

# 

* * * * * command
分 时 天 月 周 命令

ps -ef | grep cron : 是否有定时任务在运行

sudo service cron start

sudo crontab -e : 编辑

sudo service cron restart : 重启 cron

#### demo

* check if cron running 
ps -ef | grep cron
see the following line 
root       740     1  0 5月05 ?       00:00:00 /usr/sbin/cron -f

* check config file 
vim /etc/crontab

* add line
5  * * * *      root    /bin/bash  /home/ldq/mysql_backup/db_cover.sh







