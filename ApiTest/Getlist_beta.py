# -*- coding: utf-8 -*-
import urllib,urllib2
import ConfigParser
import codecs
from lib2to3.pgen2 import driver
import time
import fractions
import sysconfig
import paramiko

import select
import os,sys
import linecache
import datetime

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common import keys
from bs4 import BeautifulSoup
import requests

class getlist_beta:
    def __init__(self,url,data,path,Time):
        self.url = url
        self.data = data
        self.path = path
        self.Time = Time

    def getlist(self):
        URL = 'http://l-tts9.vc.beta.cn6.qunar.com/supplier/order.do?opType=getOrder&displayId=&selecttime=create&starttime=2017-03-03&stoptime=2017-03-03&coupon=&product_name=&order_status=-1&refund_status=-1&purchase_order_status=-1&purchase_order_refund_status=-1&visa_status=-1&productId=&order_combine=G&order_source=all&securityDepositStatus=-1&groupOrderStatus=-1&contact_user=&visit=-1&departure=&arrive=&contact_mobile=&csrfToken=hwCOIahxriqIGwPLX7Vyt0H6RucdrfXv&od=all&pageNo=1&perPageNo=10'
        soup = requests.get(URL,verify=False).text

        print soup





