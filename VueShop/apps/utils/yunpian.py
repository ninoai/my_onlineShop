# -*- coding:utf-8 -*-
import json

__author__ = 'catherine'
__date__ = '2019/3/31 10:16 AM'
import requests

class YunPian(object):

    def __init__(self, api_key):
        self.api_key = api_key
        self.single_send_url = ''

    def send_sms(self, code ,mobile):
        params = {
            'apikey':self.api_key,
            'mobile':mobile,
            'text': ''
        }
        response = requests.post(self.single_send_url, data=params)
        re_dict = json.loads(response.text)
        print(re_dict)

if __name__ == "__main__":
    yun_pian = YunPian("api_key")
    yun_pian.send_sms("2017","17615876172")