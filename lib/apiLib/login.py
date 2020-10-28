#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :login.py
# @Time      :2020/10/26 20:23
# @Author    :xxf
# 1- 完成登录代码的编写  依据接口文档
# 登录接口：http://121.41.14.39:9097/api/loginS  20154084 123456
import pprint

from config.config import HOST
import requests
import hashlib  #加密库
#1 接口地址 -- 参数化
url = f'{HOST}/api/loginS' #字符串
# 2 构建请求
payload = {'username':'20154084','password':'e10adc3949ba59abbe56e057f20f883e'}
# 3 发送请求
'''
data  表单
json 
files
'''
resp = requests.post(url,json=payload)
# pprint.pprint(resp.json())

def get_md5(psw):#md5加密
    md5 = hashlib.md5() #创建MD5对象
    md5.update(psw.encode("UTF-8")) #加密方法
    return md5.hexdigest() #返回加密结果
'''
 封装
  1、获取token
  2、接口自动化
'''
class Login:
    def login(self,inData,getToken = False):
        # 1 接口地址 -- 参数化
        url = f'{HOST}/api/loginS'  # 字符串
        # 2 构建请求
        payload = inData
        payload['password'] = get_md5(payload['password'])
        resp = requests.post(url, json=payload)
        print(resp.json)
        if getToken:
            return resp.json()['token']
        else:
            return resp.json()

if __name__ == '__main__':
    #实例化对象
    testData= {'username': '20154084', 'password': '123456'}
    res = Login().login(testData,getToken=False)
    print(res)