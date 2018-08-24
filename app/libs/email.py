# -*- coding: utf-8 -*-
# @Author: jpch89
# @Time:   18-8-24 下午8:31

from app import mail
from flask_mail import Message

def send_mail():
    msg = Message('测试邮件', sender='test@163.com', body='这是测试邮件。',
                  recipients=['test@qq.com'])
    mail.send(msg)
