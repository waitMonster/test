# -*- coding: utf-8 -*-
import selenium
from appium import webdriver
import os
import time
import unittest
import HTMLParser

class appium_m(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android' #设置平台
        desired_caps['platformVersion'] = '6.0.1' #系统版本
        desired_caps['deviceName'] = '1ea6e8e0'
        desired_caps['browerName'] = 'Chrome' #浏览器名称
        desired_caps['unicodeKeyboard'] = 'true'
        desired_caps['resetKeyboard'] = 'true'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        print desired_caps

    def tearDown(self):
        self.driver.quit()

    def test_mjd(self):
        time.sleep(5)
        self.driver.get('https://m.jd.com/')
        time.sleep(3)
        search = self.driver.find_element_by_xpath('.//*[@id="index_newkeyword"]')
        search.click()
        search.send_keys('iwatch')
        self.driver.find_element_by_xpath('.//*[@id="index_search_submit"]/span').click()
        for i in range(1,5):
            time.sleep(3)
            pro = './/*[@id="searchlist44"]/li['+str(i)+']/a/div[2]/div[1]/span'
            self.driver.find_element_by_xpath(pro).click()
            time.sleep(3)
            self.driver.find_element_by_xpath('.//*[@id="cart1"]/div[2]/a[1]').click()
            if i<4:
                time.sleep(3)
                self.driver.find_element_by_xpath('.//*[@id="m_common_header_goback"]/span').click()
        time.sleep(3)
        num = int(self.driver.find_element_by_xpath('.//*[@id="carNum"]').text)
        if num == i:
            print u'购物车已添加'+str(num)+u'件商品'
        else:
            print u'购物车商品数量不对，请联系相关人员查看'






