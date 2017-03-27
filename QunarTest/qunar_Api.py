# -*- coding: utf-8 -*-
import codecs
import time
import urllib2,urllib
import requests
from selenium import webdriver
import os
import datetime
from Data.devices import fs_datadevices

class Api:
    def __init__(self):
        self.xls_name = 'qunar_test.xlsx'
        self.fs = fs_datadevices.fs_datadevice(self.xls_name)
        self.loginx_url = self.fs.Rxls_Data().get('web_loginx')
        self.addtraffic_url = self.fs.Rxls_Data().get('web_addtraffic')
        self.dict_params = self.fs.Rxls_Data()
        self.cookies = []

    def loginx(self):
        R_loginx = []
        loginx_headers = {'Accept':'application/json, text/javascript, */*; q=0.01',
                            'Cache-Control':'no-cache',
                            'Accept-Encoding':'gzip, deflate, br',
                            'Accept-Language':'zh-CN,zh;q=0.8',
                            'Connection':'keep-alive',
                            'Content-Type':'aapplication/x-www-form-urlencoded; charset=UTF-8'}

        try:
            for i in range(len(self.dict_params.get('stauts_loginx'))):
                loginx_data = {}
                loginx_data['loginType'] = str(self.dict_params.get('loginType')[i])
                loginx_data['username'] = str(self.dict_params.get('username')[i])
                loginx_data['password'] = str(self.dict_params.get('password')[i])
                loginx_data['remember'] = str(self.dict_params.get('remember')[i])
                r = requests.post(self.loginx_url,data=loginx_data,headers=loginx_headers,verify=False)
                R_loginx.append(eval(r.content))

            print R_loginx

        except Exception,e:
            print e


if __name__ == '__main__':
    A = Api()
    A.loginx()