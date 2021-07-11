# _*_ coding:utf-8 _*_
"""
@Coding: utf-8
@Version: python3.8
@Project: pyTest
@File: send_request.PY
@Date: 2021/7/11 21:16
@Author: jia
@Description: 共用方法：通过解析请求方式， 发送不同请求
"""
import allure
import requests

# 发送请求
@allure.step('发送请求')
def send_request(self):
    if self.last_method == 'GET':
        res = requests.get(self.last_url, params=self.last_data, headers=self.last_headers)
        with allure.step('发送GET请求'):
            pass
        return res

    if self.last_method == 'POST':
        res = requests.post(self.last_url, data=self.last_data, headers=self.last_headers)
        with allure.step('发送POST请求'):
            pass
        return res

    if self.last_method == 'DELETE':
        res = requests.delete(self.last_url, data=self.last_data, headers=self.last_headers)
        return res

    if self.last_method == 'PUT':
        res = requests.put(self.last_url, data=self.last_data, headers=self.last_headers)
        return res
