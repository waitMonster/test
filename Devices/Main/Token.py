# -*- coding: utf-8 -*-
import time
from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex
#该模块提供生成16位动态token的AEB加密算法和解密算法
class crypt():
    def __init__(self):
        # 当前appname对应的appKey
        #self.key = key
        # 随机向量
        #self.iv = iv
        self.mode = AES.MODE_CBC
        self.BS = AES.block_size
        self.pad = lambda s: s + (self.BS - len(s) % self.BS) * chr(self.BS - len(s) % self.BS)
        self.unpad = lambda s: s[0:-ord(s[-1])]

    def encrypt(self, text,key,iv):#加密算法，HttpUntitlsZ中需要token验证的请求方法通过调用这里生成动态token
        text = self.pad(text)
        self.obj1 = AES.new(key, self.mode, iv)
        self.ciphertext = self.obj1.encrypt(text)
        return b2a_hex(self.ciphertext)

    def decrypt(self, text,key,iv):#解密算法，调用逻辑同加密算法
        self.obj2 = AES.new(key, self.mode, iv)
        plain_text = self.obj2.decrypt(a2b_hex(text))
        return self.unpad(plain_text.rstrip('\0'))

