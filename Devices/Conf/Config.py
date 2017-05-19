# -*- coding: utf-8 -*-
import codecs, ConfigParser
import os,json
import datetime
#该模块用于取出配置文件内容，最终返回一个二级字典格式的值，每个key对应配置文件中的一个section，每个value对应配置文件中一组配置内容
class Config:
    def __init__(self):
        self.path = os.path.abspath('.')+'\\Conf\\'

    def readconfig(self,conf_name):#获取一个配置文件名，并从中读取内容
        config_data = {}
        cf = ConfigParser.SafeConfigParser()
        if os.path.exists(self.path+conf_name):
            cf.readfp(codecs.open(self.path + conf_name, 'rb', 'utf_8'))
        else:
            print u'配置文件不存在'
        for i in  cf.sections():
            data = {}
            for j in cf.options(i):
                data[j] = cf.get(i,j)

            config_data[i] = data


        return config_data



