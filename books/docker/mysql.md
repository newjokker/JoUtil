
# mysql 镜像使用

### 启动任务

* 指定 root 的密码为 txkj
* 指定 可以远程连接（MYSQL_ROOT_HOST）
* 指定 端口为 11122（默认端口为 3306）
* -v /path/to/init.sql:/docker-entrypoint-initdb.d/init.sql: 将本地的 init.sql 文件挂载到MySQL容器的初始化脚本目录中，使得容器在启动时执行这个SQL文件。

* docker run -d --name my_contain_name -e MYSQL_ROOT_PASSWORD=txkj -p 11122:3306 -e MYSQL_ROOT_HOST=% -v /path/to/init.sql:/docker-entrypoint-initdb.d/init.sql mysql

### 远程连接容器服务

* mysql -u root -P 11122 -h 192.168.3.221 -p

### 在启动时，生成表格，导入数据

* 执行一个 sql 文件

* -v /path/to/init.sql:/docker-entrypoint-initdb.d/init.sql: 将本地的 init.sql 文件挂载到MySQL容器的初始化脚本目录中，使得容器在启动时执行这个SQL文件。

* 执行多个 sql 文件

*  -v /path/to/init2.sql:/docker-entrypoint-initdb.d/init2.sql， 文件的执行顺序是根据字母顺序的，你可以根据文件名的字母顺序来控制执行顺序，例如，init1.sql可能在init2.sql之前执行

```sql

-- 创建数据库
CREATE DATABASE IF NOT EXISTS SaturnDatabaseV2;

-- 切换到新数据库
USE SaturnDatabaseV2;

-- 创建表格
CREATE TABLE IF NOT EXISTS md5_uc (md5 VARCHAR(255) PRIMARY KEY, uc VARCHAR(255) NOT NULL);

-- 插入一些数据
INSERT INTO md5_uc (md5, uc) VALUES ('md5_test', 'Zzz0001');

```
