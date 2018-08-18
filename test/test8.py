# -*- coding: utf-8 -*-
# @Author: jpch89
# @Time:   2018/8/13 21:35

from werkzeug.local import LocalStack

# push 方法, pop 方法, top 属性

s = LocalStack()
s.push(1)

# top取元素，但是不删除
print(s.top)
print(s.top)

# pop弹出栈顶元素
print(s.pop())
print(s.top)

s.push(1)
s.push(2)
# 栈 后进先出
print(s.top)
print(s.top)
print(s.pop())
print(s.top)
