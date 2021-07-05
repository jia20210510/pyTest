#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
@version: python3.8
@project:socketAuto
@file:   debug.py
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
from Common import file_method

logger =log.log_execute('debug_logger')
# test_data = yaml_methods.YamlMethod.read_yaml('D:/PycharmProjects/socketAuto/data/yaml88.yaml')
test_data = file_method.FilesMethod.read_yaml('E:/PycharmProject/pyTest/Data/yaml88.yaml')


class TestApi:

    last_headers = {}
    base_url = test_data['global_config']['base_url']
    case = test_data['test_login_data']
    files = None
    last_data = {}
    last_validate = {}
    last_url = ''
    last_method = ''
    last_title = ''

    @classmethod
    def setup_class(cls):
        """
        清除报告缓存文件temp
        如果有文件夹不存在就创建，存在就清空！
        :return:
        """
        temp_path = 'E:/PycharmProject/pyTest/Report/temp'
        en_text = 'system = WIN10\npython = 3.8.8\nallure = 2.9.43\npytest = 6.2.4\nhtml = 3.1.1\nrequest = 2.25.1\n' \
                  'flask = 2.0.1\nordering = 0.6\nrerunfailures = 10.0'
        file_method.FilesMethod.clean_dir(temp_path)
        file_method.FilesMethod.write_file(temp_path+'/environment.properties', en_text)

    # 读取用例
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title('用例标题: {title}')
    @pytest.mark.parametrize('title,path,method,headers,data,validate', case)
    def test_case(self, title, path, method, headers, data, validate):

        # 从字典中取值
        title = title['name']
        path = path['path']
        method = method['method']

        if title and isinstance(title, str):
            self.last_title = title
            # print('self.last_title----', self.last_title)
        if path and isinstance(path, str):
            self.last_url = self.base_url+path
        if method and isinstance(method, str):
            self.last_method = method

        if headers and isinstance(headers, dict):
            self.last_headers = headers['headers']

        if data and isinstance(data, dict):
            self.last_data = data['data']
        if validate and isinstance(validate, dict):
            self.last_validate = validate

        print('请求参数：', self.last_url, self.last_method, self.last_data, self.last_headers)

        # 调用封装方法
        self.common_call(self.send_request())

    # 根据传参发送不同请求
    def send_request(self):

        if self.last_method == 'GET':
            res = requests.get(self.last_url, data=self.last_data, headers=self.last_headers)
            return res
        if self.last_method == 'POST':
            res = requests.post(self.last_url, json=self.last_data, headers=self.last_headers)
            return res
        if self.last_method == 'DELETE':
            res = requests.delete(self.last_url, data=self.last_data, headers=self.last_headers)
            return res
        if self.last_method == 'PUT':
            res = requests.put(self.last_url, data=self.last_data, headers=self.last_headers)
            return res

    # 公共接口
    def common_call(self, resp):
        try:
            logger.info('--<<'+self.last_title+'>>')
            expect_result = self.last_validate['validate']  # 预期结果
            actual_result = json.loads(resp.text)           # 实际结果

            # 写入日志
            # print('--预期结果：', expect_result, type(expect_result))
            # print('--实际结果：', actual_result, type(actual_result))
            logger.debug('--预期结果：' + str(expect_result))
            logger.debug('--实际结果：' + str(actual_result))

            # 接口断言
            if 'status_code' and 'message' and 'model' in expect_result:
                assert expect_result['status_code'] == actual_result['status_code']
                print('--第一个断言OK')
                logger.info('--第一个断言OK')

                assert expect_result['message'] == actual_result['message']
                print('--第二个断言OK')
                logger.info('--第二个断言OK')

                for key, value in expect_result['model'].items():
                    # print(key, value)
                    assert key in actual_result['model'].keys()
                    assert value in expect_result['model'].values()
                    print('--第三个断言OK')
                    logger.info('--第三个断言OK')

            elif 'status_code' and 'message' in expect_result:
                assert expect_result['status_code'] == actual_result['status_code']
                print('--第一个断言OK')
                logger.info('--第一个断言OK')

                assert expect_result['message'] == actual_result['message']
                print('--第二个断言OK')
                logger.info('----第二个断言OK')

            elif 'status_code' in expect_result:
                assert expect_result['status_code'] == actual_result['status_code']
                print('--第一个断言OK')
                logger.info('--第一个断言OK')
            else:
                print('--该请求没有收到正确返回值--')
                logger.info("--该请求没有收到正确返回值--")
        except Exception:
            logger.error(self.last_title + '执行失败！异常信息：%s' % str(traceback.format_exc()))
            raise

