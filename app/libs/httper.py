# -*- coding: utf-8 -*-
# @Author: jpch89
# @Time:   2018/8/10 19:44

import requests


class HTTP:
    @staticmethod
    def get(url, return_json=True):
        r = requests.get(url)
        if r.status_code != 200:
            return {} if return_json else ''
        return r.json() if return_json else r.text
