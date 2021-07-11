# _*_ coding:utf-8 _*_
"""
@version: python3.8
@project:socketAuto
@file:   test_HomeLink.py
@date:   2021/6/16 19:28
@Author: jia
@Desc: test home_linking app
"""
import os
import json
import pytest
import allure
from Config import log
from Common import file_methods
from Common import assert_request
from Common import send_request
from urllib3 import encode_multipart_formdata

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

    # 关于临时文件temp
    def setup_class(self):

        # temp_dir = 'D:/PycharmProjects/socketAuto/Report/temp'
        temp_dir = 'E:/PycharmProject/pyTest/Report/temp'

        # allure报告中的环境配置变量
        en_text = 'baseUrl =  ' + self.base_url + \
                  '\nSystem.version = win10\nauthor = jia\npython = 3.8.0\n' \
                  'pyTest = 6.2.4\nallure = 2.9.43\nflask = 2.0.1\nhtml = 3.1.1'

        # 先清除后写入
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
        files = files['files']
        data = data['data']
        headers = headers['headers']
        validate = validate['validate']

        # 用例名
        if title and isinstance(title, str):
            self.last_title = title
        else:
            logger.debug("title:"+title+",type is"+type(title))

        # 请求地址
        if path and isinstance(path, str):
            self.last_url = self.base_url + path
        else:
            logger.debug("path:"+path+",type is "+type(path))

        # 方法名
        if method and isinstance(method, str):
            self.last_method = method
        else:
            logger.debug("method:"+method+",type is "+type(method))

        # 请求头
        if headers and isinstance(headers, dict):
            # 取默认headInfo
            headInfo = login_dev[1]['headInfo']
            headers['headInfo'] = headInfo
            self.last_headers = headers
        else:
            logger.debug("headers:"+headers+"type is "+str(type(headers)))

        # 文件/图片
        if files and isinstance(files, str):
            self.files = files
        else:
            logger.debug("files:"+str(files)+"type is "+str(type(files)))

        # 参数data
        if 'multipart/form-data' == headers['Content-Type']:

            # 解析文件名和类型
            file_name = os.path.split(files)[1]
            f_type = str(file_name.split('.', 1)[1])

            # files放入data中
            data['files'] = (file_name, open(files, 'rb').read(), 'image/'+f_type)

            # data统一格式化
            encode_data = encode_multipart_formdata(data)

            # 赋值
            self.last_data = encode_data[0]
            self.last_headers['Content-Type'] = encode_data[1]

        elif 'application/x-www-form-urlencoded' == headers['Content-Type']:
            self.last_data = data
        elif 'application/json' == headers['Content-Type']:
            self.last_data = data
        else:
            logger.debug('content-type: '+headers['Content-Type'])

        # 预期结果
        if validate and isinstance(validate, dict):
            self.last_validate = validate
        else:
            logger.debug("validate:"+str(validate)+",type is "+type(validate))

        # 输出各请求参数
        logger.info("测试用例名:    <<" + title + ">>")
        logger.info('请求method:    <<' + method + ">>")
        logger.info("返回userCode:  <<" + login_dev[0]+">>")
        logger.info("请求参数URL:   <<" + self.last_url+">>")
        logger.info('请求参数files: <<' + files + ">>")
        logger.info('请求参数data:' + str(self.last_data)+",type is "+str(type(data)))
        logger.info("预期结果last_validate:\n" + str(validate))
        logger.info('请求参数headers:\n' + json.dumps(self.last_headers)+"\n")

        # 调用封装方法
        assert_request.assert_request(self, send_request.send_request(self))








