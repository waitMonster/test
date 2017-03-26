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
        self.xls_name = 'fs_apitest.xlsx'
        self.fs = fs_datadevices.fs_datadevice(self.xls_name)
        self.getlogin_url = self.fs.Rxls_URL().get('web_getlogin')
        self.oldlogin_url = self.fs.Rxls_URL().get('web_oldlogin')
        self.createpro_url = self.fs.Rxls_URL().get('web_createproject')
        self.dict_params = self.fs.Rxls_Data()
        self.cookies = []

    def getlogin(self):
        getlogin_url = self.getlogin_url
        getlogin_headers = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                            'Cache-Control':'no-cache',
                            'Accept-Encoding':'gzip, deflate, br',
                            'Accept-Language':'zh-CN,zh;q=0.8',
                            'Connection':'keep-alive'
                            }
        r = requests.get(getlogin_url,headers=getlogin_headers,verify=False)
        self.cookies.append(r.cookies)
        return self.cookies[0]

    def postlogin(self):
        oldlogin_url = self.oldlogin_url
        cookie = self.cookies[0]
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
                oldlogin_params['ImgCode'] = str(eval(str(self.dict_params.get('ImgCode')).replace(' ',''))[i])
                oldlogin_params['ClientId'] = str(self.dict_params.get('ClientId_old')[i])
                r = requests.post(oldlogin_url,data=oldlogin_params,json=oldlogin_headers,cookies=cookie,verify=False)
                self.cookies.append(r.cookies)
                R_oldlogin.append(eval(r.content))
                print oldlogin_params

            print R_oldlogin


        except Exception,e:
            print e


    def postcreatepro(self):
        createpro_url = self.oldlogin_url
        createpro_headers = {'Content-Type':'application/json'}
        R_createpro = []
        try:
           for i in range(len(self.dict_params.get('StatusCode_createpro'))):
               createpro_params = {}
               template = {}
               createpro_params['creatorId'] = self.dict_params.get('creatorId')[i]
               createpro_params['name'] = self.dict_params.get('name')[i]
               createpro_params['description'] = self.dict_params.get('description')[i]
               createpro_params['star'] = self.dict_params.get('star')[i]
               createpro_params['admins'] = self.dict_params.get('admins')[i]
               createpro_params['members'] = self.dict_params.get('members')[i]
               createpro_params['ClientId'] = self.dict_params.get('ClientId_cro')[i]
               createpro_params['backgroundID'] = self.dict_params.get('backgroundID')[i]
               template['categoryType'] = self.dict_params.get('categoryType')[i]
               template['id'] = self.dict_params.get('id')[i]
               createpro_params['template'] = template
               r = requests.post(createpro_url,data=createpro_params,headers=createpro_headers,verify=False)
               R_createpro.append(eval(r.content))

           return R_createpro

        except Exception,e:
            print e


if __name__ == '__main__':
    A = Api()
    A.getlogin()
    A.postlogin()
    #A.postcreatepro()




