# -*- coding: utf-8 -*-
# @Author: jpch89
# @Time:   2018/8/13 14:28

import threading

def worker():
    print('我是线程')
    t = threading.current_thread()
    print(t.getName())

print('我是主线程')
t = threading.current_thread()
print(t.getName())

new_t = threading.Thread(target=worker, name='子线程1')
new_t.start()
