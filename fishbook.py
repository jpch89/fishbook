# -*- coding: utf-8 -*-
# @Author: jpch89
# @Time:   2018/8/10 11:30

from flask import Flask
from helper import is_isbn_or_key

app = Flask(__name__)
app.config.from_object('config')
print(app.config['DEBUG'])

@app.route('/book/search/<q>/<page>')
def search(q, page):
    """
        q: 普通关键字或者isbn
        page: 页码
    """
    isbn_or_key = is_isbn_or_key(q)
    pass

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81, debug=app.config['DEBUG'])
