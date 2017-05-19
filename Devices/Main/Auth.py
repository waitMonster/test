# -*- coding: utf-8 -*-
import time
from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex
import hashlib

class MD5:
    def __init__(self):
        self.m = hashlib.md5()

    def get_md5(self,str_key):
        self.m.update(str_key)
        length = len(list(self.m.hexdigest()))
        if length >= 16:
            Reallkey = self.m.hexdigest()[:16]
        else:
            Reallkey = self.m.hexdigest()
        return Reallkey

