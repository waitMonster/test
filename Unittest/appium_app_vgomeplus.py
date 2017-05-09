# -*- coding: utf-8 -*-
import selenium
from appium import webdriver
from selenium.common.exceptions import WebDriverException
from Data.devices.AppElements import AppElements
import os
import time
import unittest
import HTMLParser

#Appium环境配置
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class app_vgomeplus(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android' #设置平台
        desired_caps['platformVersion'] = '6.0.1' #系统版本
        desired_caps['deviceName'] = '1ea6e8e0'
        desired_caps['autoLaunch'] = 'true' #是否自动启动
        desired_caps['appPackage'] = 'cn.com.gomeplus.video' #包名
        desired_caps['appActivity'] = 'cn.com.gomeplus.video.view.SplashActivity'#启动活动
        desired_caps['unicodeKeyboard'] = 'true'
        desired_caps['resetKeyboard'] = 'true'
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.x = self.driver.get_window_size()['width']
        self.y = self.driver.get_window_size()['height']
        self.app = AppElements(self.driver)


    def tearDown(self):
        self.driver.quit()

    def test_video_detail(self):
        try:
           Video_titles = self.app.ids('cn.com.gomeplus.video:id/tv_video_title')
           Video_title_text = Video_titles[0].text
           Video_titles[0].click()
           detail_title_text = self.app.id('cn.com.gomeplus.video:id/tv_imagetext_title').text
           if Video_title_text == detail_title_text:
               print self.app.id('cn.com.gomeplus.video:id/tv_subscribe_summary').text
           else:
               print u'进入的视频详情页标题为：'+detail_title_text+u'，与视频列表不一致，请联系相关人员查看'
        except AttributeError,a:
            print u'异常原因：'+str(a)
            self.assertEqual('',str(a))
        except WebDriverException ,w:
            print u'异常原因：'+str(w)
            self.assertEqual('',str(w))




