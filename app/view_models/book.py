# -*- coding: utf-8 -*-
# @Author: jpch89
# @Time:   2018/8/14 22:44

class BookViewModel:
    def package_single(self, data, keyword):
        returned = {
            'books': [],
            'total': 0,
            'keyword': keyword
        }
        if data:
            returned['total'] = 1

    def package_collection(self, data, keyword):
        pass

    def __cut_book_data(self, data):
        book = {
            'title': data['title'],

        }