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
import json

class Api:
    def __init__(self):
        self.xls_name = 'fs_apitest.xlsx'
        self.fs = fs_datadevices.fs_datadevice(self.xls_name)
        self.oldlogin_url = self.fs.Rxls_URL().get('web_oldlogin')
        self.createpro_url = self.fs.Rxls_URL().get('web_createproject')
        self.dict_params = self.fs.Rxls_Data()
        self.cookies = RequestsCookieJar()
        self.params = []

    def postlogin(self):
        oldlogin_headers = {'Accept':'application/json, text/javascript, */*; q=0.01',
                            'Cache-Control':'no-cache',
                            'Accept-Encoding':'gzip, deflate, br',
                            'Accept-Language':'zh-CN,zh;q=0.8',
                            'Connection':'keep-alive',
                            'Content-Type':'application/json'}
        R_oldlogin = []
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
                R_oldlogin.append(result.json())
                if oldlogin_params.get('UserAccount') == 'linxl':
                    self.cookies = result.cookies

            print R_oldlogin


        except Exception,e:
            print e


    def postcreatepro(self):
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
               http = HttpUntils.HttpUntils(self.createpro_url,createpro_params,createpro_headers,self.cookies)
               result = http.Post_cookies()
               R_createpro.append(result.json())

           print R_createpro

        except Exception,e:
            print e


if __name__ == '__main__':
    A = Api()
    A.postlogin()
    A.postcreatepro()




