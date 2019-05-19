#! /usr/bin/python
# -*- coding:utf-8 -*-
import os
import logging
import datetime

# 创建一个日志文件的名字
logs = os.path.join('/Users/oldman/D_sound/src/logs', str(datetime.datetime.now().date()) + ".out")
print(logs)
