# -*- coding: utf-8 -*-
# @Author: jpch89
# @Time:   18-8-25 上午9:25

from threading import Thread


class MyThread(Thread):
    def __init__(self, name, wid, food):
        super().__init__()
        self.name = name
        self.wid = wid
        self.food = food

    def run(self):
        print(f'我的名字叫做{self.name}')
        print(f'我的工号是{self.wid}')
        print(f'我吃{self.food}')


my_thr = MyThread('黑猩猩', 1, '香蕉')
my_thr.start()
