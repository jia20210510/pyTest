"""
@version: python3.8
@project:socketAuto
@file:   conftest.py
@date:   2021/6/4 19:33
@Author: jia
@Desc:  在test_case下创建conftest.py配合pytest.fixture夹具，可使该前置和后置方法在
test_case下的每个文件的每个func都能调用

#conftest.py 文件固定命名，不支持自定义
#conftest.py放在根目录配合pytest.fixture可以当做全局的前置和后置的方法来调用
"""

import pytest


# fixture夹具的params用法
# @pytest.fixture(scope="module",parames=参数化,ids=参数化时的变量名,autouse=自动执行) 默认为func
@pytest.fixture(scope='function', params=['aa', 'bb', 'cc'])
def py_fixture(request):
    # 固定用法返回参数，其它test用方法名调用
    return request.param

# 在每一个func的前后都执行一次，autouse默认为False,scope默认为func
@pytest.fixture(scope="package", autouse=True)
def py_fixture_02():
    print("\n-------**初始化目录**-------")
    yield
    print("\n-------**清除目录**-------")