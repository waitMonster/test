# -*- coding: utf-8 -*-
import codecs, ConfigParser
import urllib2,urllib
import requests
from requests.cookies import RequestsCookieJar
from selenium import webdriver
import os
import datetime
from Devices import fs_datadevices,HttpUntils
from Devices.Conf import Config
import json,unittest
#该模块为创建视频信息，给需要依赖它的接口业务case提供视频ID
class VideoMain:
    def __init__(self,url,params,headers,cookies):
        self.url = url
        self.params = params
        self.headers = headers
        self.cookies = cookies
        self.http = HttpUntils.HttpUntils(self.headers, self.cookies)

    def Creat(self):#请求创建视频的接口，如果成功返回包含视频ID的列表，如果都失败返回一个空列表
        id = []
        for j in range(len(self.params.get('is_published'))):
            creat_params = {}
            creat_params['user_id'] = self.params.get('user_id')[j]
            creat_params['title'] = self.params.get('title')[j]
            creat_params['file_name'] = self.params.get('file_name')[j]
            creat_params['description'] = self.params.get('description')[j]
            creat_params['ratio'] = self.params.get('ratio')[j]
            creat_params['tags'] = self.params.get('tags')[j]
            creat_params['is_published'] = self.params.get('is_published')[j]
            #print type(creat_params)
            repeson = self.http.Post_token(self.url,creat_params)
            #print repeson.content
            if 'error'not in repeson:
                id.append(eval(repeson.content).get('data').get('video_id'))
            else:
                print repeson
        return id

    def H5_GetVideoId(self,url,params):
        video_id = []
        list_params = {}
        list_params['keywords'] = params.get('keywords')[0]
        list_params['page'] = params.get('page')[0]
        list_params['number'] = params.get('number')[0]
        repeson = self.http.Get(url, list_params)
        ID = eval(repeson.content).get('data')
        for j in range(len(ID)):
            id = ID[j].get('video_id')
            video_id.append(id)
        return video_id

