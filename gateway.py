"""
# -*- coding: utf-8 -*-
# @Time    : 2023/5/3 21:26
# @Author  : garykyang
# @File    : gateway.py
"""


import base64
import hashlib
from crypto.Cipher import AES


def decodeTokcen(token, appsecret, timestamp):

    """"
        :param token: string，从Header x-token获取的值
        :param appsecret: string，TPP系统密钥
        :param timestamp: string，从Header x-timestamp获取的值
        :return plain: string，解密后返回的结果

    """
    # 密钥hash字符串
    hash = hashlib.md5((timestamp+appsecret+timestamp).encode(encoding='UTF-8')).hexdigest()

    # 取hash字符串前16位作为AES解密用的密钥
    secret = hash[0:16]
    # 取hash字符串后16位作为AES解密的IV(向量值)
    iv = hash[-16:]
    # 创建一个AES实例
    cryptor =AES.new(secret, AES.MODE_CBC, iv)
    plain = cryptor.decrypt(base64.b64decode(token)).decode(encoding='UTF-8', errors="ignore")

    return plain.strip()
