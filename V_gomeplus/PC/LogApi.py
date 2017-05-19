# -*- coding: utf-8 -*-
import subprocess

class LogApi:
    def __init__(self):
        pass

    def getdom(self,url):
        cmd = 'phantomjs D:\\phantomjs-2.1.1-windows\\examples\\netsniff.js'+' '+url
        p = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE).stdout
        print p.read()




if __name__ == "__main__":
    L = LogApi()
    L.getdom('http://v.gomeplus.com/v/1536.html')