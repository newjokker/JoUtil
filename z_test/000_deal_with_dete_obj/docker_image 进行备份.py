# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import subprocess

with open("save_docker.sh", "w") as txt_file:

    res = subprocess.Popen("docker image list", shell=True, stdout=subprocess.PIPE)
    res.stdout.readline()
    gpu_uuid_list = []
    for line in res.stdout.readlines():
        # gpu_uuid_list.append(line.strip(b'\n').decode('utf-8'))
        each_line = line.strip(b'\n').decode('utf-8')

        a = list(filter(lambda x:x!="", each_line.split(" ")))
        name = a[0]
        # fixme 不知道怎么把斜杠改为下划线
        name.replace("\/", "_")
        name.replace("//", "_")
        name.replace("\\", "_")
        name.replace("\/", "_")

        print(f"docker save -o {name}_{a[1]}.tar {a[0]}:{a[1]}")
        txt_file.write(f"docker save -o {name}_{a[1]}.tar {a[0]}:{a[1]}\n")


# 生成 sh 文件之后 执行这个 sh 文件即可