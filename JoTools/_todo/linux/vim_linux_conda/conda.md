# conda 

* conda create -n tc --clone /home/fbc/.conda/envs/tc                   拷贝一个环境

* conda create -n jokker python=3.6                                     创建环境

* conda create -n ldq --clone jokker                                    复制安装环境

* conda info --envs                                                     查看安装的环境

* conda activate assign_envs                                            切换到指定的环境

* conda remove --name your_env_name --all                               删除虚拟环境

* conda remove --name your_env_name package_name                        删除已有的包

