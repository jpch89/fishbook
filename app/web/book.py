# -*- coding: utf-8 -*-
# @Author: jpch89
# @Time:   2018/8/11 9:45

from flask import jsonify, request, render_template, flash

from app.forms.book import SearchForm
from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook
from app.view_models.book import BookViewModel, BookCollection

from . import web
import json


@web.route('/test1/')
def test1():
    from flask import request
    from app.libs.none_local import n
    print(n.v)
    n.v = 2
    print('-' * 30)
    print(getattr(request, 'v', None))
    setattr(request, 'v', 2)
    print('-' * 30)
    return ''


@web.route('/book/search')
def search():
    """
        q: 普通关键字或者isbn
        page: 页码
        ?q=金庸&page=1
    """

    form = SearchForm(request.args)
    books = BookCollection()

    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        yushu_book = YuShuBook()

        if isbn_or_key == 'isbn':
            yushu_book.search_by_isbn(q)
        else:
            yushu_book.search_by_keyword(q, page)

        books.fill(yushu_book, q)
        return json.dumps(books, default=lambda o: o.__dict__)

    else:
        return jsonify(form.errors)


@web.route('/test/')
def test():
    r = {
        'name': '',
        'age': 18
    }
    r1 = {
        'name': '王大锤',
        'age': 17
    }
    flash('消息闪现第一次', category='error')
    flash('消息闪现第二次', category='warning')
    return render_template('test.html', data=r, data1=r1)

@web.route('/test2/')
def test2():
    r = {
        'name': '张三',
        'age': 18
    }
    return render_template('test2.html', data=r)
