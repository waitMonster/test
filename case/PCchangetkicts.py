# -*- coding: utf-8 -*-
import codecs
import time
import urllib

from selenium import webdriver
import os
import datetime
from Main import detil_main

class changetkicts:
    def __init__(self,drive,url,data,Year,path,Time):
        self.drive = drive
        self.url = url
        self.data = data
        self.Year = Year
        self.path = path
        self.Time = Time
        self.m = detil_main.detil_main(self.drive,self.url,self.data,self.Year)

    def change(self):
        self.m.getcomfirm()
        self.drive.find_element_by_xpath('.//*[@id="js_p_booking"]/div[1]/div[2]/div[1]/i').click()
        self.drive.find_element_by_xpath('html/body/div[5]/div/div/ul/li[1]/a').click()
        time.sleep(3)
        for i in range(1,7):
            for j in range(1,8):
                element1 = 'html/body/div[5]/div/table/tbody/tr['+str(i)+']/td['+str(j)+']/div/p'
                #print self.drive.find_element_by_xpath(element).text
                if self.drive.find_element_by_xpath(element1).text == u'今天':
                    break
            else:
                continue
            break
        self.drive.find_element_by_xpath('html/body/div[5]/div/span').click()
        time.sleep(2)
        for k in range(i,7):
            if k == i:
                for g in range(j,8):
                    self.drive.find_element_by_xpath('.//*[@id="js_p_booking"]/div[1]/div[2]/div[1]/i').click()
                    self.drive.find_element_by_xpath('html/body/div[5]/div/div/ul/li[1]/a').click()
                    element2 ='html/body/div[5]/div/table/tbody/tr['+str(k)+']/td['+str(g)+']/div/p'
                    self.drive.find_element_by_xpath(element2).click()
                    time.sleep(2)
                    title = self.drive.find_element_by_xpath('.//*[@id="confirmOrder"]/div/div[1]/div[1]/div[3]/div/div[3]').text
                    if title == u'您选择的机票库存不足，请重新选择日期和机票':
                        continue
                    else:
                        self.drive.find_element_by_xpath('.//*[@id="confirmOrder"]/div/div[1]/div[1]/div[3]/div[1]/div[3]/a').click()
                        time.sleep(3)
                        print self.drive.find_element_by_xpath('.//*[@id="messageContainer"]').text
                        self.drive.find_element_by_xpath('html/body/div[10]/div[1]/a').click()
                        time.sleep(2)
            else:
                for g in range(1,8):
                    self.drive.find_element_by_xpath('.//*[@id="js_p_booking"]/div[1]/div[2]/div[1]/i').click()
                    self.drive.find_element_by_xpath('html/body/div[5]/div/div/ul/li[1]/a').click()
                    element2 ='html/body/div[5]/div/table/tbody/tr['+str(k)+']/td['+str(g)+']/div/p'
                    self.drive.find_element_by_xpath(element2).click()
                    time.sleep(2)
                    title = self.drive.find_element_by_xpath('.//*[@id="confirmOrder"]/div/div[1]/div[1]/div[3]/div/div[3]').text
                    if title == u' 您选择的机票库存不足，请重新选择日期和机票':
                        continue
                    else:
                        self.drive.find_element_by_xpath('.//*[@id="confirmOrder"]/div/div[1]/div[1]/div[3]/div[1]/div[3]/a').click()
                        time.sleep(3)
                        print self.drive.find_element_by_xpath('.//*[@id="messageContainer"]').text
                        self.drive.find_element_by_xpath('html/body/div[10]/div[1]/a').click()
                        time.sleep(2)








