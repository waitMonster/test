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
from pyexcel_xls import get_data
from pyexcel_xls import save_data
import xlrd
import collections


class fs_datadevice:
    def __init__(self):
        self.path = os.path.abspath('..') + '\\Data\\fs_XLS\\'
        self.xls_name = 'fs_apitest.xlsx'
        if os.path.exists(self.path + self.xls_name):
            self.xls_data = xlrd.open_workbook(self.path + self.xls_name)
        self.table = self.xls_data.sheets()
        self.num = []

    def Rxls_URL(self):
        nrows = self.table[0].nrows  # 行数
        ncols = self.table[0].ncols  # 列数
        URL = []
        for i in range(1, nrows):
            data_url = self.table[0].row_values(i)
            if data_url[1]:
                URL.append(data_url)
            else:
                print u'接口地址不能为空'
        for j in range(len(URL)):
            del URL[j][ncols - 1]

        self.num = self.table[0].col_values(ncols - 1)
        del self.num[0]
        print dict(URL)
        print self.num


    def Rxls_Data(self):
        nrows = self.table[1].nrows  # 行数
        ncols = self.table[1].ncols  # 列数
        Data = []
        Datas = {}
        for i in range(nrows):
            data_data = self.table[1].row_values(i)
            for j in data_data[:]:
                if j == '':
                    data_data.remove(j)
            Data.append(data_data)

        for j in range(len(self.num)):
            if j == 0:
                for l in range(int(self.num[j] + str(1)), int(self.num[j + 1])):
                    for k in range(len(Data[int(self.num[j])])):
                        Datas[Data[int(self.num[j])][k]]=Data[l][k]

        print Datas


if __name__ == '__main__':
    f = fs_datadevice()
    f.Rxls_URL()
    f.Rxls_Data()

























