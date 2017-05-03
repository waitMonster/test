# -*- coding: utf-8 -*-
import codecs,time,urllib2,urllib,requests,os,datetime,json,logging
from selenium import webdriver
from Data.devices import fs_datadevices

class HttpUntils:
    def __init__(self,url,data,headers,cookies):
        self.url = url
        self.data = data
        self.herders = headers
        self.cookies = cookies
        logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename='myapp.log',
                filemode='w')
        #################################################################################################
        #定义一个StreamHandler，将INFO级别或更高的日志信息打印到标准错误，并将其添加到当前的日志处理对象#
        console = logging.StreamHandler()
        console.setLevel(logging.INFO)
        formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
        console.setFormatter(formatter)
        logging.getLogger('').addHandler(console)
        #################################################################################################

    def Get(self):#get请求实现方法
        if 'auth' in self.data.keys():
            Auth = self.data.get('auth')
            data_p = urllib.urlencode(self.data)
            oldAuth = data_p.split('&')[3].split('=')[1]
            get_data = str(data_p).replace(oldAuth,Auth)
        else:
            get_data = urllib.urlencode(self.data)
        try:
           r = requests.get(self.url,params=get_data,verify=False)
           if r.status_code == 200:
               self.repeson = r
           elif r.status_code in [502,504]:
               self.repeson = 'Gateway error'
               logging.warning(self.repeson)
           else:
               self.repeson = 'sever is error'
               logging.warning(self.repeson)
        except requests.ConnectionError, e:  # 处理DNS网络问题异常
            print e
        except requests.HTTPError, h:  # 处理无效http响应异常
            print h
        except requests.Timeout, t:  # 处理请求超时异常
            print t

        return self.repeson


    def Post(self):#不需要cookies的post请求方法
        if 'x-www-form-urlencoded' in self.herders.get('Content-Type'):
            Post_data = urllib.urlencode(self.data)
        elif 'json' in self.herders.get('Content-Type'):
            Post_data = json.dumps(self.data)
        else:
            Post_data = self.data
        try:
           r = requests.post(self.url,data=Post_data,headers=self.herders,verify=False)
           if r.status_code == 200:
               self.repeson = r
           elif r.status_code in [502, 504]:
               self.repeson = 'Gateway error'
               logging.warning(self.repeson)
           else:
               self.repeson = 'sever is error'
               logging.warning(self.repeson)
        except requests.ConnectionError, e:  # 处理DNS网络问题异常
            print e
        except requests.HTTPError, h:  # 处理无效http响应异常
            print h
        except requests.Timeout, t:  # 处理请求超时异常
            print t

        return self.repeson



    def Post_cookies(self):#需要cookies的post请求方法
        if 'x-www-form-urlencoded' in self.herders.get('Content-Type'):
            Post_data = urllib.urlencode(self.data)
        elif 'json' in self.herders.get('Content-Type'):
            Post_data = json.dumps(self.data)
        else:
            Post_data = self.data
        try:
           r = requests.post(self.url,data=Post_data,headers=self.herders,cookies=self.cookies,verify=False)
           if r.status_code == 200:
               self.repeson = r
           elif r.status_code in [502, 504]:
               self.repeson = 'Gateway error'
               logging.warning(self.repeson)
           else:
               self.repeson = 'sever is error'
               logging.warning(self.repeson)
        except requests.ConnectionError, e:  # 处理DNS网络问题异常
            print e
        except requests.HTTPError, h:  # 处理无效http响应异常
            print h
        except requests.Timeout, t:  # 处理请求超时异常
            print t

        return self.repeson



















