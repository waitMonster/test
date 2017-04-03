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
from ApiMain import Login,LoginOff

class Project(unittest.TestCase):
    def setUp(self):
        self.xls_name = 'fs_apitest.xlsx'
        self.fs = fs_datadevices.fs_datadevice(self.xls_name)
        self.oldlogin_url = self.fs.Rxls_URL().get('web_oldlogin')
        self.createpro_url = self.fs.Rxls_URL().get('web_createproject')
        self.dict_params = self.fs.Rxls_Data()
        self.cookies = RequestsCookieJar()
        self.loginoff_url = self.fs.Rxls_URL().get('web_loginoff')
        self.L = Login.PC_Login(self.oldlogin_url, self.dict_params, self.cookies)
        self.Cookies = self.L.oldlogin()
        self.token = []
        for i in range(len(self.Cookies)):
            self.token.append(dict(self.Cookies[i]).get('fs_token'))
        self.F = LoginOff.PC_LoginOff(self.loginoff_url,self.token,self.cookies)

    def tearDown(self):
        self.F.loginoff()

    def test_postcreatepro(self):
        createpro_headers = {'Content-Type':'application/json'}
        R_createpro = []
        try:
           for i in range(len(self.dict_params.get('StatusCode_createpro'))):
               createpro_params = {}
               template = {}
               createpro_params['creatorId'] = str(self.dict_params.get('creatorId')[i])
               createpro_params['name'] = str(self.dict_params.get('name')[i])
               createpro_params['description'] = str(self.dict_params.get('description')[i])
               createpro_params['star'] = str(self.dict_params.get('star')[i])
               createpro_params['admins'] = eval(self.dict_params.get('admins')[i])
               createpro_params['members'] = eval(self.dict_params.get('members')[i])
               #createpro_params['ClientId'] = str(self.dict_params.get('ClientId_cro')[i])
               createpro_params['backgroundID'] = str(self.dict_params.get('backgroundID')[i])
               template['categoryType'] = str(self.dict_params.get('categoryType')[i])
               template['id'] = str(self.dict_params.get('id')[i])
               createpro_params['template'] = template
               http = HttpUntils.HttpUntils(self.createpro_url,createpro_params,createpro_headers,self.Cookies[0])
               result = http.Post_cookies()
               R_createpro.append(result.json())

           print R_createpro

        except Exception,e:
            print e

    #A.postcreatepro()




