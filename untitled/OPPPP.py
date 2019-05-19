#! /usr/bin/python
# -*-coding:utf-8 -*-
from appium import webdriver
from time import sleep


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

    def tiao_zhuan(self):
        self.dr.find_element_by_id('com.qk.butterfly:id/v_login_pwd').click()

    # 检查那四个文字的函数/方法
    # def check_text(self):
    #
    #     # 获取微信文字
    #     text = self.dr.find_element_by_id('com.qk.butterfly:id/v_login_wx').find_element_by_class_name('android.widget.TextView').text
    #     print(text)
    #     return text

    def lonin(self,phone,password):
        # self.dr.find_element_by_class_name('com.qk.butterfly:id/v_login_pwd').click()
        self.dr.find_element_by_id('com.qk.butterfly:id/et_login_phone').send_keys(phone)  # 向账号输入框输入手机号
        self.dr.find_element_by_id('com.qk.butterfly:id/et_login_pwd').send_keys(password)  # 向密码输入框输入密码
        self.dr.find_element_by_id('com.qk.butterfly:id/tv_to_login').click()
        sleep(10.0)
    # 关闭app的函数
    def close_app(self):
        self.dr.quit()


if __name__ == '__main__':
    go = DS()  # 创建一个DS类的实例，赋值给变量go
    # 调用DS类的方法
    go.tiao_zhuan()  ##跳转页面
    go.lonin('13723233269','zxcvb123..+') ### 执行登录 输入账号，密码
    # go.check_text()
    go.close_app()
