# -*- coding: utf-8 -*-
import codecs
import time
import urllib

from selenium import webdriver
import os
import datetime
from Main import detil_main

class PCbeta_Calendar:
    def __init__(self,drive,url,data,Year,path,Time):
        self.drive = drive
        self.url = url
        self.data = data
        self.Year = Year
        self.path = path
        self.Time = Time
        self.m = detil_main.detil_main(self.drive,self.url,self.data,self.Year)

    def detil(self):
        for i in range(2,3):
            for j in range(5,8):
                self.m.getdetil()
                xpath = './/*[@id="booking-info"]/div/div[1]/div[2]/table/tbody/tr['+str(i)+']/td['+str(j)+']/div'
                element = self.drive.find_element_by_xpath(xpath)
                if u'¥' in element.text:
                    element.click()
                    self.drive.find_element_by_xpath('.//*[@id="booking-info"]/div/div[2]/ul/li[3]/a').click()
                    time.sleep(2)
                    con_element = self.drive.find_element_by_xpath('.//*[@id="confirmOrder"]/div/div[1]/div[1]/div[3]/div[1]/div[3]')
                    if con_element.text == u'您选择的机票库存不足，请重新选择日期和机票':
                        print con_element.text
                        continue
                    else:
                        self.m.passenger_info_gj()
                else:
                    print u'请检查本天价格库存设置'

    def orderlist(self):
        self.drive.get(self.url[2])
        time.sleep(5)
        logname = self.path+self.Time+u'下单支付操作'+'.log'
        if not os.path.exists(logname):
                f = codecs.open(logname,'w','utf-8')
        self.drive.execute_script("var q=document.body.scrollTop=100")
        OrderLists = []
        for i in range(2,13,5):
            div = './/*[@id="orderContents"]/div[4]/table/tbody/tr['
            span = ']/td[1]/table/tbody/tr[1]/th/ul/li/span'
            self.drive.execute_script("var q=document.body.scrollTop=100")
            time.sleep(2)
            order_number = self.drive.find_element_by_xpath(div+str(i)+span).text
            fly_number = self.drive.find_element_by_xpath(div+str(i+2)+span).text
            order_list =u'整单编号：'+order_number+','+u'机票单号'+fly_number+','+u'状态：'+self.drive.find_element_by_xpath(div+str(i)+']/td[5]/div').text.replace('\n','')+'\n'
            f.write(order_list)

        f.close()






