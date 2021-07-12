"""
@version: python3.8
@project: pyTest
@file:   conftest.py
@date:   2021/6/4 19:33
@Author: jia
@Desc:  在test_case下创建conftest.py配合pytest.fixture夹具，可使该前置和后置方法在
test_case下的每个文件的每个func都能调用

#conftest.py 文件固定命名，不支持自定义
#conftest.py放在根目录配合pytest.fixture可以当做全局的前置和后置的方法来调用
"""
import pytest
import requests
import json
import time
import allure
from Config import log
from Common import file_methods

logger = log.log_execute('debug_logger')


# @pytest.fixture(scope="module",parames=参数化,ids=参数化时的变量名,autouse=自动执行) 默认为func
@pytest.fixture(scope='function', params=['aa', 'bb', 'cc'])
def py_fixture(request):
    # 固定用法返回参数，其它test用方法名调用
    return request.param


# 在每一个package的前后都执行一次，autouse默认为False,scope默认为func
@pytest.fixture(scope="package", autouse=True)
def py_fixture_02():
    print("\n-------**初始化目录**-------")
    yield
    print("\n-------**清除目录**-------")


@allure.severity(allure.severity_level.BLOCKER)
@allure.suite('登录模块')
@allure.step('账号登录')
@pytest.fixture(scope='session')
def login_dev():
    """
    ：先使用默认headInfo登录
    ：登录后更新token, userCode, time, headInfo
    ：返回headInfo以供调用
    """
    # 从测试用例取值
    test_data = file_methods.FileMethod.read_yaml('../Data/homelink_case.yaml')
    host = test_data['global_config']['dev_base_url']
    url = host+'/app/user-info/login'
    headers = test_data['global_config']['headers']
    data = test_data['global_config']['login_data']

    # 提取返回值token，userCode
    res = requests.post(url, data=data, headers=headers)
    json_res = json.loads(res.text)
    token = json_res['model']['token']
    userCode = json_res['model']['userCode']

    # headInfo转dic
    json_headInfo = json.loads(headers['headInfo'])
    # 更新headInfo
    json_headInfo['token'] = token
    json_headInfo['userCode'] = userCode
    now_time = time.localtime((time.time()))
    now_format_time = time.strftime('%Y%m%d%H%M', now_time)
    json_headInfo['time'] = now_format_time

    # 更新headers, content-type 默认为 application/x-www-form-urlencoded
    headers['headInfo'] = json.dumps(json_headInfo)

    return userCode, headers




