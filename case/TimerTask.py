# -*- coding: utf-8 -*-
import ConfigParser
import codecs
from lib2to3.pgen2 import driver
import time
import fractions
import sysconfig
import paramiko

import select
import os,sys

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common import keys

class timerTask:
    def __init__(self):
        lasttime = ''
        chromeoath = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
        profile_dir=r"C:\Users\yaguang.zhang\AppData\Local\Google\Chrome\User Data"
        chrome_options=webdriver.ChromeOptions()
        chrome_options.add_argument("user-data-dir="+os.path.abspath(profile_dir))
        self.drive = webdriver.Chrome(chromeoath,chrome_options=chrome_options)
        self.drive.get("http://beta.qschedule.corp.qunar.com/jobs.do")

    def task(self):
        self.drive.find_element_by_xpath('//input[@name="jobName"]').send_keys('settlement.settlementTransQTask')
        self.drive.find_element_by_xpath('//a[@id="search"]').click()
        try:
            for i in range(5):
                self.drive.find_element_by_xpath('//a[@class="btn btn-mini btn-danger retry"]').click()
                self.drive.implicitly_wait(5)
                self.drive.find_element_by_xpath('//button[@class="btn btn-primary btn-mini ui-button ui-widget ui-state-default ui-corner-all ui-button-text-only"]').click()
                time.sleep(3)
                self.drive.back()
            self.drive.refresh()
            lasttime = self.drive.find_element_by_xpath('.//*[@id="table_report"]/tbody/tr/td[4]').text
            if lasttime:
                print u'操作页最新一次执行时间:'+lasttime+\
                      '############################'
            else:
                print u'请查看日志详情'
        except:
            return -1

    def check(self):
        true = u'已经完成'
        self.drive.forward()
        self.drive.find_element_by_xpath('//a[@href="/tasks.do?jobName=settlement.settlementTransQTask"]').click()
        try:
            for j in range(1,6):
                status = self.drive.find_element_by_xpath('.//*[@id="taskTable"]/tr['+str(j)+']/td[2]').text
                if status == true:
                    print u'第'+str(j)+u'次执行'+status
                else:
                    print u'第'+str(j)+u'次执行'+status+'请登录服务器查询日志'
            time = self.drive.find_element_by_xpath('.//*[@id="taskTable"]/tr[1]/td[4]').text
            print '###############################'+\
                  u'日志页最新一次执行时间:'+time
            return 0
        except:
            print u'没有找到结果请查看日志'
            return -1

if __name__ == '__main__':
    t = timerTask()
    t.task()
    t.check()
