# -*- coding: utf-8 -*-#
import requests
import json
 
class airoot(object):
    def __init__(self):
        self.url = r'http://api.qingyunke.com/api.php'
        self.data = {
            'key':'free',
            'appid':0,
            'msg':''
        }
 
 
    def getword(self, word=''):
        self.data['msg'] = word
        if self.data['msg'] == '':
            self.data['msg'] = '你好'
        self.res = requests.get(self.url, self.data)
        self.res.encoding = 'utf8'
        self.res = self.res.json()
 
        print(self.res)
        return self.res