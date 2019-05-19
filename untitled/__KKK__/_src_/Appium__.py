#! /usr/bin/python
# -*-coding:utf-8 -*-
from appium import webdriver
from time import sleep

#测试脚本与appium服务器进行连接的参数数据
d ={
   "device": "android",
   "platformName": "Android",
   "platformVersion": "8.1.0",
   "deviceName": "3634c4cc",
   "appPackage": "com.qk.butterfly",
   "appActivity": ".main.LauncherActivity",
   "noReset": "True"
}

#测试脚本是appium服务器与手机建立连接的过程
dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_capabilities=d)
sleep(10.0)

#元素是Id 就使用ID定位
# dr.find_element_by_id('com.qk.butterfly:id/v_login_wx').click()

#获取微信文字
#先定位上一级，在定位下面的元素，class属性
# txt = dr.find_element_by_id('com.qk.butterfly:id/v_login_wx').find_element_by_class_name('android.widget.TextView').text
# print(txt)
# sleep(3.0)
# txt_1 = dr.find_element_by_id('com.qk.butterfly:id/v_login_wb').find_element_by_class_name('android.widget.TextView').text
# print(txt_1)
# sleep(3.0)
# txt_2 = dr.find_element_by_id('com.qk.butterfly:id/v_login_qq').find_element_by_class_name('android.widget.TextView').text
# print(txt_2)
# sleep(3.0)
# txt_3 = dr.find_element_by_id('com.qk.butterfly:id/v_login_pwd').find_element_by_class_name('android.widget.TextView').text
# print(txt_3)
#插入等待时间
# sleep(10.0)

#点击密码
dr.find_element_by_class_name('com.qk.butterfly:id/v_login_pwd').click()

#send_keys()输入的是字符串
#什么时候使用可以使用send_keys?
#1 向手机的输入框内输入数据的时候
#2 clickable  ————》》true
#3 enabled  ————》》true
# 4 foucsable --》 true
dr.find_element_by_id('com.qk.butterfly:id/et_login_phone').send_keys('13723233269') #向账号输入框输入手机号
dr.find_element_by_id('com.qk.butterfly:id/et_login_pwd').send_keys('zxcvb123..+')   #向密码输入框输入密码
dr.find_element_by_id('com.qk.butterfly:id/tv_to_login').click()
sleep(10.0)
#查看登录后的效果

#退出APP，包括后台进程也关掉
dr.quit()






