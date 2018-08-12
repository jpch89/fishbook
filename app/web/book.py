# -*- coding: utf-8 -*-
# @Author: jpch89
# @Time:   2018/8/11 9:45

from flask import jsonify, request

from app.forms.book import SearchForm
from helper import is_isbn_or_key
from yushu_book import YuShuBook

from . import web

@web.route('/book/search/')
def search():
    """
        q: 普通关键字或者isbn
        page: 页码
        ?q=金庸&page=1
    """

    form = SearchForm(request.args)
    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        if isbn_or_key == 'isbn':
            result = YuShuBook.search_by_isbn(q)
        else:
            result = YuShuBook.search_by_keyword(q)
        return jsonify(result)
    else:
        return jsonify(form.errors)
