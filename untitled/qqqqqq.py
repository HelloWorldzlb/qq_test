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
    def test_1(self):
        ww = self.denglu(1593835273,111111)
        ll = ww['code']
        print(ll)
        self.assertEqual(ww['code'],-2)
    def test_2(self):
        ee = self.denglu(2121212212,111111)
        self.assertEqual(ee['code'],0)
if __name__ == '__main__':
    unittest.main()    #删除