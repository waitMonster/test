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

class xiaomiAndroidTests(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android' #设置平台
        desired_caps['platformVersion'] = '6.0.1' #系统版本
        desired_caps['deviceName'] = '1ea6e8e0'
        desired_caps['autoLaunch'] = 'true' #是否自动启动
        desired_caps['appPackage'] = 'com.xiaomi.shop' #包名
        desired_caps['appActivity'] = 'com.xiaomi.shop.activity.MainTabActivity'
        desired_caps['unicodeKeyboard'] = 'true'
        desired_caps['resetKeyboard'] = 'true'
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.x = self.driver.get_window_size()['width']
        self.y = self.driver.get_window_size()['height']

    def test_order(self):
        time.sleep(7)
        self.driver.find_element_by_id('com.xiaomi.shop.plugin.homepage:id/main_bottom_tab_category_icon').click()
        time.sleep(2)
        type = self.driver.find_elements_by_id('com.xiaomi.shop.plugin.homepage:id/listitem_category_group_item_cate_imageview')
        type[1].click()
        titles = self.driver.find_elements_by_id('com.xiaomi.shop.plugin.productlist:id/product_sub_title')
        for i in range(3):
            print titles[i].text+'\n'
        titles[i].click()
        time.sleep(3)
        print self.driver.contexts







