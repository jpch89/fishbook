# -*- coding: utf-8 -*-
# @Author: jpch89
# @Time:   2018/8/13 21:07

import threading
import time
from werkzeug.local import Local

my_obj = Local()
my_obj.b = 1

def worker():
    # 新线程
    my_obj.b = 2
    print('在新线程中b是' + str(my_obj.b))

new_t = threading.Thread(target=worker, name='新线程')
new_t.start()
time.sleep(1)
# 主线程
print('在主线程中b是' + str(my_obj.b))
