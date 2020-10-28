#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :msg.py
# @Time      :2020/10/26 21:14
# @Author    :xxf
 
from config.config import HOST
import requests
from lib.apiLib.login import Login
# 1 封装类
class Msg:
    # 1-增加留言
    def add_msg(self,inToken,inData):
        '''
        :param inToken:
        :param inData:
        :return:
        '''
        url = f'{HOST}/api/message'
        # 请求头 token
        header = {'X-AUTH-TOKEN':inToken,'Content-Type':'application/json'}
        payload = inData;
        resp = requests.post(url,json=payload,headers=header);
        return resp.json()

if __name__ == '__main__':
    #1 登录
    testData= {'username': '20154084', 'password': '123456'}
    token = Login().login(testData,getToken=True)
    # 2 增加留言
    info = {
        "title":"留言标题",
        "content":'留言内容'
    }
    res = Msg().add_msg(token,info)
    print(res)