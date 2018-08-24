# -*- coding: utf-8 -*-
# @Author: jpch89
# @Time:   18-8-23 上午11:53

from contextlib import contextmanager


# 如何自动加书名号？
@ contextmanager
def bookmark():
    print('《', end='')
    yield
    print('》')

# 注意 yield 可以不返回任何结果
# 因为 with 后面没有 as
with bookmark():
    print('且将生活一饮而尽', end='')
