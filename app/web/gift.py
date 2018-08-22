# -*- coding: utf-8 -*-
# @Author: jpch89
# @Time:   2018/8/22 10:50

from . import web



@web.route('/my/gifts')
def my_gifts():
    pass


@web.route('/gifts/book/<isbn>')
def save_to_gifts(isbn):
    pass


@web.route('/gifts/<gid>/redraw')
def redraw_from_gifts(gid):
    pass
