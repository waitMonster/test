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
        for i in range(1,7):
            for j in range(1,8):
                element = 'html/body/div[5]/div/table/tbody/tr['+str(i)+']/td['+str(j)+']/div/p'
                if self.drive.find_element_by_xpath(element).text == u'今天':
                    break

        print i,j




