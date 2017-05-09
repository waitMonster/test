# -*- coding: utf-8 -*-
import ConfigParser
import codecs
import unittest
import os
import datetime
import Tester
import HTMLTestRunner
import appium_m,appium_qunar,appium_app_vgomeplus
from case.Main import SendMile
from fsTest import PC_Api_Project
from V_gomeplus.Search import Search_ApiTest
from V_gomeplus.PC import Recommend
from V_gomeplus.Android import Login

if __name__ == '__main__':
    suite = unittest.TestSuite()
    path = os.path.abspath('..')+'\\Data\\result\\'
    time = datetime.datetime.now().strftime('%Y%m%d%H%M')
    reportname = path+time+u'测试报告'+'.html'
    #suite.addTest(Tester.Tester("test_detile1"))
    #suite.addTest(Tester.Tester("test_orderlist"))
    #suite.addTest(Tester.Tester("test_detil2"))
    #suite.addTest(Tester.Tester("test_en"))
    #suite.addTest(Tester.Tester("test_change"))
    #suite.addTest(Tester.Tester("test_timeTask"))
    #suite.addTest(appium_qunar.qunarAndroidTests("test_search"))
    #suite.addTest(appium_xiaomi.xiaomiAndroidTests("test_order"))
    #suite.addTest(appium_m.appium_m("test_mjd"))';
    #suite.addTest(PC_Api_Project.Project("test_postcreatepro"))
    #suite.addTest(PC_Api_Project.Project("test_postprojectlist"))
    #suite.addTest(Search_ApiTest.Search_ApiTest("test_search"))
    #suite.addTest(Search_ApiTest.Search_ApiTest("test_searchpublisher"))
    #suite.addTest(Search_ApiTest.Search_ApiTest("test_searchimage"))
    #suite.addTest(appium_app_vgomeplus.app_vgomeplus("test_video_detail"))
    #suite.addTest(Recommend.Recommend("test_recommend_num"))
    suite.addTest(Login.Login("test_login"))
    #if not os.path.exists(reportname):
                #f = open(reportname,'wb')
    #runner=HTMLTestRunner.HTMLTestRunner(stream=f,title='test report',description=u'report:')
    #runner.run(suite)
    #f.close()
    runner = unittest.TextTestRunner()
    runner.run(suite)
    #cf = ConfigParser.SafeConfigParser()
    #conf_name = 'email.ini'
    #cf.readfp(codecs.open(path+conf_name,'rb','utf_8'))
    #emails = [cf.get('sdm1','user'),cf.get('sdm1','pwd'),cf.get('sdm1','to')]
    #S = SendMile.SendMail(emails[0],emails[1],emails[2],reportname)
    #S.send()



