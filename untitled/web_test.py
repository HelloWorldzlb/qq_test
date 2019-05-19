#! /usr/bin/python
# -*-coding:utf-8 -*-


#  selenium : web 自动化的测试工具集  版本： selenium 1.0 和2.0差距大   selenium3.0

# selenium1.0 里的工具 ：1：selenium IDE 是嵌入火狐浏览器中的一个插件，实现简单的浏览器操作的录制与回放功能
                        # 2：selenium Grid  ： 是一种自动化的测试辅助工具，可以很方便的同时在多台机器上和异构环境中并行运行多个用例   通过一个主机统一控制用例在不同环境，不同浏览器下运行
                        # 3：selenium RC   ：是selenium的核心工具，支持多种不同的语言编写自动化测试脚本，负责控制浏览器的行为。

# selenium 的优点：开源，免费，多浏览器支持（Firefox，Chrome，IE，Opera，Safari），多平台支持（Linux，Windows，Mac）
                     #多语言支持

# selenium RC ：分为Client Libraries  和 selenium server
# selenium server ：负责控制浏览器的行为，包括3个部分：launcher ， HTTP proxy ， Core

# selenium 1.0 和 2.0 的区别： seleniumRC在浏览器中运行javaScript应用，使用浏览器内置的JavaScript翻译器来翻译和执行自动化脚本

from selenium import webdriver
import time


# dr = webdriver.Firefox()           # 定义要打开的浏览器
# dr.get('https://www.baidu.com')    # 请求网页
# time.sleep(2)
# #  关闭浏览器
# # dr.quit()
#
# print(dr.title)  # 获取网页标题  一般用来做断言 判断请求到的网页的标题是否符合预期结果
#
# time.sleep(2)
#
# print(dr.current_url) # 获取请求的网址
#
# time.sleep(2)
#
# dr.set_window_size(400,400)  # 设置浏览器窗口大小
#
# time.sleep(2)
#
# dr.set_window_position(400,400)  # 设置浏览器窗口的位置
#
# time.sleep(2)

# dr.maximize_window()  # 最大化浏览器窗口

# dr.minimize_window()  # 最小化浏览器窗口
#
#
# dr.back()             # 回到上次打开的页面
#
# time.sleep(2)
#
# dr.forward()          # 前进


################################# 定位 #####################################

dr = webdriver.Firefox()           # 定义要打开的浏览器
# dr.get('https://www.baidu.com')    # 请求网页
dr.get('https://www.ctrip.com')
time.sleep(2)

# 1， id  定位
# dr.find_element_by_id('kw').send_keys('python')

# time.sleep(2)

 # 2，class 为了区分跟python中的class，class_name
 #   单个class定位时 必须保证class的值是唯一的
# dr.find_element_by_class_name('mnav')[0].click()

#   3,  name 通过 name 定位
# dr.find_element_by_name('').click()

#  4, link_text  文本定位   要保证文本的唯一性
# dr.find_element_by_link_text('地图').click()

# 5，partial link text   模糊文本定义  保证文本唯一性
# dr.find_element_by_partial_link_text('hao').click()
# time.sleep(2)

#  6,   tag_name 定位  通过标签页的名称
# dr.find_element_by_tag_name('').click()

#   7， xpath  定位  路径定位
# dr.find_element_by_xpath('/html/body/div[3]/div/div[4]/div[6]/div/div/h3/div/span/div[5]/a').click()

#  8, css  定位
# dr.find_element_by_css_selector('').click()



#  定位之后的动作 ： 1.send_keys() ：输入   2，click()     ：点击   3， clear()：清除   4，text  ：文本




 ###############################  定位一组元素，多个数据 ##############################

# ww = dr.find_elements_by_class_name('mnav')
#
# for  i in ww:
#     print(i.text)


################ 层级定位 ：先定位一个顶层元素，再定位这个元素下面的元素  多用于复杂的定位场景

ww = dr.find_element_by_xpath('//*[@id="searchHotelLevelSelect"]').find_element_by_tag_name('option')

# print(ww)
for i in ww:
    i.click()
    time.sleep(2)










