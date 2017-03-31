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

class Api:
    def __init__(self):
        #abc
        self.xls_name = 'qunar_test.xlsx'
        self.fs = fs_datadevices.fs_datadevice(self.xls_name)
        self.loginx_url = self.fs.Rxls_URL().get('web_loginx')
        self.addtraffic_url = self.fs.Rxls_URL().get('web_addtraffic')
        self.dict_params = self.fs.Rxls_Data()
        self.cookies = []

    def loginx(self):
        R_loginx = []
        loginx_headers = {'Accept':'application/json, text/javascript, */*; q=0.01',
                            'Cache-Control':'no-cache',
                            'Accept-Encoding':'UTF-8',
                            'Accept-Language':'zh-CN,zh;q=0.8',
                            'Connection':'keep-alive',
                            'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8'}

        headers = eval(str(loginx_headers).replace('\'','"'))
        try:
            for i in range(len(self.dict_params.get('stauts_loginx'))):
                loginx_data = {}
                loginx_data['username'] = str(self.dict_params.get('username')[i])
                loginx_data['password'] = str(self.dict_params.get('password')[i])
                loginx_data['remember'] = str(self.dict_params.get('remember')[i])
                loginx_data['loginType'] = str(self.dict_params.get('loginType')[i])
                data = urllib.urlencode(loginx_data)
                r = requests.post(self.loginx_url,data=data,headers=headers,verify=False)
                R_loginx.append(r.content)
                print type(r.status_code)

            print R_loginx

        except Exception,e:
            print e


if __name__ == '__main__':
    A = Api()
    A.loginx()
