# DockerFile

* RUN
    * RUN echo helloword
    * RUN ['func', 'parameter_1', 'parameter_2']
    * &&, joint RUN with && 
    
* COPY 
    * /local/path/file /Image/path/file
    
* ADD
    * ADD file /images/path/file
    * ADD latest.tar /var/www/
    
* EXPOSE 
    * EXPOSE host
    
* CMD
    * use only once
    * CMD ['echo', 'hello docker file']
    
* WORKDIR
    * WORKDIR /path/to/workdir


# ----------------------------------------------------------------------------------------------------------------------

* RUN，dockerfile 最后一行使用 run 程序一直执行下去
    * RUN /v0.0.1/script/allflow_wuhan.py
    
* 
























 