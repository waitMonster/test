# -*- coding: utf-8 -*-
import selenium
from appium import webdriver
from selenium.common.exceptions import WebDriverException
from Data.devices.AppElements import AppElements
import os
import time
import unittest

class Login(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'  # 设置平台
        desired_caps['platformVersion'] = '6.0.1'  # 系统版本
        desired_caps['deviceName'] = '1ea6e8e0'
        desired_caps['autoLaunch'] = 'true'  # 是否自动启动
        desired_caps['appPackage'] = 'com.gomeplus.v.meimiao'  # 包名
        desired_caps['appActivity'] = 'com.gomeplus.v.meimiao.SplashActivity'  # 启动活动
        desired_caps['unicodeKeyboard'] = 'true'
        desired_caps['resetKeyboard'] = 'true'
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.x = self.driver.get_window_size()['width']
        self.y = self.driver.get_window_size()['height']
        self.point = [u'手机号/邮箱/用户名/门店会员卡', u'请输入密码']
        self.contents = ['13511035140','89692938a']
        self.app = AppElements(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        try:
            self.app.name(u'我的').click()
            user_name_button = self.app.id('com.gomeplus.v.meimiao:id/tv_user_name')
            user_name_button.click()
            current_activity_name = self.driver.current_activity
            EdTexts= self.app.CLASS_S('android.widget.EditText')
            for i in range(len(EdTexts)):
                EdTexts[i].clear()
                if EdTexts[i].text:
                    if EdTexts[i].text == self.point[i]:
                        pass
                    else:
                        print u'第'+str(i)+u'个输入框默认文案提示为：'+EdTexts[i].text+u',与预期不符'
                else:
                    print u'第'+str(i)+u'个输入框没有默认文案提示'
                if i == 0:
                    EdTexts[i].send_keys(self.contents[i])
                else:
                    self.driver.wait_activity(current_activity_name)
                    EdTexts[i].send_keys(self.contents[i])
            self.app.id('com.gomeplus.v.meimiao:id/login_button').click()
            self.app.id('com.gomeplus.v.meimiao:id/dialog_btn_sure').click()
            self.assertEqual(u'美美_031494317',user_name_button.text)

        except AttributeError,a:
            print u'异常原因：'+str(a)
            self.assertEqual('',str(a))
        except WebDriverException ,w:
            print u'异常原因：'+str(w)
            self.assertEqual('',str(w))






