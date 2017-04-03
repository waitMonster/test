# -*- coding: utf-8 -*-
import codecs
import time
import urllib2,urllib
import requests
from requests.cookies import RequestsCookieJar
from selenium import webdriver
import os
import datetime
from Data.devices import fs_datadevices,HttpUntils
import json,unittest,Login

class PC_LoginOff:
    def __init__(self,loginoff_url,token,cookies):
        self.loginoff_url = loginoff_url
        self.token = token
        self.cookies = cookies

    def loginoff(self):
        off_headers = {'Accept':'application/json, text/javascript, */*; q=0.01',
                            'Cache-Control':'no-cache',
                            'Accept-Encoding':'gzip, deflate, br',
                            'Accept-Language':'zh-CN,zh;q=0.8',
                            'Connection':'keep-alive',
                            'Content-Type':'application/json'}
        try:
            for i in range(self.token):
                off_params = {}
                off_params['traceId'] = str('E-E.fktest.183-32797485')
                off_params['_fs_token'] = str(self.token[i])
                http = HttpUntils.HttpUntils(self.loginoff_url,off_params,off_headers,self.cookies)
                result = http.Post().json()
                if result.get('Result').get('StatusCode') == 0:
                    return 0
                else:
                    print result.get('Result').get('FailureMessage')
        except Exception,e:
            print e





