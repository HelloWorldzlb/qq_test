#! /usr/bin/python
# -*- coding:utf-8 -*-
from selenium import webdriver
import time

dr = webdriver.Firefox()

dr.get('https://www.douban.com/')  ###请求网页     1  号窗口
time.sleep(3)

dr.find_element_by_xpath('/html/body/div[1]/div[1]/ul/li[1]/a').click()  ## 2 号窗口


### 切换窗口  浏览器本身是无法决定什么时候打开哪一个窗口
   ###浏览器按照窗口打开的顺序给窗口标号----唯一标识这个窗口的字符串

####获取当前窗口的标识（句柄）
print(dr.current_window_handle)

####获取所有窗口的标识（句柄）
qq = dr.window_handles
time.sleep(3)
print(qq)

### 切换窗口
dr.switch_to.window(qq[-1])

print(dr.title)
















