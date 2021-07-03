"""
@version: python3.8
@project:socketAuto
@file:   conftest.py
@date:   2021/6/4 19:33
@Author: jia
@Desc:
conftest.py配合pytest.fixture夹具可使前置和后置方法在不同作用域调用

"""
"""
#conftest.py放在test_case下，test_case每个文件内的test_方法都能调用
# 相当于setup_method,teardown_method

#conftest.py 文件固定命名，不支持自定义

#conftest.py放在根目录配合pytest.fixture可以当做全局的前置和后置的方法来调用
# 相当于setup_class,teardown_class



"""

"""
import pytest


# 在每一个func的前后都auto执行一次，autouse默认为False,scope默认为func
# @pytest.fixture(scope="function", autouse=True)

# parames用法
@pytest.fixture(scope='function', params=['aa', 'bb', 'cc'])
def py_fixture(request):
    # 固定用法
    return request.param
    # print("-------这是一个前置函数相当于setup-------")
    # yield
    # print("-------这是一个后置函数相当于teardown-------")


"""

