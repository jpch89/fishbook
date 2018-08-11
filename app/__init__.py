# -*- coding: utf-8 -*-
# @Author: jpch89
# @Time:   2018/8/11 11:40

from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config.from_object('config')
    register_blueprint(app)
    return app


def register_blueprint(app):
    from app.web.book import web
    app.register_blueprint(web)