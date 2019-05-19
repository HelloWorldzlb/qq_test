#! /usr/bin/python
# -*-coding:utf-8 -*-


from appium import webdriver
from time import sleep
import unittest
import yaml
# ---
# # 三方登录
# three:
#   wx_id: com.qk.butterfly:id/v_login_wx  # 微信
#   wb_id: com.qk.butterfly:id/v_login_wb  # 微博
#   qq_id: com.qk.butterfly:id/v_login_qq  # qq
#   pd_id: com.qk.butterfly:id/v_login_pwd  # 密码
#
# TextView_class: android.widget.TextVie  # 文本
with open(r'E:\Users\Zlb\PycharmProjects\untitled\__KKK__\_element_\a.yaml', 'r', encoding='utf-8') as fb:
    #a = yaml.load(fb)    使用 yaml 模块的load方法将 yaml 文件中的数据转换成 python 字典格式
    item_data = yaml.load(fb)  # 字典
print(item_data)
print(item_data['three']['wx_id'])

# a = {
#     "device": "android",
#     "platformName": "Android",
#     "platformVersion": "8.1.0",
#     "deviceName": "3634c4cc",
#     "appPackage": "com.qk.butterfly",
#     "appActivity": ".main.LauncherActivity",
#     "noReset": "True"
# }
#
# dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=a)
# def foo(driver):
#     # dr = 'xxx'
#     dr.find_element_by_id('')






