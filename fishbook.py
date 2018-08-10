# -*- coding: utf-8 -*-
# @Author: jpch89
# @Time:   2018/8/10 11:30

from flask import Flask
# from flask import make_response

app = Flask(__name__)
app.config.from_object('config')
print(app.config['DEBUG'])

@app.route('/hello/')
def hello():
    headers = {
        'content-type': 'text/plain',
        'location': 'http://www.bing.com'
    }
    # response = make_response('<html></html>', 404)
    # response.headers = headers
    return '<html></html>', 301, headers

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81, debug=app.config['DEBUG'])
