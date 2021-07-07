#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
@version: python3.8
@project:socketAuto
@file:   common_data_driven.py
@date:   2021/6/16 19:28
@Author: jia
@Desc:
"""

import json
import traceback
import pytest
import requests
import allure
from Config import log
from Common import file_methods
from allure_commons.types import LinkType

logger = log.log_execute('debug_logger')
# test_data = yaml_methods.YamlMethod.read_yaml('D:/PycharmProjects/socketAuto/Data/yaml88.yaml')
test_data = file_methods.YamlMethod.read_yaml('E:/PycharmProject/pyTest/Data/yaml88.yaml')


@allure.suite('登录模块')
@allure.story('登录功能')
class TestApi:

    # 初始化参数
    last_headers = {}
    base_url = test_data['global_config']['base_url']
    case = test_data['test_login_data']
    files = None
    last_data = {}
    last_validate = {}
    last_url = ''
    last_method = ''
    last_title = ''

    # 读取用例
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.step('读取用例{title}')
    @allure.title('用例名:{title}')
    @pytest.mark.parametrize('title,path,method,headers,data,validate', case)
    def test_case(self, title, path, method, headers, data, validate):

        # 从字典中取值
        title = title['name']
        path = path['path']
        method = method['method']

        # 用例名
        if title and isinstance(title, str):
            self.last_title = title
        else:
            logger.info('self.last_title:', self.last_title, type(self.last_title))

        # 路径
        if path and isinstance(path, str):
            self.last_url = self.base_url + path
        else:
            logger.info('self.last_url:', self.last_url, type(self.last_url))

        # 方法
        if method and isinstance(method, str):
            self.last_method = method
        else:
            logger.info('self.last_method:', self.last_method, type(self.last_method))

        # header
        if headers and isinstance(headers, dict):
            self.last_headers = headers['headers']
        else:
            logger.info('self.last_headers:', self.last_headers, type(self.last_headers))

        # 参数
        if data and isinstance(data, dict):
            self.last_data = data['data']
        else:
            logger.info('self.last_data:', self.last_data, type(self.last_data))

        # 响应
        if validate and isinstance(validate, dict):
            self.last_validate = validate
        else:
            logger.info('self.last_validate:', self.last_validate, type(self.last_validate))

        # print("last_url：%s, last_method: %s" % (self.last_url, self.last_method))
        logger.info('请求参数URL:' + self.last_url + ', method:' + self.last_method)
        logger.info('请求参数data:'+json.dumps(self.last_data) + ', head:' + json.dumps(self.last_headers))

        # 调用封装方法
        self.assert_request(self.send_request())

    # 发送不同请求
    @allure.step('发送请求')
    def send_request(self):

        if self.last_method == 'GET':
            res = requests.get(self.last_url, data=self.last_data, headers=self.last_headers)
            with allure.step('发送GET请求'):
                pass
            return res

        if self.last_method == 'POST':
            res = requests.post(self.last_url, json=self.last_data, headers=self.last_headers)
            with allure.step('发送POST请求'):
                pass
            return res

        if self.last_method == 'DELETE':
            res = requests.delete(self.last_url, data=self.last_data, headers=self.last_headers)
            return res

        if self.last_method == 'PUT':
            res = requests.put(self.last_url, data=self.last_data, headers=self.last_headers)
            return res

    # 断言
    @allure.step('断言')
    def assert_request(self, resp):
        try:
            logger.info('--<<' + self.last_title + '>>')
            expect_result = self.last_validate['validate']  # 预期结果
            actual_result = json.loads(resp.text)  # 实际结果

            # 写入日志
            # print('--预期结果：', expect_result, type(expect_result))
            # print('--实际结果：', actual_result, type(actual_result))
            logger.debug('--预期结果：' + str(expect_result))
            logger.debug('--实际结果：' + str(actual_result))

            # 接口断言
            if 'status_code' and 'message' and 'model' in expect_result:
                assert expect_result['status_code'] == actual_result['status_code']
                logger.info('--status_code--断言OK')

                assert expect_result['message'] == actual_result['message']
                logger.info('--message------断言OK')

                for key, value in expect_result['model'].items():
                    # print(key, value)
                    assert key in actual_result['model'].keys()
                    assert value in expect_result['model'].values()

                    logger.info('--model-----断言OK')

            elif 'status_code' and 'message' in expect_result:
                assert expect_result['status_code'] == actual_result['status_code']

                logger.info('--status_code----断言OK')

                assert expect_result['message'] == actual_result['message']

                logger.info('----message------断言OK')

            elif 'status_code' in expect_result:
                assert expect_result['status_code'] == actual_result['status_code']

                logger.info('--status_code-----断言OK')
            else:
                with allure.step('断言失败'):
                    pass
                logger.info("--该请求没有收到正确返回值--")
        except Exception:
            logger.error(self.last_title + '执行失败！异常信息：%s' % str(traceback.format_exc()))
            raise

    @allure.issue('https://www.baidu.com/', '百度')
    def test_issue(self):
        """
        函数下加注释，相当于allure.description,也是用于在报告中描述测试用例的测试行为
        """
        pass
