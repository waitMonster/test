# -*- coding: utf-8 -*-
import os, datetime, fs_datadevices, json, httplib, logging, requests, urllib, urllib2, time, codecs
from requests.models import Response
from Main import Token
from binascii import b2a_hex, a2b_hex
from Conf import Config


# 该模块依赖requestes获取接口请求返回体，并处理相关异常和记录日志；实现get，post接口验证请求，包括使用cookies以及token验证
class HttpUntils:
    def __init__(self, headers, cookies):
        self.herders = headers
        self.cookies = cookies
        self.repeson = None
        conf_name = 'token.ini'
        self.con = Config.Config()
        logging.basicConfig(level=logging.DEBUG,
                            format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                            datefmt='%a, %d %b %Y %H:%M:%S',
                            filename='myapp.log',
                            filemode='w')
        #################################################################################################
        # 定义一个StreamHandler，将DEBUG级别或更高的日志信息打印到标准错误，并将其添加到当前的日志处理对象#
        console = logging.StreamHandler()
        console.setLevel(logging.INFO)
        formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
        console.setFormatter(formatter)
        logging.getLogger('').addHandler(console)
        #################################################################################################
        self.appname = {}
        self.key = {}
        self.iv = {}
        ConfigData = self.con.readconfig(conf_name)
        for i in ConfigData.keys():
            self.appname[i] = ConfigData.get(i).get('appname')
            self.key[i] = ConfigData.get(i).get('key')
            self.iv[i] = ConfigData.get(i).get('iv')
        # 当前时间戳
        self.t = Token.crypt()

    def Get_be(self, url, data, params):  # 普通的get请求实现方法
        if 'auth' in data.keys():
            Auth = data.get('auth')
            data_p = urllib.urlencode(data)
            oldAuth = data_p.split('&')[3].split('=')[1]
            get_data = str(data_p).replace(oldAuth, Auth)
        else:
            get_data = urllib.urlencode(data)
        get_url = url + '?' + get_data
        try:
            r = requests.get(get_url, params=params, verify=False)
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

    def Get_cookies(self, url, data):  # 需要cookie验证的get请求实现方法
        if 'auth' in data.keys():
            Auth = data.get('auth')
            data_p = urllib.urlencode(data)
            Data_p = data_p.split('&')
            for i in range(len(Data_p)):
                if 'auth' in Data_p[i]:
                    oldAuth = Data_p[i].split('=')[1]
                else:
                    pass
            get_data = str(data_p).replace(oldAuth, Auth)
        else:
            get_data = urllib.urlencode(data)
        try:
            r = requests.get(url, params=get_data, cookies=self.cookies, verify=False)
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

    def Post_be(self, url, data, params,files):  # 不需要cookies的post请求方法
        if 'auth' in data.keys():
            Auth = data.get('auth')
            data_p = urllib.urlencode(data)
            Data_p = data_p.split('&')
            for i in range(len(Data_p)):
                if 'auth' in Data_p[i]:
                    oldAuth = Data_p[i].split('=')[1]
                else:
                    pass
            post_data = str(data_p).replace(oldAuth, Auth)
        else:
            post_data = urllib.urlencode(data)
        # post_url = url+'?'+post_data
        if 'x-www-form-urlencoded' in self.herders.get('Content-Type'):
            Post_params = urllib.urlencode(params)
        elif 'json' in self.herders.get('Content-Type'):
            Post_params = json.dumps(params)
        else:
            Post_params = params
        try:
            if files:
                r = requests.post(url,params=post_data,files=files,verify=False)
            else:
                r = requests.post(url,data=Post_params,params=post_data,headers=self.herders,verify=False)
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

    def Post_cookies(self, url, data):  # 需要cookies的post请求方法
        if 'x-www-form-urlencoded' in self.herders.get('Content-Type'):
            Post_data = urllib.urlencode(data)
        elif 'json' in self.herders.get('Content-Type'):
            Post_data = json.dumps(data)
        else:
            Post_data = data
        try:
            r = requests.post(url, data=Post_data, headers=self.herders, cookies=self.cookies, verify=False)
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

    def Get_token(self, url, data):
        tamp = int(time.time() * 1000)  # 需要验证token的get请求，每次请求前调用Main.Token中的加密算法生成一个token
        if 'dev' in str(url):  # 定义开发环境生成token所需的appname和appkey
            appname = str(self.appname.get('dev'))
            key = self.key.get('dev')
            iv = self.iv.get('dev')
            rang = str(tamp) + '|' + appname
            token = b2a_hex(iv) + self.t.encrypt(rang, key, iv)
            query_params = urllib.urlencode({'appname': appname, 'token': token})
        elif 'pre' in str(url):  # 定义测试环境生成token所需的appname和appkey
            appname = str(self.appname.get('pre'))
            key = self.key.get('pre')
            iv = self.iv.get('pre')
            rang = str(tamp) + '|' + appname
            token = b2a_hex(iv) + self.t.encrypt(rang, key, iv)
            query_params = urllib.urlencode({'appname': appname, 'token': token})
        else:
            query_params = ''

        get_url = url + '?' + query_params
        if 'auth' in data.keys():
            Auth = data.get('auth')
            data_p = urllib.urlencode(data)
            oldAuth = data_p.split('&')[3].split('=')[1]
            get_data = str(data_p).replace(oldAuth, Auth)
        else:
            get_data = urllib.urlencode(data)
        try:
            r = requests.get(get_url, params=get_data, verify=False)
            if r.status_code == 200:
                self.repeson = r
            elif r.status_code in [502, 504]:
                self.repeson = 'Gateway error'
                logging.warning(self.repeson)
            else:
                repeson = 'sever is error'
                logging.warning(self.repeson)
        except requests.ConnectionError, e:  # 处理DNS网络问题异常
            print e
        except requests.HTTPError, h:  # 处理无效http响应异常
            print h
        except requests.Timeout, t:  # 处理请求超时异常
            print t

        return self.repeson

    def Post_token(self, url, data):
        tamp = int(time.time() * 1000)  # 需要验证token的post请求，每次请求前调用Main.Token中的加密算法生成一个token
        if 'dev' in str(url):  # 定义开发环境生成token所需的appname和appkey
            appname = str(self.appname.get('dev'))
            key = self.key.get('dev')
            iv = self.iv.get('dev')
            rang = str(tamp) + '|' + appname
            token = b2a_hex(iv) + self.t.encrypt(rang, key, iv)
            query_params = urllib.urlencode({'appname': appname, 'token': token})
        elif 'pre' in str(url):  # 定义测试环境生成token所需的appname和appkey
            appname = str(self.appname.get('pre'))
            key = self.key.get('pre')
            iv = self.iv.get('pre')
            rang = str(tamp) + '|' + appname
            token = b2a_hex(iv) + self.t.encrypt(rang, key, iv)
            query_params = urllib.urlencode({'appname': appname, 'token': token})
        else:
            query_params = ''
        # query_params = {'appname': self.appname, 'token': token}
        Post_url = url + '?' + query_params
        if 'x-www-form-urlencoded' in self.herders.get('Content-Type'):
            # keys = self.data.keys()
            # values = self.data.values()
            # for i in range(len(keys)):
            # if not self.data.get(keys[i]):
            # self.data.pop(keys[i])
            # else:
            # continue
            Post_data = urllib.urlencode(data)
            # Post_data = urllib.urlencode(dict(self.data.items()+query_params.items()))
        elif 'json' in self.herders.get('Content-Type'):
            Post_data = json.dumps(data)
        else:
            Post_data = data
        try:
            r = requests.post(Post_url, data=Post_data, headers=self.herders, verify=False)
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
