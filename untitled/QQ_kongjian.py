#! /usr/bin/python
# -*- coding:utf-8 -*-
from selenium import webdriver
import time

###############################自动登录QQ空间
dr = webdriver.Firefox()

# dr.get('https://i.qq.com/')
# time.sleep(3)
#
# dr.switch_to_frame('login_frame')
# time.sleep(3)
#
# dr.find_element_by_xpath('//*[@id="switcher_plogin"]').click()
# time.sleep(3)
#
# dr.find_element_by_id('u').send_keys('1248430625')
# time.sleep(2)
#
# dr.find_element_by_id('p').send_keys('zxcvb813955..+')
# time.sleep(3)
#
# dr.find_element_by_xpath('//*[@id="login_button"]').click()  ####点击登录

#####点击退出的时候回弹出框  叫  alert
# dr.find_element_by_xpath('//*[@id="tb_logout"]').click()##定位到退出按键
# time.sleep(3)
# dr.find_element_by_xpath('/html/body/div[3]/div/div/div[1]/div[1]/a[2]/i').click()



dr.get('file:///C:/Users/Zlb/Desktop/abc.html')
time.sleep(3)
dr.find_element_by_xpath('/html/body/input')
#### 将控制器切换到弹出框
ff = dr.switch_to.alert()

print(ff.text)    ####获取alert上的文本
time.sleep(3)

ff.accept()   ###   点击确定

# ff.dismiss()   ####点击取消
















# we = dr.switch_to.alert()  ###切换到 alert 上去 ，自动点击确定
# print(we.text)  ####获取alert上面的文本
# we.accept()     ####点击确定
#







############################









