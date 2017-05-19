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
from collections import OrderedDict
import xlrd
import collections


class fs_datadevice:
    def __init__(self,xls_name):
        self.path = os.path.abspath('..') + '\\Data\\fs_XLS\\'
        #print self.path
        self.path = 'E:\\ZygTest\\Data\\fs_XLS\\'
        print self.path
        self.xls_name = xls_name
        if os.path.exists(self.path + self.xls_name):
            self.xls_data = xlrd.open_workbook(self.path + self.xls_name)
        self.table = self.xls_data.sheets()

    #读取url
    def Rxls_URL(self):
        nrows = self.table[0].nrows  # 行数
        ncols = self.table[0].ncols  # 列数
        self.URL = []
        for i in range(1, nrows):
            data_url = self.table[0].row_values(i)
            if data_url[1]:
                self.URL.append(data_url)
            else:
                print u'接口地址不能为空'
        for j in range(len(self.URL)):
            del self.URL[j][ncols - 1]
        self.num = self.table[0].col_values(ncols - 1)
        self.url = self.table[0].col_values(0)
        del self.num[0]
        del self.url[0]
        for n in range(len(self.num)):
            if not self.num[n]:
                self.url.remove(self.url[n])
        for num in self.num[:]:
            if not num:
                self.num.remove(num)
        #print self.num
        return  dict(self.URL)

    #读取入参值
    def Rxls_Data(self):
        nrows = self.table[1].nrows  # 行数
        ncols = self.table[1].ncols  # 列数
        nData = []
        Data_params = {}
        for i in range(nrows):
            data = self.table[1].row_values(i)
            for j in data[:]:
                if j == '':
                    data.remove(j)
            nData.append(data)
        #print nData

        for k in range(len(self.num)):
            dict_params = {}
            for col in range(len(nData[int(self.num[k])])):
                params = []
                if k < (len(self.num)-1):
                    for nro in range(int(self.num[k])+1,int(self.num[k+1])):
                        param = self.table[1].cell(nro,col).value
                        params.append(param)
                    dict_params[nData[int(self.num[k])][col]]=params
                else:
                    for nro1 in range(int(self.num[k])+1,nrows):
                        param = self.table[1].cell(nro1,col).value
                        params.append(param)
                    dict_params[nData[int(self.num[k])][col]]=params
            Data_params[self.url[k]] = dict_params


        #for s in range(0,len(params),nro):
            #STR = [params[s],params[s+1]]
            #Data_params.append(STR)

        #print Data_params
        return Data_params





























