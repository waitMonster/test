# -*- coding: utf-8 -*-
import ConfigParser
import codecs
import unittest
import os
import datetime
from Unittest import Tester
import HTMLTestRunner
from Unittest import appium_qunar,appium_m,appium_xiaomi
from case.Main import SendMile

if __name__ == '__main__':
    suite = unittest.TestSuite()
    path = os.path.abspath('..')+'\\ApiTest\\result\\'
    time = datetime.datetime.now().strftime('%Y%m%d%H%M')
    reportname = path+time+u'测试报告'+'.html'
    #suite.addTest(Tester.Tester("test_detile1"))
    #suite.addTest(Tester.Tester("test_orderlist"))
    #suite.addTest(Tester.Tester("test_detil2"))
    #suite.addTest(Tester.Tester("test_en"))
    #suite.addTest(Tester.Tester("test_getlist"))
    suite.addTest(appium_qunar.qunarAndroidTests("test_search"))
    suite.addTest(appium_xiaomi.xiaomiAndroidTests("test_order"))
    suite.addTest(appium_m.appium_m("test_mjd"))
    if not os.path.exists(reportname):
                f = open(reportname,'wb')
    runner=HTMLTestRunner.HTMLTestRunner(stream=f,title='test report',description=u'report:')
    runner.run(suite)
    f.close()
    cf = ConfigParser.SafeConfigParser()
    conf_name = 'email.ini'
    cf.readfp(codecs.open(path+conf_name,'rb','utf_8'))
    emails = [cf.get('sdm1','user'),cf.get('sdm1','pwd'),cf.get('sdm1','to')]
    S = SendMile.SendMail(emails[0],emails[1],emails[2],reportname)
    S.send()



