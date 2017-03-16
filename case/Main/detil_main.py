# -*- coding: utf-8 -*-
import urllib
from selenium import webdriver
import time


class detil_main:
    def __init__(self,drive,url,data,Year):
        self.drive = drive
        self.url = url
        self.data = data
        self.Year = Year

    def getdetil(self):

        self.drive.get(self.url[0] + urllib.urlencode(self.data[0]).replace('tuid','tuId'))
        time.sleep(3)
        #pro_title = self.drive.find_element_by_xpath('.//*[@id="page-root"]/div[2]/div[3]/div[2]/h1')
        #print pro_title.text
        self.drive.execute_script("var q=document.body.scrollTop=400")
        time.sleep(3)

    def getcomfirm(self):
        self.drive.get(self.url[1]+ urllib.urlencode(self.data[1]).replace('tuid','tuId').replace('pid','pId'))
        time.sleep(3)

    def passenger_info_gj(self):
        self.drive.execute_script("var q=document.body.scrollTop=800")
        time.sleep(2)
        for p in range(1,5):
            li = './/*[@id="js_p_passenger"]/div[3]/ul[1]/li/div/div[2]/div/div['+str(p)+']'
            inputs = ']/input'
            div1 = '/div['
            div2 = '/div/div['
            if p == 1:
                self.drive.find_element_by_xpath(li+'/div[2]/input[2]').send_keys('css')
                self.drive.find_element_by_xpath(li+'/div[5]/input').send_keys('0123456789')
            elif p == 2:
                for d in [2,4]:
                    self.drive.find_element_by_xpath(li+div1+str(d)+inputs).send_keys('ssss')
            elif p == 3:
                for d in [4,5,6]:
                    self.drive.find_element_by_xpath(li+div2+str(d)+inputs).send_keys(self.Year[d-4])
            elif p == 4:
                for d in [4,5,6]:
                    self.drive.find_element_by_xpath(li+div2+str(d)+inputs).send_keys(self.Year[d-1])
        #time.sleep(3)
        self.drive.find_element_by_xpath('.//*[@id="js_p_accounts"]/div/a').click()
        time.sleep(10)
        self.drive.find_element_by_xpath('html/body/div[2]/div/div/div[2]/div[3]/div[1]/div[1]/div/div/label/input').click()
        time.sleep(3)
        self.drive.find_element_by_xpath('.//*[@id="goto_trade_code"]/span[2]').click()
        time.sleep(3)
        self.drive.find_element_by_xpath('html/body/div[4]/div/div/div[2]/form/div[2]/div[2]/table/tbody/tr[1]/td[2]/div/div[1]/input').send_keys('abc123')
        self.drive.find_element_by_xpath('html/body/div[4]/div/div/div[2]/form/div[3]/a').click()
        time.sleep(3)
        title = self.drive.find_element_by_xpath('html/body/div[2]/div/div/div[2]/div/table/tbody/tr/td[2]/div/div/span').text
        print u'本次日历产品下单并支付成功：'+title
        time.sleep(5)

    def passenger_info_gn(self):
        self.drive.execute_script("var q=document.body.scrollTop=800")
        time.sleep(3)
        self.drive.find_element_by_xpath('.//*[@id="js_p_passenger"]/div[3]/ul[1]/li/div/div[2]/div[1]/div[2]/input[2]').send_keys('css')
        self.drive.find_element_by_xpath('.//*[@id="js_p_passenger"]/div[3]/ul[1]/li/div/div[2]/div[1]/div[5]/input').send_keys('412821199112314456')
        self.drive.find_element_by_xpath('.//*[@id="js_p_accounts"]/div/a').click()
        time.sleep(7)
        self.drive.find_element_by_xpath('html/body/div[2]/div/div/div[2]/div[3]/div[1]/div[2]/div/div/label/input').click()
        time.sleep(3)
        self.drive.find_element_by_xpath('.//*[@id="goto_trade_code"]/span[2]').click()
        time.sleep(3)
        self.drive.find_element_by_xpath('html/body/div[4]/div/div/div[2]/form/div[2]/div[2]/table/tbody/tr[1]/td[2]/div/div[1]/input').send_keys('abc123')
        self.drive.find_element_by_xpath('html/body/div[4]/div/div/div[2]/form/div[3]/a').click()
        time.sleep(3)
        title = self.drive.find_element_by_xpath('html/body/div[2]/div/div/div[2]/div/table/tbody/tr/td[2]/div/div/span').text
        print u'本次类型产品下单并支付成功：'+title

