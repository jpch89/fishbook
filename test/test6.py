# -*- coding: utf-8 -*-
# @Author: jpch89
# @Time:   2018/8/13 21:45
import threading
import time

from werkzeug.local import LocalStack

my_stack = LocalStack()
my_stack.push(1)
print('主线程入栈后，值为：', my_stack.top)

def worker():
    # 新线程
    print('在新线程入栈前，值为：', my_stack.top)
    my_stack.push(2)
    print('在新线程入栈后，值为：', my_stack.top)

new_t = threading.Thread(target=worker, name='新线程')
new_t.start()
time.sleep(1)

# 主线程
print('最终，主线程值为：', my_stack.top)
