#! /usr/bin/python
# -*-coding:utf-8 -*-
from appium import webdriver
from time import sleep
import unittest



a = {
    "device": "android",
    "platformName": "Android",
    "platformVersion": "8.1.0",
    "deviceName": "3634c4cc",
    "appPackage": "com.qk.butterfly",
    "appActivity": ".main.LauncherActivity",
    "noReset": "True"
}

dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=a)
sleep(2.0)

###选择密码登录
dr.find_element_by_id('com.qk.butterfly:id/v_login_pwd').click()
sleep(2.0)

###选择账号输入框并输入账号
dr.find_element_by_id('com.qk.butterfly:id/et_login_phone').send_keys('123456')
sleep(2.0)

###清空账号并输入新的账号
dr.find_element_by_id('com.qk.butterfly:id/et_login_phone').send_keys('13723233269')
sleep(2.0)

###选择密码输入框并输入密码
dr.find_element_by_id('com.qk.butterfly:id/et_login_pwd').send_keys('zxcvb123')
sleep(2.0)

###点击登录
dr.find_element_by_id('com.qk.butterfly:id/tv_to_login').click()
sleep(2.0)

###将选项以列表形式赋值给 a
a = dr.find_element_by_id('android:id/tabs').find_elements_by_class_name('android.widget.RelativeLayout')
print(a)
sleep(2.0)

####选择 “我的”
a[3].click()
sleep(2.0)

###点击设置
dr.find_element_by_id('com.qk.butterfly:id/v_me_setting').click()
sleep(2.0)

###点击退出登录
dr.find_element_by_id('com.qk.butterfly:id/v_me_grade').click()











































# a = dr.find_element_by_id('android:id/tabs').find_elements_by_class_name('android.widget.RelativeLayout')
# print(a)
#
# a[3].click()
#
# dr.find_element_by_id('com.qk.butterfly:id/v_login_pwd')
# ##选择账号输入框并输入账号
# dr.find_element_by_id('com.qk.butterfly:id/et_login_phone').send_keys('1372323329')
# ##账号错了 清空
# dr.find_element_by_id('com.qk.butterfly:id/et_login_phone').clear()
# ##输入正确的账号
# dr.find_element_by_id('com.qk.butterfly:id/et_login_phone').send_keys('13723233269')
# sleep(3.0)
#
# ####输入密码
# dr.find_element_by_id('com.qk.butterfly:id/et_login_pwd').send_keys('zxcvb123')
# sleep(2.0)
#
# ###点击登录
# dr.find_element_by_id('	com.qk.butterfly:id/tv_to_login').click()





###模拟人工上划
# size = dr.get_window_size()
# x1 = size['width'] * 0.5
# y1 = size['height'] * 0.25
# y2 = size['height'] * 0.75
# for i in range(2):
#     dr.swipe(x1, y2, x1, y1)
# shezhi = dr.find_element_by_id('com.qk.butterfly:id/v_me_setting').click()
# sleep(3.0)
# tuichu = dr.find_element_by_id('com.qk.butterfly:id/v_me_grade').click()



