#! /usr/bin/python
# -*-coding:utf-8 -*-
import requests
import json
import unittest
import requests
import xlrd
import HTMLTestRunner


class qwe(unittest.TestCase):
    def denglu(self,name,passwd):
        url = "http://120.132.8.33:9000/api/Account/LoginByPhone"

        payload = "{\r\n    \"phone\":\"%s\",\r\n    \"password\":\"%s\",\r\n    \"zone\":\"86\",\r\n    \"loginType\":0,\r\n    \"isAuto\":0,\r\n    \"deviceId\":\"ec:89:14:54:93:007\"\r\n}"%(name,passwd)
        headers = {
    'Content-Type': "application/json",
    'PhoneInfo': '{"platform": "iOS","systemVersion": "12.0","phoneModel": "iPhone X"}',
    'AppInfo': '{"version": "2.0.1","buildVersion": "2.0.1.3","type": 0}',
    'Language': "zh_CN",
    'APIVersion': "3.0",
    'cache-control': "no-cache",
    'Postman-Token': "75b2b176-8c1a-4524-93f8-a51073118917"
    }

        response = requests.request("POST", url, data=payload, headers=headers)

        qq = response.json()
        return qq

print(qwe().denglu(1593835273,111111))
#     def test_1(self):
#         ww = self.denglu(1593835273,111111)
#         ll = ww['code']
#         print(ll)
#         self.assertEqual(ww['code'],-2)
#     def test_2(self):
#         ee = self.denglu(2121212212,111111)
#         self.assertEqual(ee['code'],0)
# if __name__ == '__main__':
#     unittest.main()    #删除
    # suit = unittest.TestSuite()                      # 创建一个测试套件
    # suit.addTest(qwe('test_1'))          ###将测试用例添加到测试套件中
    # suit.addTest(qwe('test_2'))          ###下面是第二种方式
    #
    # # suit.addTest(unittest.makeSuite(qwe))  ##将qwe类中所有以test开头的函数添加到测试套件中
    # f = open('abc.html','wb')               #打开一个空文件  必须是以html结尾
    # runner = HTMLTestRunner.HTMLTestRunner(stream=f,title='接口报告',tester='张立博',description='结果如下')   ###定义测试报告的信息  stream是将报告放进某个文件
    # runner.run(suit)                        #####执行套件
    # f.close()