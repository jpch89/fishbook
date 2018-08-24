# -*- coding: utf-8 -*-
# @Author: jpch89
# @Time:   18-8-24 下午5:09


class A:
    # def go(self):
    #     return object()
    def __call__(self):
        return object()


class B:
    def run(self):
        return object()


def func():
    return object()


def main(call_able):
    call_able()
    # 想在 main 中调用传入的参数
    # 得到对象 object
    # 不用区分到底是A.go()
    # 还是B.run()
    # 还是函数func()
    # 直接调用即可
    # __call__ 实现了统一调用接口


main(A)
