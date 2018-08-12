# -*- coding: utf-8 -*-
# @Author: jpch89
# @Time:   2018/8/11 8:51

from httper import HTTP

class YuShuBook:
    per_page = 15
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
    def search_by_keyword(cls, keyword, page):
        url = cls.keyword_url.format(keyword, cls.per_page, (page-1)*cls.per_page)
        result = HTTP.get(url)
        return result
