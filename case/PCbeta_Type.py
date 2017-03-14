# -*- coding: utf-8 -*-

import codecs
import time
import urllib
import selenium

from selenium import webdriver
import os
import datetime
from Main import detil_main

class PCbeta_Type:
    def __init__(self,drive,url,data,Year,path,Time):
        self.drive = drive
        self.url = url
        self.data = data
        self.Year = Year
        self.path = path
        self.Time = Time
        self.m = detil_main.detil_main(self.drive,self.url,self.data,self.Year)

    def detil(self):
        for i in range(2,5,2):
            self.m.getdetil()
            xpath = './/*[@id="booking-info"]/div/div/div[2]/table/tbody/tr['+str(i)+']/td[6]/a'
            self.drive.find_element_by_xpath(xpath).click()
            time.sleep(3)
            self.drive.execute_script("var q=document.body.scrollTop=100")
            time.sleep(3)
            con_element = self.drive.find_element_by_xpath('.//*[@id="confirmOrder"]/div/div[1]/div[1]/div[3]/div[3]/div[3]/a')
            if con_element.text == u'您选择的机票库存不足，请重新选择日期和机票':
                print con_element.text
                continue
            else:
                self.m.passenger_info_gn()

        print '################'+datetime.datetime.now().strftime('%Y-%m-%d:%H:%M:%S')






