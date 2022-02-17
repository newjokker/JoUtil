# 说明


* 参考：https://blog.csdn.net/qq_22238021/article/details/80279001

* 五层结构
    * 应用层
    * 运输层
    * 网络层
    * 数据链路层
    * 物理层
   
   
    
* 运输层(transport layer)
    
    * 运输层(transport layer)：负责向两个主机中进程之间的通信提供服务。由于一个主机可同时运行多个进程，因此运输层有复用和分用的功能

    * 复用，就是多个应用层进程可同时使用下面运输层的服务。
    
    * 分用，就是把收到的信息分别交付给上面应用层中相应的进程。运输层主要使用以下两种协议： 

    * **TCP** 传输控制协议TCP(Transmission Control Protocol)：面向连接的，数据传输的单位是报文段，能够提供可靠的交付。 

    * **UDP** 用户数据包协议UDP(User Datagram Protocol)：无连接的，数据传输的单位是用户数据报，不保证提供可靠的交付，只能提供“尽最大努力交付”。

* 应用层(application layer) 

    * 应用层(application layer)：是体系结构中的最高。直接为用户的应用进程（例如电子邮件、文件传输和终端仿真）提供服务。
    
    * 在因特网中的应用层协议很多，如支持万维网应用的HTTP协议，支持电子邮件的SMTP协议，支持文件传送的FTP协议，DNS，POP3，SNMP，Telnet等等。
    
    * **FTP** 
    
    * **DNS**
    
    * **SNMP**
    
    


