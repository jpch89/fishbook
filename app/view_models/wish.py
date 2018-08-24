# -*- coding: utf-8 -*-
# @Author: jpch89
# @Time:   18-8-24 上午11:26

# from collections import namedtuple

from app.view_models.book import BookViewModel

# MyGift = namedtuple('MyGift', ['id', 'book', 'wishes_count'])


class MyWishes:
    def __init__(self, wishes_of_mine, gift_count_list):
        self.wishes = []
        self.__wishes_of_mine = wishes_of_mine
        self.__gift_count_list = gift_count_list
        self.wishes = self.__parse()

    def __parse(self):
        temp_wishes = []
        for wish in self.__wishes_of_mine:
            my_wish = self.__matching(wish)
            temp_wishes.append(my_wish)
        return temp_wishes

    def __matching(self, wish):
        count = 0
        for gift_count in self.__gift_count_list:
            if wish.isbn == gift_count['isbn']:
                count = gift_count['count']

        r = {
            'gifts_count': count,
            'book': BookViewModel(wish.book),
            'id': wish.id
        }

        return r
        # my_gift = MyGift(gift.id, BookViewModel(gift.book), count)
        # return my_gift
