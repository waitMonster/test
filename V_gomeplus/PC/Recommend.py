# -*- coding: utf-8 -*-
import ConfigParser
import codecs,unittest
from lib2to3.pgen2 import driver
import time
import fractions
import sysconfig
import select
import os,sys
from selenium import webdriver
from selenium.common.exceptions import ElementNotVisibleException
from selenium.webdriver import ActionChains
from selenium.webdriver.common import keys
from Data.devices import WebElements

class Recommend(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.web = WebElements.WebElements(self.driver)
        self.driver.get('http://v.gomeplus.com/')
        self.i = 1

    def tearDown(self):
        self.driver.quit()

    def test_recommend_num(self):
        try:
            while True:
                xpath = './/*[@id="videoList"]/ul/li['+str(self.i)+']/a/div'
                video_player = self.web.xpath(xpath)
                video_player.click()
                time.sleep(3)
                handles = self.driver.window_handles
                if len(handles)>1:
                    self.driver.close()
                else:
                    print u'第'+str(self.i)+u'个视频无效'
                self.drive.execute_script("var q=document.body.scrollTop=100")
                self.i = self.i+1
                if self.web.xpath('.//*[@id="videoList"]/div[2]/div/a').text == u'没有更多了':
                    break
            print u'PC首页共有推荐视频'+str(self.i)+u'个'

        except AttributeError,a:
            print u'异常原因：'+str(a)
            self.assertEqual('',str(a))
        except ElementNotVisibleException,e:
            print u'异常原因：'+str(e)
            self.assertEqual('',str(e))
















