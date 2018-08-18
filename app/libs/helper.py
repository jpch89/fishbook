# -*- coding: utf-8 -*-
# @Author: jpch89
# @Time:   2018/8/10 17:59

def is_isbn_or_key(word):
   """判断查询的是isbn还是关键字。
   """
   isbn_or_key = 'key'
   if len(word) == 13 and word.isdigit():
      isbn_or_key = 'isbn'
   short_word = word.replace('-', '')
   if '-' in word and len(short_word) == 10 and short_word.isdigit():
      isbn_or_key = 'isbn'
   return isbn_or_key
