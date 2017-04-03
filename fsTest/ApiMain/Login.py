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

class PC_Login:
    def __init__(self,oldlogin_url,dict_params,cookies):
        self.oldlogin_url = oldlogin_url
        self.dict_params = dict_params
        self.cookies = cookies

    def oldlogin(self):
        oldlogin_headers = {'Accept':'application/json, text/javascript, */*; q=0.01',
                            'Cache-Control':'no-cache',
                            'Accept-Encoding':'gzip, deflate, br',
                            'Accept-Language':'zh-CN,zh;q=0.8',
                            'Connection':'keep-alive',
                            'Content-Type':'application/json'}
        Cookies = []
        try:
            for i in range(len(self.dict_params.get('StatusCode_oldlogin'))):
                oldlogin_params = {}
                oldlogin_params['EnterpriseAccount'] = str(self.dict_params.get('EnterpriseAccount')[i])
                oldlogin_params['UserAccount'] = str(self.dict_params.get('UserAccount')[i])
                oldlogin_params['Password'] = str(self.dict_params.get('Password')[i])
                oldlogin_params['PersistenceHint'] = str(self.dict_params.get('PersistenceHint')[i])
                #oldlogin_params['ImgCode'] = str(eval(str(self.dict_params.get('ImgCode')).replace(' ',''))[i])
                oldlogin_params['ClientId'] = str(self.dict_params.get('ClientId_old')[i])
                http = HttpUntils.HttpUntils(self.oldlogin_url,oldlogin_params,oldlogin_headers,self.cookies)
                result = http.Post()
                JsonResult = result.json()
                if result.cookies:
                    self.cookies = result.cookies
                    Cookies.append(self.cookies)
                    return Cookies
                else:
                    print JsonResult

        except Exception,e:
            print e


