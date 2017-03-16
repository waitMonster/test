# -*- coding: utf-8 -*-
import ConfigParser
import codecs
import unittest
import datetime
import urllib
import sys
from selenium import webdriver
import os
import time
from case import PCbeta_Calendar,PCbeta_Type,dujia_AddNewProduct,PCchangetkicts



import re
class Tester(unittest.TestCase):
    def setUp(self):
        chromeoath = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
        profile_dir=r"C:\Users\yaguang.zhang\AppData\Local\Google\Chrome\User Data"
        chrome_options=webdriver.ChromeOptions()
        chrome_options.add_argument("user-data-dir="+os.path.abspath(profile_dir))
        chrome_options.add_argument("--disable-extensions")
        self.drive = webdriver.Chrome(chromeoath,chrome_options=chrome_options)
        self.path = os.path.abspath('..')+'\\ApiTest\\result\\'
        cf = ConfigParser.SafeConfigParser()
        conf_name = 'apicase.ini'
        cf.readfp(codecs.open(self.path+conf_name,'rb','utf_8'))
        self.url = [cf.get('URL','url_detile'),cf.get('URL','url_confrom'),cf.get('URL','url_orderlist'),cf.get('URL','url_admin')]
        self.data = []
        for i in range(2):
            self.Item = cf.items(cf.sections()[i])
            self.data.append(self.Item)
        self.Time = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        self.Year = ['1991','12','31','2099','12','12']
        self.p1 = PCbeta_Calendar.PCbeta_Calendar(self.drive,self.url,self.data,self.Year,self.path,self.Time)
        self.p2 = PCbeta_Type.PCbeta_Type(self.drive,self.url,self.data,self.Year,self.path,self.Time)
        self.Contents = []
        self.con = 'content'
        self.confs_name = ['login.ini', 'config.ini']
        cf1 = ConfigParser.SafeConfigParser()
        for k in range(2):
                cf1.readfp(codecs.open(self.path + self.confs_name[k], "rb", "utf8"))
                if k == 0:
                    for j in range(1, 7):
                        uu = [cf1.get(self.con + str(j), 'username'), cf1.get(self.con + str(j), 'passwd'),
                              cf1.get(self.con + str(j), 'result')]
                        self.Contents.extend(uu)
                elif k == 1:
                    self.Options = [cf1.get('options', 'Protitle'), cf1.get('options', 'Profeat'),
                                    cf1.get('options', 'teamNo'),
                                    cf1.get('options', 'Remark'), cf1.get('options', 'Day'), cf1.get('options', 'Nijht'),
                                    cf1.get('options', 'Advance'),cf1.get('options','pass'),cf1.get('options','city1'),cf1.get('options','city2')]

        self.p3 = dujia_AddNewProduct.dujiaAdd(self.drive,self.Options,self.Contents,self.path,self.url,self.Time)
        self.c = PCchangetkicts.changetkicts(self.drive,self.url,self.data,self.Year,self.path,self.Time)

    def tearDown(self):
        self.drive.quit()

    def test_detile1(self):
        self.p1.detil()

    def test_orderlist(self):
        self.p1.orderlist()

    def test_detil2(self):
        self.p2.detil()

    def test_en(self):
        self.p3.en()

    def test_change(self):
        self.c.change()






































if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Tester)
    unittest.TextTestRunner(verbosity=2).run(suite)




