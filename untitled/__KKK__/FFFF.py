#! /usr/bin/python
# -*-coding:utf-8 -*-
from appium import webdriver
from time import sleep
import unittest


class DS(object):

    # 测试脚本与appium服务器进行连接的参数数据
    d = {
        "device": "android",
        "platformName": "Android",
        "platformVersion": "8.1.0",
        "deviceName": "3634c4cc",
        "appPackage": "com.qk.butterfly",
        "appActivity": ".main.LauncherActivity",
        "noReset": "True"
    }

    # 建立连接的函数
    def __init__(self):

        self.dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=self.d)
        sleep(10.0)
    #跳转密码登录跳转
    def tiao_zhuan(self):
        self.dr.find_element_by_id('com.qk.butterfly:id/v_login_pwd').click()
        sleep(2.0)

    def login(self,phone,pswd):
        # 向手机账号输入框输入手机号
        self.dr.find_element_by_id('com.qk.butterfly:id/et_login_phone').send_keys(phone)
        # 向手机密码框输入密码
        self.dr.find_element_by_id('com.qk.butterfly:id/et_login_pwd').send_keys(pswd)
        sleep(2.0)

        # 点击登录
        self.dr.find_element_by_id('com.qk.butterfly:id/tv_to_login').click()

        sleep(10.0)

    def test_qqweizi(self):


        text=self.dr.find_element_by_id('com.qk.butterfly:id/v_login_qq').find_element_by_class_name('android.widget.TextView').text
        print(text)
        # self.assertEqual(text,'QQ')
    # 关闭app的函数
    def close_app(self):
        sleep(10.0)
        self.dr.quit()

    ##app退出登录
    def logout(self):
 #       #find_element_by_class_name() 定位一个class属性的元素，要求元素唯一
#         # find_elements_by_class_name()  定位多个class属性的元素，元素是多个
        self.dr.find_element_by_id('android:id/tabs').find_element_by_class_name('android.widget.RelativeLayout')


if __name__ == '__main__':
    go = DS()  # 创建一个DS类的实例，赋值给变量go
    # 调用DS类的方法
    go.tiao_zhuan()
    #执行登录
    go.login('13723233269','zxcvb123..+')
    go.close_app()




