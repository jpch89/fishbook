# -*- coding: utf-8 -*-
# @Author: jpch89
# @Email:  jpch89@outlook.com
# @Time:   2018/8/10 11:30

from flask import Flask
# from config import DEBUG

app = Flask(__name__)
app.config.from_object('config')
print(app.config['DEBUG'])

@app.route('/hello/')
def hello():
    return "Hello, World!"

# app.add_url_rule('/hello/', view_func=hello)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81, debug=app.config['DEBUG'])
