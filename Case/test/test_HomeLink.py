# _*_ coding:utf-8 _*_
"""
@version: python3.8
@project:socketAuto
@file:   test_HomeLink.py
@date:   2021/6/16 19:28
@Author: jia
@Desc: test home_linking app
"""

import json
import traceback
import pytest
import requests
import allure
from Config import log
from Common import file_methods
from requests_toolbelt.multipart.encoder import MultipartEncoder

logger = log.log_execute('debug_logger')
# test_data = file_methods.FileMethod.read_yaml('D:/PycharmProjects/socketAuto/Data/homelink_case.yaml')
test_data = file_methods.FileMethod.read_yaml('E:/PycharmProject/pyTest/Data/homelink_case.yaml')



class TestHomeLink:

    # 初始化参数
    base_url = test_data['global_config']['dev_base_url']
    case = test_data['test_case']
    last_validate = {}
    last_headers = {}
    last_data = {}
    files = {}
    last_url = ''
    last_method = ''
    last_title = ''

    # 清除temp缓存,并重新写入环境配置
    def setup_class(self):
        temp_dir = 'D:/PycharmProjects/socketAuto/Report/temp'
        en_text = 'baseUrl =  ' + self.base_url + '\nSystem.version = win10\nauthor = jia\npython = 3.8.0\n' \
                                                  'pyTest = 6.2.4\nallure = 2.9.43\nflask = 2.0.1\nhtml = 3.1.1'
        file_methods.FileMethod.clean_dir(temp_dir)
        file_methods.FileMethod.write_file(temp_dir + '/environment.properties', en_text)

    # 读取用例
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.step('读取用例{title}')
    @allure.title('用例名:{title}')
    @pytest.mark.parametrize('title,path,method,headers,data,files,validate', case)
    def test_case(self, title, path, method, headers, data, files, validate, login_dev):

        # 实例化
        title = title['name']
        path = path['path']
        method = method['method']
        onlyCode = login_dev[0]

        # 用例名
        if title and isinstance(title, str):
            self.last_title = title
        else:
            print('self.last_title:', self.last_title, type(self.last_title))

        # 路径
        if path and isinstance(path, str):
            self.last_url = self.base_url + path
        else:
            print('self.last_url:', self.last_url, type(self.last_url))

        # 方法
        if method and isinstance(method, str):
            self.last_method = method
        else:
            print('self.last_method:', self.last_method, type(self.last_method))

        # headers
        if headers and isinstance(headers, dict):
            # 取默认headers
            default_headers = login_dev[1]
            print('default_headers--', default_headers, type(default_headers))

            # 向headers添加用例中的请求头
            for key, value in headers['headers'].items():
                default_headers[key] = value
                # self.last_headers = json.dumps(default_headers)
                self.last_headers = default_headers
                print('self.last_headers', self.last_headers, type(self.last_headers))
        else:
            print('self.last_headers:', self.last_headers, type(self.last_headers))

        # 文件/图片
        if files and isinstance(files, dict):
            self.files = files['files']
        else:
            print('self.files--', self.files, type(self.files))

        # 参数
        if 'multipart/form-data' == headers['Content-Type']:
            self.last_data = MultipartEncoder(
                fields={
                    'img': ('scare.jpg', open(self.files, 'rb'), 'image/jpg'),
                    "userCode": "e1d31c81a02248488136dff33968b142",
                    "content": "这个APP很好用",
                },
                boundary='----WebKitFormBoundaryZR5EZPH1yDBju'
            )
            pass
        elif 'application/x-www-form-urlencoded' == headers['Content-Type']:
            self.last_data = data['data']
        else:
            print('self.last_data:', self.last_data, type(self.last_data))
            logger.info('self.last_data: '+str(self.last_data)+', '+str(type(self.last_data)))

        # 预期结果
        if validate and isinstance(validate, dict):
            self.last_validate = validate
            print('self.last_validate[vadidate]', self.last_validate['validate'])
        else:
            print('self.last_validate:', self.last_validate, type(self.last_validate))

        # 输出各请求参数
        logger.debug('请求参数URL->' + self.last_url)
        logger.debug('请求参数method->' + self.last_method)
        logger.debug('请求参数files:\n' + json.dumps(self.files))
        logger.debug('请求参数data:\n' + json.dumps(self.last_data))
        logger.debug('请求参数headers:\n' + json.dumps(self.last_headers))

        # 调用封装方法
        # self.assert_request(self.send_request())

    # 发送不同请求
    @allure.step('发送请求')
    def send_request(self):

        if self.last_method == 'GET':
            res = requests.get(self.last_url, data=self.last_data, headers=self.last_headers)
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

    # 断言
    @allure.step('断言')
    def assert_request(self, resp):
        try:
            logger.info('--<<' + self.last_title + '>>')
            expect_result = self.last_validate['validate']  # 预期结果
            actual_result = json.loads(resp.text)           # 实际结果

            # 写入日志
            logger.debug('--预期结果：' + str(expect_result))
            logger.debug('--实际结果：' + str(actual_result))

            # 根据预期结果断言
            if 'status' and 'message' and 'model' in expect_result:
                # 断言状态码
                assert expect_result['status'] == actual_result['status']
                logger.info('--status--断言OK')

                # 断言消息
                assert expect_result['message'] == actual_result['message']
                logger.info('--message------断言OK')

                # 断言model下每个KEY
                for key, value in expect_result['model'].items():
                    assert key in actual_result['model'].keys()

                    # 如果model下的KEY又是一个列表，则再检查这个列表中的每个KEY
                    if value and isinstance(value, dict):
                        for ke in expect_result['model'][key].keys():
                            assert ke in actual_result['model'][key].keys()
                            logger.info('--model-[ '+key+'][ '+ke+']断言OK-----')
                    else:
                        logger.info('--model-----断言OK')

            # 断言状态码和消息
            elif 'status' and 'message' in expect_result:
                assert expect_result['status'] == actual_result['status']

                logger.info('--status----断言OK')

                assert expect_result['message'] == actual_result['message']

                logger.info('----message------断言OK')

            # 断言状态码
            elif 'status' in expect_result:
                assert expect_result['status'] == actual_result['status']

                logger.info('--status-----断言OK')

            else:
                with allure.step('断言失败'):
                    pass
                logger.info("--该请求没有收到正确返回值--")
        except Exception:
            logger.error(self.last_title + '执行失败！异常信息：%s' % str(traceback.format_exc()))
            raise

