# -*- coding: utf-8 -*-
import selenium
from appium import webdriver
import os
import time
import unittest
import HTMLParser

#Appium环境配置
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class qunarAndroidTests(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android' #设置平台
        desired_caps['platformVersion'] = '6.0.1' #系统版本
        desired_caps['deviceName'] = '1ea6e8e0'
        desired_caps['autoLaunch'] = 'true' #是否自动启动
        desired_caps['appPackage'] = 'com.Qunar' #包名
        desired_caps['appActivity'] = 'com.mqunar.splash.SplashActivity'
        desired_caps['unicodeKeyboard'] = 'true'
        desired_caps['resetKeyboard'] = 'true'
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.x = self.driver.get_window_size()['width']
        self.y = self.driver.get_window_size()['height']


    def tearDown(self):
        self.driver.quit() #case执行完退出

    def test_search(self): #需要执行的case
        time.sleep(10)
        self.driver.find_element_by_id('com.mqunar.atom.alexhome:id/atom_alexhome_search_edittext').click()
        time.sleep(2)
        accpet = self.driver.find_element_by_id('com.mqunar.atom.voice:id/atom_voice_title_search_edittext').send_keys(u'三亚')
        time.sleep(2)
        arrows = self.driver.find_elements_by_name(u'更多')
        print type(arrows[0])
        arrows[3].click()
        time.sleep(3)
















