# -*- coding: utf-8 -*-
import selenium
from appium import webdriver
import os,unittest,time
from selenium.common.exceptions import NoSuchElementException,WebDriverException
#Appium环境配置
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
class AppElements:
    def __init__(self,driver):
        self.driver = driver
        self.driver.implicitly_wait(10)
        self.Element = self.Elements = None

    def xpath(self,selector):
        try:
            self.Element = self.driver.find_element_by_xpath(selector)
        except NoSuchElementException:
            print u'元素'+selector+u'不存在'

        return self.Element

    def xpaths(self,selector):
        try:
            list_Elements = self.driver.find_elements_by_xpath(selector)
            if list_Elements:
                self.Elements = list_Elements
            else:
                self.Elements = u'元素'+selector+u'不存在'
                print self.Elements
        except WebDriverException, e:
            print 'app reeor:' + str(e)

        return self.Elements

    def id(self,selector):
        try:
            self.Element = self.driver.find_element_by_id(selector)
        except NoSuchElementException:
            self.Element = u'元素'+selector+u'不存在'
            print self.Element

        return self.Element

    def ids(self,selector):
        try:
            list_Elements = self.driver.find_elements_by_id(selector)
            if list_Elements:
                self.Elements = list_Elements
            else:
                self.Elements = u'元素'+selector+u'不存在'
                print self.Elements
        except WebDriverException,e:
            print 'app reeor:'+str(e)

        return self.Elements

    def CLASS(self,selector):
        try:
            self.Element = self.driver.find_element_by_class_name(selector)
        except NoSuchElementException:
            print u'元素'+selector+u'不存在'

        return self.Element

    def CLASS_S(self,selector):
        try:
            list_Elements = self.driver.find_elements_by_class_name(selector)
            if list_Elements:
                self.Elements = list_Elements
            else:
                self.Elements = u'元素'+selector+u'不存在'
                print self.Elements
        except WebDriverException, e:
            print 'app reeor:' + str(e)

        return self.Elements
    def name(self,selector):
        try:
            self.Element = self.driver.find_element_by_name(selector)
        except NoSuchElementException:
            print u'元素'+selector+u'不存在'

        return self.Element
    def names(self,selector):
        try:
            list_Elements = self.driver.find_elements_by_name(selector)
            if list_Elements:
                self.Elements = list_Elements
            else:
                self.Elements = u'元素'+selector+u'不存在'
                print self.Elements
        except WebDriverException, e:
            print 'app reeor:' + str(e)

        return self.Elements
    def Desc(self,selector):
        try:
            self.Element = self.driver.find_element_by_accessibility_id(selector)
        except NoSuchElementException:
            print u'元素'+selector+u'不存在'

        return self.Element
    def Descs(self,selector):
        try:
            list_Elements = self.driver.find_elements_by_accessibility_id(selector)
            if list_Elements:
                self.Elements = list_Elements
            else:
                self.Elements = u'元素'+selector+u'不存在'
                print self.Elements
        except WebDriverException, e:
            print 'app reeor:' + str(e)

        return self.Elements















