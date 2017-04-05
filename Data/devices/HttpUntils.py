# -*- coding: utf-8 -*-
import codecs
import time
import urllib2,urllib
import requests
from selenium import webdriver
import os
import datetime
from Data.devices import fs_datadevices
import json
import httplib
import logging
class HttpUntils:
    def __init__(self,url,data,headers,cookies):
        self.url = url
        self.data = data
        self.herders = headers
        self.cookies = cookies
        logging.basicConfig(level=logging.INFO,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename='myapp.log',
                filemode='w')
        #################################################################################################
        #定义一个StreamHandler，将INFO级别或更高的日志信息打印到标准错误，并将其添加到当前的日志处理对象#
        console = logging.StreamHandler()
        console.setLevel(logging.INFO)
        formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
        console.setFormatter(formatter)
        logging.getLogger('').addHandler(console)
        #################################################################################################

    def Get(self):
        get_data = urllib.urlencode(self.data)
        try:
           r = requests.get(self.url+get_data,verify=False)
           if r.status_code == 200:
               return r
           elif r.status_code in [502,504]:
               logging.warning('Gateway Time-out')
           else:
               logging.warning('sever is error')

        except requests.ConnectionError,e:
            print e

    def Post(self):
        if 'x-www-form-urlencoded' in self.herders.get('Content-Type'):
            Post_data = urllib.urlencode(self.data)
        elif 'json' in self.herders.get('Content-Type'):
            Post_data = json.dumps(self.data)
        else:
            Post_data = self.data
        try:
           r = requests.post(self.url,data=Post_data,headers=self.herders,verify=False)
           if r.status_code == 200:
               return r
           elif r.status_code in [502,504]:
               logging.warning('Gateway Time-out')
           else:
               logging.warning('sever is error')

        except requests.ConnectionError,e:
            print e


    def Post_cookies(self):
        if 'x-www-form-urlencoded' in self.herders.get('Content-Type'):
            Post_data = urllib.urlencode(self.data)
        elif 'json' in self.herders.get('Content-Type'):
            Post_data = json.dumps(self.data)
        else:
            Post_data = self.data
        try:
           r = requests.post(self.url,data=Post_data,headers=self.herders,cookies=self.cookies,verify=False)
           if r.status_code == 200:
               return r
           elif r.status_code in [502,504]:
               logging.warning('Gateway Time-out')
           else:
               logging.warning('sever is error')

        except requests.ConnectionError,e:
            print e



















