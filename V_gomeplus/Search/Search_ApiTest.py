# -*- coding: utf-8 -*-
import codecs, ConfigParser
import time
import urllib2,urllib
import requests
from requests.cookies import RequestsCookieJar
from selenium import webdriver
import os
import datetime
from Data.devices import fs_datadevices,HttpUntils
import json,unittest
class Search_ApiTest(unittest.TestCase):
    def setUp(self):
        self.xls_name = 'V_gomeplus.xlsx'
        self.V = fs_datadevices.fs_datadevice(self.xls_name)
        self.cf =  ConfigParser.SafeConfigParser()
        self.path = 'E:\\ZygTest\\Data\\result\\'
        conf_name = 'config.ini'
        self.cf.readfp(codecs.open(self.path + conf_name, 'rb', 'utf_8'))
        self.search_url = []
        self.searchpub_url = []
        self.searchimg_url = []
        for option in self.cf.options('options'):
            self.url1 = self.cf.get('options',option)+self.V.Rxls_URL().get('GetSearch')
            self.search_url.append(self.url1)

        for option in self.cf.options('options'):
            self.url2 = self.cf.get('options',option)+self.V.Rxls_URL().get('GetSearchPublisher')
            self.searchpub_url.append(self.url2)

        for option in self.cf.options('options'):
            self.url3 = self.cf.get('options',option)+self.V.Rxls_URL().get('GetSearchImage')
            self.searchimg_url.append(self.url3)

        self.dict_params = self.V.Rxls_Data()
        self.cookies = RequestsCookieJar()

    def tearDown(self):
        pass

    def test_search(self):
        search_headers = {}
        for i in range(len(self.search_url)):
            for j in range(len(self.dict_params.get('message'))):
                search_params = {}
                search_params['platform'] = self.dict_params.get('platform')[j]
                search_params['device_id'] = self.dict_params.get('device_id')[j]
                search_params['auth'] = str(self.dict_params.get('auth')[j]).split(',')[i]
                search_params['name'] = self.dict_params.get('name')[j]
                search_params['size'] = self.dict_params.get('size')[j]
                http = HttpUntils.HttpUntils(self.search_url[i],search_params,search_headers,self.cookies)
                respeson = http.Get()
                if search_params.get('platform') == 'pc':
                    self.assertEqual(str(self.dict_params.get('code')[j]),str(eval(respeson.content).get('code')))
                    self.assertEqual(str(self.dict_params.get('message')[j]),str(eval(respeson.content).get('message')))
                else:
                    break

    def test_searchpublisher(self):
        searchpub_headers = {}
        for i in range(len(self.search_url)):
            for j in range(len(self.dict_params.get('message_pub'))):
                search_params = {}
                search_params['platform'] = self.dict_params.get('platform')[j]
                search_params['device_id'] = self.dict_params.get('device_id')[j]
                search_params['auth'] = str(self.dict_params.get('auth')[j]).split(',')[i]
                search_params['name'] = self.dict_params.get('name')[j]
                search_params['page'] = self.dict_params.get('page')[j]
                search_params['size'] = self.dict_params.get('size')[j]
                http = HttpUntils.HttpUntils(self.searchpub_url[i], search_params, searchpub_headers, self.cookies)
                respeson = http.Get()
                if search_params.get('platform') == 'pc':
                    self.assertEqual(str(self.dict_params.get('code_pub')[j]),str(eval(respeson.content).get('code')))
                    self.assertEqual(str(self.dict_params.get('message_pub')[j]),str(eval(respeson.content).get('message')))
                else:
                    break



    def test_searchimage(self):
        search_headers = {}
        for i in range(len(self.search_url)):
            for j in range(len(self.dict_params.get('message_img'))):
                search_params = {}
                search_params['platform'] = self.dict_params.get('platform')[j]
                search_params['device_id'] = self.dict_params.get('device_id')[j]
                search_params['auth'] = str(self.dict_params.get('auth')[j]).split(',')[i]
                search_params['name'] = self.dict_params.get('name')[j]
                search_params['page'] = self.dict_params.get('page')[j]
                search_params['size'] = self.dict_params.get('size')[j]
                http = HttpUntils.HttpUntils(self.searchimg_url[i], search_params, search_headers, self.cookies)
                respeson = http.Get()
                if search_params.get('platform') == 'pc':
                    self.assertEqual(str(self.dict_params.get('code_img')[j]),str(eval(respeson.content).get('code')))
                    self.assertEqual(str(self.dict_params.get('message_img')[j]),str(eval(respeson.content).get('message')))
                else:
                    break





