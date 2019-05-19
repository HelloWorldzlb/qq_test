#! /usr/bin/python
# -*-coding:utf-8 -*-
import  os

#获取当前文件的绝对路径
a = os.path.dirname(os.path.abspath(__file__))
print(a)

BASE_DIR = os.path.dirname(os.path.abspath(__file__)) #项目个根目录
print(BASE_DIR)

LOG_DIR = BASE_DIR + '/logs/'                           #日志目录
print(LOG_DIR)

REPORT_DIR = BASE_DIR + '/report/'                      #报告目录

SRC_DIR = BASE_DIR + '/src/'                            #源文件目录

TEST_CASE = BASE_DIR + '/testcase/'                     #测试用例目录

FUNC = BASE_DIR + '/func/'                               #页面方法目录

UNYIL = BASE_DIR + '/until/'                            #公共目录



