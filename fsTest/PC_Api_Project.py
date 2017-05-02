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
from ApiMain import Login,LoginOff,Delproject

class Project(unittest.TestCase):
    def setUp(self):
        self.xls_name = 'fs_apitest.xlsx'
        self.fs = fs_datadevices.fs_datadevice(self.xls_name)
        self.oldlogin_url = self.fs.Rxls_URL().get('web_oldlogin')
        self.createpro_url = self.fs.Rxls_URL().get('web_createproject')
        self.loginoff_url = self.fs.Rxls_URL().get('web_loginoff')
        self.delproject_url = self.fs.Rxls_URL().get('web_delproject')
        self.list_url = self.fs.Rxls_URL().get('web_projectlist')
        self.login_params = self.fs.Rxls_Data().get('web_oldlogin')
        self.createpro_params = self.fs.Rxls_Data().get('web_createproject')
        self.list_params = self.fs.Rxls_Data().get('web_projectlist')
        self.cookies = RequestsCookieJar()
        self.L = Login.PC_Login(self.oldlogin_url, self.login_params, self.cookies)
        self.Cookies = self.L.oldlogin()
        self.token = []
        for i in range(len(self.Cookies)):
            self.token.append(dict(self.Cookies[i]).get('fs_token'))
        self.F = LoginOff.PC_LoginOff(self.loginoff_url,self.token,self.cookies)
        self.projectID = []

    def tearDown(self):
        if self.projectID:
            self.D = Delproject.Delproject(self.delproject_url,self.projectID,self.Cookies)
            self.D.delproject()
            self.F.loginoff()
        else:
            self.F.loginoff()

    def test_postcreatepro(self):
        createpro_headers = {'Content-Type':'application/json'}
        #R_createpro = []
        for i in range(len(self.createpro_params.get('StatusCode_createpro'))):
            createpro_params = {}
            template = {}
            createpro_params['creatorId'] = str(self.createpro_params.get('creatorId')[i])
            createpro_params['name'] = str(self.createpro_params.get('name')[i])
            createpro_params['description'] = self.createpro_params.get('description'[i])
            createpro_params['star'] = str(self.createpro_params.get('star')[i])
            createpro_params['admins'] = eval(self.createpro_params.get('admins')[i])
            createpro_params['members'] = eval(self.createpro_params.get('members')[i])
            #createpro_params['ClientId'] = str(self.dict_params.get('ClientId_cro')[i])
            createpro_params['backgroundID'] = str(self.createpro_params.get('backgroundID')[i])
            template['categoryType'] = str(self.createpro_params.get('categoryType')[i])
            template['id'] = str(self.createpro_params.get('id')[i])
            createpro_params['template'] = template
            http = HttpUntils.HttpUntils(self.createpro_url,createpro_params,createpro_headers,self.Cookies[0])
            result = http.Post_cookies()
            id = result.json().get('Value').get('projectId')
            self.projectID.append(id)
            self.assertEquals(str(self.createpro_params.get('StatusCode_createpro')[i]),str(result.json().get('Result').get('StatusCode')))
        print self.projectID

    def test_postprojectlist(self):
        list_headers = {'Content-Type':'application/json'}
        list_params = {}
        list_params['orderType'] = str(self.list_params.get('orderType')[0])
        http = HttpUntils.HttpUntils(self.list_url,list_params,list_headers,self.Cookies[0])
        result = http.Post_cookies()
        print type(result)
        ProjectList = result.json().get('Value').get('myProjectList')
        for i in range(len(ProjectList)):
            self.projectID.append(ProjectList[i].get('projectId'))
        self.assertEquals(0,result.json().get('Result').get('StatusCode'))

        print self.projectID







