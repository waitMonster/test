# -*- coding: utf-8 -*-
import ConfigParser
import codecs
import unittest
import datetime
import urllib
import sys
from selenium import webdriver
import os
import time
from collections import OrderedDict
from pyexcel_xls import get_data
from pyexcel_xls import save_data
import xlrd

class fs_Tester:
    def __init__(self,xls_name):
        self.path = os.path.abspath('..')+'\\Data\\fs_XLS\\'
        self.xls_name = xls_name
        if os.path.exists(self.path+self.xls_name):
            self.xls_data = get_data(unicode(self.path+self.xls_name,'rb','utf-8'))
        self.values = []
        for i in self.xls_data.keys():
            self.values.append(self.xls_data[i])

    def Rxls_url(self):
        urls = []
        ApiNames = []
        dict_urls = {}
        for i in range(1,len(self.values[0])):
            url = self.values[0][i][1]
            apiname = self.values[0][i][0]
            ApiNames.append(apiname)
            if url:
                urls.append(url)
            else:
                print u'接口请求地址不能为空'






















