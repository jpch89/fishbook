# -*- coding: utf-8 -*-
# @Author: jpch89
# @Time:   18-8-23 上午11:41


class MyResource:
    # def __enter__(self):
    #     print('连接资源')
    #     return self
    #
    # def __exit__(self, exc_type, exc_value, tb):
    #     print('关闭资源连接')

    def query(self):
        print('查询数据')


# with MyResource() as r:
#     r.query()

from contextlib import contextmanager


@contextmanager
def make_myresource():
    print('连接资源')
    yield MyResource()
    print('关闭资源连接')


# yield 生成器
with make_myresource() as r:
    r.query()
