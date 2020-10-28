#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :test_login.py
# @Time      :2020/10/28 20:18
# @Author    :xxf
from tools.ExcelDataCtl import get_excel_data
from lib.apiLib.login import Login
import os #执行命令行
import pytest
# 1-登录的测试类
class TestLogin:
    # 返回值是列表套元组 [{},{}]
    @pytest.mark.parametrize('inBody,expData',get_excel_data('1-登录模块', 'login')) #数据参数化
    def test_login(self,inBody,expData):
        # 2- 调用登录的接口代码
        res = Login().login(inBody)
        #3-预期结果与实际结果对比
        assert res['code'] == expData['code']

if __name__ == '__main__':
    #1- 框架执行后的结果数据 --alluredir
    pytest.main(['test_login.py','-s','--alluredir','../report/temp'])
    # 2- 使用allure应用打开这个结果数据
    # 3- 浏览器访问报告 serve ../report/temp
    os.system('allure serve ../report/temp')
