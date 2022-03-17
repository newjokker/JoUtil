# -*- coding: utf-8  -*-
# -*- author: jokker -*-
import os
from datetime import datetime as dt
import sys
import time


for i in range(100):
    print("-"*50)
    print(dt.now())
    print("-"*50)
    time.sleep(1)
    os.system('clear')