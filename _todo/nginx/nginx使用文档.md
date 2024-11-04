# nginx 说明文档


### 安装

* 直接 apt 安装即可
    * apt update
    * apt install iginx

### 设置

* 简单的负载均衡和转发只需要修改一个文件即可 /etc/nginx/nginx.conf

```shell
# 设置负载均衡
upstream backserver {
    # 默认轮询负载均衡策略
    # ip-hash 负载均衡策略
    # ip_hash;   
    # 最少连接数负载均衡策略
    # least_conn
    # 加权负载均衡，设置 weight 权重值
    server 192.168.3.221:5001 weight=1;
    server 192.168.3.221:1237 weight=1;
    server 192.168.3.221:1236 weight=1;
    server 192.168.3.221:1235 weight=1;
    server 192.168.3.221:1234 weight=1;
    }   

server {
    listen       8090;
    server_name  localhost;
    
    # body 最大为 30M 超过会报错 
    client_max_body_size 30m;
    
    # 转发的地址，此处的 backserver 和上面的 upstream backserver 想对应
    location / { 
        proxy_pass http://backserver;
    }   

    error_page   500 502 503 504  /50x.html;
    }   

}   
```

### 重启 nginx
    
* 搞定设置之后，运行 service nginx restart 重启 nginx

### 遇到的问题

* 启动负载均衡之后提升没那么大，其一个模型和三个模型，使用三个客户端去测试也就相差 10% 是不是我测试的方法有问题还是 nginx 我配置的有问题

* 我测试了不是因为转发的数据比较大导致的转发消耗时间（只开一个进程一个直接和 docker 进行交互，一个使用 nginx 代理和 docker 进行交互）



