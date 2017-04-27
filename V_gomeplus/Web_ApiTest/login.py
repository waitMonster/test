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
import json,unittest

class login:
    def __init__(self):
        self.xls_name = 'V_gomeplus.xlsx'
        self.V = fs_datadevices.fs_datadevice(self.xls_name)
        self.login_url = self.V.Rxls_URL().get('Web_gmsst5Login')
        self.dict_params = self.V.Rxls_Data()
        self.cookies = RequestsCookieJar()


    def login(self):
        login_headers = {'Accept':'application/json, text/javascript, */*; q=0.01',
                         'Content-Type':'application/x-www-form-urlencoded'}

        for i in range(len(self.dict_params.get('gomeOrCoo8'))):
            login_params = {}
            login_params['loginName'] = str(self.dict_params.get('loginName')[i])
            login_params['gomeOrCoo8'] = str(self.dict_params.get('gomeOrCoo8')[i])
            login_params['password'] = str(self.dict_params.get('password')[i])
            login_params['chkRememberUsername'] = str(self.dict_params.get('chkRememberUsername')[i])
            login_params['captchaType'] = str(self.dict_params.get('captchaType')[i])
            login_params['agreeFlag'] = str(self.dict_params.get('agreeFlag')[i])
            login_params['captcha'] = eval(str(self.dict_params.get('captcha')).replace(' ',''))[i]
            login_params['code'] = str(self.dict_params.get('code')[i])
            http = HttpUntils.HttpUntils(self.login_url,login_params,login_headers,self.cookies)
            result = http.Post()
            print '第'+str(i+1)+'次登录请求返回结果为：'+str(result.content)
            print '第'+str(i+1)+'次登录请求获得的cookie为：'+str(result.cookies)




if __name__ == "__main__":
    L = login()
    L.login()

