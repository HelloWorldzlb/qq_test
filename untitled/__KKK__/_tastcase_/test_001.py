#! /usr/bin/python
# -*-coding:utf-8 -*-
from __KKK__._func_.LLLL import foo
from appium import webdriver

#建立连接
a = {
    "device": "android",
    "platformName": "Android",
    "platformVersion": "8.1.0",
    "deviceName": "3634c4cc",
    "appPackage": "com.qk.butterfly",
    "appActivity": ".main.LauncherActivity",
    "noReset": "True"
}
# app 建立连接
dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=a)
foo(dr)
