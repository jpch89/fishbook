# -*- coding: utf-8 -*-
# @Author: jpch89
# @Time:   2018/8/11 11:39

from flask import Blueprint

web = Blueprint('web', __name__)

from app.web import book
from app.web import auth
from app.web import drift
from app.web import gift
from app.web import main
from app.web import wish
