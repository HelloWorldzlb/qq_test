#! /usr/bin/python
# -*- coding:utf-8 -*-
from selenium import webdriver
import time

dr = webdriver.Firefox()

dr.get('https://i.qq.com/')  ###请求网页
time.sleep(3)

#####  iframe  网页框架
dr.switch_to.frame('login_frame')   ###切换到框架  可以根据ID 或者name切换  ////没有ID，name 就先定位到他，然后赋值给一个变量
time.sleep(3)

# dr.switch_to.parent_frame()          ##########  切换到父框架（上一级的框架）
dr.switch_to.default_content()        ###### 退出框架  ,  ###退出到最初的框架
time.sleep(3)

dr.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[1]/ul/li[1]/a/i').click()
