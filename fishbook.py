# -*- coding: utf-8 -*-
# @Author: jpch89
# @Time:   2018/8/10 11:30

from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81, debug=app.config['DEBUG'])
