# -*- coding: utf-8 -*-
import ConfigParser
import codecs
from lib2to3.pgen2 import driver
import new


import time
import fractions
import sysconfig

import select
import os, sys

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common import keys


class ChromeOptions(object):
    pass


class dujiaAdd:
    def __init__(self,drive,Options,Contents,path,url,Time):
        self.drive = drive
        self.Options = Options
        self.path = path
        self.Contents = Contents
        self.url = url
        self.Time = Time

    def en(self):
        self.drive.get(self.url[3])
        time.sleep(3)
        button = self.drive.find_element_by_xpath('//a[@id="mainmenu_142"]')
        button.click()
        # self.drive.maximize_window()
        time.sleep(5)
        self.drive.switch_to.frame("show_info")
        time.sleep(3)
        self.drive.find_element_by_xpath('//a[@href="product.jsp?p_function=freetrip&free_type=normal"]').click()
        self.drive.switch_to.default_content()
        handles = self.drive.window_handles
        if len(handles) == 2:
            self.drive.switch_to.window(handles[1])
            time.sleep(3)
            #self.drive.get_screenshot_as_file(self.path+'jietu\\'+self.Time+u'基本信息页面.png')
            inputs = self.drive.find_elements_by_xpath('//input[@type="text"]')
            for i in range(1,16):
                a1 = './/*[@id="tr_basic"]/td[2]/label['
                a2 = './/*[@id="frm_2"]/table[1]/tbody/tr[6]/td[2]/label['
                if i in [1,2]:
                    self.drive.find_element_by_xpath(a1+str(i)+']').click()
                elif i in range(3,6):
                    self.drive.find_element_by_xpath(a2+str(i)+']').click()
                elif i in [6,7,8,9,10,11,12,14,15] :
                    inputs[i-3].send_keys(self.Options[i-6])
                    if i == 14:
                        time.sleep(3)
                        self.drive.find_element_by_xpath('html/body/div[9]/table/tbody/tr/td').click()
                    elif i == 15:
                        time.sleep(3)
                        self.drive.find_element_by_xpath('html/body/div[8]/table/tbody/tr[1]/td').click()
                        self.drive.find_element_by_xpath('.//*[@id="arriveContainer"]/td[2]/img').click()
                else:
                    continue

            selects = self.drive.find_elements_by_xpath('//select[@data-jvalidator-pattern="selected"]')
            for i in range(2):
                selects[i].click()
                if i == 0:
                    self.drive.find_element_by_xpath('.//*[@id="totraffic"]/option[3]').click()
                else:
                    self.drive.find_element_by_xpath('.//*[@id="backtraffic"]/option[3]').click()

            self.drive.find_element_by_xpath('.//*[@id="pay_way_0"]').click()

            self.drive.find_element_by_xpath('.//*[@id="frm_2"]/table[1]/tbody/tr[23]/td[2]/div[3]/a').click()
            time.sleep(3)
            for i in range(1,4):
                img = './/*[@id="image-layer"]/div[2]/div[1]/div[2]/ul[1]/li['+str(i)+']/div/img'
                self.drive.find_element_by_xpath(img).click()
            time.sleep(3)
            self.drive.find_element_by_xpath('.//*[@id="image-layer"]/div[2]/div[3]/a').click()

            time.sleep(15)



















        else:
            #self.drive.save_screenshot(self.path+'jietu\\'+self.Time+u'点击添加err'+'.png')
            print u'请查看日志'






















