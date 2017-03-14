# -*- coding: utf-8 -*-
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
class SendMail:
    def __init__(self,user,pwd,to,filename):
        self.user = user
        self.pwd = pwd
        self.to = to
        self.filename = filename

    def send(self):
        msg = MIMEMultipart()
        msg["Subject"] = "testreport"
        msg["From"]  = self.user
        msg["To"]   = self.to
        part = MIMEText(open(self.filename,'rb').read(),_subtype='html')
        msg.attach(part)
        s = smtplib.SMTP_SSL("smtp.qq.com",465,timeout=30)
        s.login(self.user,self.pwd)
        s.sendmail(self.user,self.to,msg.as_string())
        s.close()



