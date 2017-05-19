# -*- coding: utf-8 -*-
import codecs, ConfigParser
import urllib2,urllib
import requests
from selenium import webdriver
import os
import datetime
from Devices import fs_datadevices,HttpUntils
import json,unittest
#该模块为不同终端的用户登录和登出，最后返回一个对应账号的cookies对象，需要依赖登录的接口业务测试case可以调用该模块获取
class Login:

    def __init__(self,headers):
        self.cookies = self.Cookies = None
        self.headers = headers
        self.http = HttpUntils.HttpUntils(self.headers, self.cookies)

    def H5_login(self,login_url,params):#h5登录
        for i in range(len(params.get('seven_login'))):
            login_params ={}
            login_params['username'] = params.get('username')[i]
            login_params['password'] = params.get('password')[i]
            login_params['seven_login'] = params.get('seven_login')[i]
            login_params['isAuthorized'] = params.get('isAuthorized')[i]
            repeson = self.http.Post(login_url,login_params)
            if repeson:
                if 'error' not in repeson:
                    if repeson.cookies:
                        self.Cookies = repeson.cookies
                    else:
                        print repeson.cookies

        return self.Cookies

    def H5_loginout(self,out_url,cookies):#h5注销登录
        out_headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}
        out_params = {}
        out_params['intcmp'] = 'v-public01035'
        out_params['type'] = 'logout'
        http = HttpUntils.HttpUntils(out_headers,cookies)
        repeson = http.Get_cookies(out_url,out_params)

    def Pc_login(self,login_url,params):#pc登录
        for i in range(len(params.get('gomeOrCoo8'))):
            login_params = {}
            login_params['loginName'] = params.get('loginName')[i]
            login_params['gomeOrCoo8'] = params.get('gomeOrCoo8')[i]
            login_params['password'] = params.get('password')[i]
            login_params['chkRememberUsername'] = params.get('chkRememberUsername')[i]
            login_params['captchaType'] = params.get('captchaType')[i]
            login_params['agreeFlag'] = params.get('agreeFlag')[i]
            login_params['captcha'] = eval(str(params.get('captcha')).replace(' ',''))[i]
            login_params['code'] = params.get('code')[i]
            repeson = self.http.Post(login_url,login_params)
            if eval(repeson.content).get('code') == 200:
                self.Cookies = repeson.cookies
            else:
                print repeson.cookies
        return self.Cookies


