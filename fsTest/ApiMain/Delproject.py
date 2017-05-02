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

class Delproject:
    def __init__(self,delproject_url,projectID,Cookies):
        self.delproject_url = delproject_url
        self.projectID = projectID
        self.Cookies = Cookies

    def delproject(self):
        delproject_headers = {'Content-Type':'application/json;charset=UTF-8'}
        try:
            for i in range(len(self.projectID)):
                delproject_params = {}
                delproject_params['projectId'] = str(self.projectID[i])
                http = HttpUntils.HttpUntils(self.delproject_url,delproject_params,delproject_headers,self.Cookies[0])
                result = http.Post_cookies()
                #self.assertEquals(str(self.dict_params.get('StatusCode_createpro')[i]),str(result.json().get('Result').get('StatusCode')))
                #self.assertEquals(1,result.json().get('Value').get('status'))
                #print str(result.json())+'\n'
        except Exception,e:
            print e