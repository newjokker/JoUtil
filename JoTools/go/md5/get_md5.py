# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import time
from JoTools.utils.HashlibUtil import HashLibUtil

start = time.time()
md5_str = HashLibUtil.get_str_md5(r"/home/ldq/golang/img/87285e857438e3c3540477118ec09d1f.jpg")
print(md5_str, time.time() - start)

