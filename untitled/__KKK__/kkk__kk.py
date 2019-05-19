#! /usr/bin/python
# -*-coding:utf-8 -*-
from appium import webdriver
from time import sleep
import unittest
#@classmethod


#####################面向对象#####################
class DS(unittest.TestCase):
    ##测试脚本与appium服务器进行连接的参数数据
    d = {
        "device": "android",
        "platformName": "Android",
        "platformVersion": "8.1.0",
        "deviceName": "3634c4cc",
        "appPackage": "com.qk.butterfly",
        "appActivity": ".main.LauncherActivity",
        "noReset": "True"
    }
    def setUp(self):
        self.dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_capabilities=self.d)

        sleep(5.0)
    ##检查那四个文字的函数/方法
    def test_1(self):
        text = self.dr.find_element_by_id('com.qk.butterfly:id/v_login_wx').find_element_by_class_name('android.widget.TextView').text
        print(text)
        #断言
        self.assertEqual(text,'微信')
    #
    # def tearDown(self):
    #     self.dr.quit()
    def tearDown(self):
        self.dr.quit()
if __name__ == '__main__':
    unittest.main()

    def close_app(self):  #####关闭APP的函数
        self.dr.quit()

if __name__ == '__main__':
    go = DS()    #创建一个DS类的实例，赋值给变量go
    go.check_test()   ##调用DS类的方法
    go.close_app()































