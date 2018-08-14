# -*- coding: utf-8 -*-
# @Author: jpch89
# @Time:   2018/8/11 8:51

from app.libs.httper import HTTP
from flask import current_app

class YuShuBook:
    isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    keyword_url = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={}'

    @classmethod
    def search_by_isbn(cls, isbn):
        url = cls.isbn_url.format(isbn)
        # url = self.isbn_url.format(isbn) # 链式查找
        result = HTTP.get(url)
        # json 在 Python 中会转换成字典
        return result

    @classmethod
    def search_by_keyword(cls, keyword, page=1):
        url = cls.keyword_url.format(keyword, current_app.config['PER_PAGE'], cls.calculate_start(page))
        result = HTTP.get(url)
        return result

    @staticmethod
    def calculate_start(page):
        return (page - 1) * current_app.config['PER_PAGE']
