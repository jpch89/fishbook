# -*- coding: utf-8 -*-
# @Author: jpch89
# @Time:   2018/8/22 10:50

from flask_login import login_required

from . import web



@web.route('/my/gifts')
@login_required
def my_gifts():

    return 'My Gifts'


@web.route('/gifts/book/<isbn>')
def save_to_gifts(isbn):
    pass


@web.route('/gifts/<gid>/redraw')
def redraw_from_gifts(gid):
    pass
