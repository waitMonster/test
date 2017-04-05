# -*- coding: utf-8 -*-
import codecs
import time
import urllib2,urllib
import requests
from selenium import webdriver
import os
import datetime
from Data.devices import fs_datadevices,HttpUntils
from requests.cookies import RequestsCookieJar
import json
import httplib
import logging,unittest

class Search_home(unittest.TestCase):
    def setUp(self):
        self.xls_name = 'mstroe_apitest.xlsx'
        self.fs = fs_datadevices.fs_datadevice(self.xls_name)
        self.hisearch_url = self.fs.Rxls_URL().get('post_hisearch')
        self.dict_params = self.fs.Rxls_Data()
        self.cookies = RequestsCookieJar()

    def tearDown(self):
        pass

    def test_postsearch(self):
        hisearch_headers = {'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
                            'Android-Ver':'23',
                            'device':'SBnmKQzYMYzOc3Z4dEKkdw==',
                            'Uuid':'bb023da5-01d5-1ec7-52c4-102f08fa927d',
                            'Network-Stat':'wifi',
                            'Accept-Encoding':'gzip'}

        for i in range(len(self.dict_params.get('desc'))):
            hisearch_params = {}
            hisearch_params['input_word'] = str(self.dict_params.get('input_word')[i])
            hisearch_params['query'] = str(self.dict_params.get('query')[i])
            hisearch_params['page_index'] = str(self.dict_params.get('page_index')[i])
            hisearch_params['checkbox'] = str(self.dict_params.get('checkbox')[i])
            hisearch_params['page_size'] = str(self.dict_params.get('page_size')[i])
            http = HttpUntils.HttpUntils(self.hisearch_url,hisearch_params,hisearch_headers,self.cookies)
            result = http.Post()
            print str(eval(result.content).get('desc'))+'\n'
