# -*- coding: utf-8 -*-
import codecs
import time
import urllib2,urllib
import requests
from selenium import webdriver
import os
import datetime

class Login:
    def __init__(self):
        chromeoath = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
        profile_dir = r"C:\Users\yaguang.zhang\AppData\Local\Google\Chrome\User Data"
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("user-data-dir=" + os.path.abspath(profile_dir))
        chrome_options.add_argument("--disable-extensions")
        self.drive = webdriver.Chrome(chromeoath, chrome_options=chrome_options)
        #self.url = url
        #self.drive.get(self.url[3])
        self.session = requests.session()
        self.r = ''

    def postlogin(self):
        oldlogin_url = 'https://www.fxiaoke.com/FHH/EM0HXUL/Authorize/Login'
        oldlogin_headers = {'Accept':'application/json'}
        oldlogin_params = {'EnterpriseAccount':'fktest','UserAccount':'linxl','Password':'123qwe'}
        headers = self.session.get(oldlogin_url).headers
        self.r = requests.post(oldlogin_url,data=oldlogin_params,headers=oldlogin_headers,verify=False).content
        print headers


    def login_admin(self):
        try:
            self.drive.find_element_by_xpath('.//*[@id="fxiaoke"]/body/header/div/div/a[2]').click()
            time.sleep(2)
            self.drive.find_element_by_xpath('html/body/div/div[2]/div/div[2]/div[1]/div[1]/div/div[2]').click()
            self.drive.find_element_by_xpath('.//*[@id="j-new-login-form"]/div[6]/span').click()
            time.sleep(2)
            for i in range(1,4):
                inputs = ['fktest','linxl','123qwe']
                selement = './/*[@id="j-old-login-form"]/div['+str(i)+']/input'
                self.drive.find_element_by_xpath(selement).send_keys(inputs[i-1])
            self.drive.find_element_by_xpath('.//*[@id="submit"]').click()

        except:
            print u'登录失败'


if __name__ == '__main__':
    L = Login()
    L.postlogin()




