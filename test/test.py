# -*- coding: utf-8 -*-
# @Author: jpch89
# @Time:   2018/8/12 20:58

from flask import Flask, current_app

app = Flask(__name__)

# ctx = app.app_context()
# ctx.push()
# a = current_app
# d = current_app.config['DEBUG']
# ctx.pop()

with app.app_context():
    a = current_app
    d = current_app.config['DEBUG']
