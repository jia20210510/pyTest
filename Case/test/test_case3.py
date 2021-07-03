"""
@version: python3.8
@project:socketAuto
@file:   test_case3.py
@date:   2021/6/4 9:48
@Author: jia
"""
import pytest
"""
pip install -r requirement_plugin.txt 安装文件内的所有插件

pip install fixture  安装插件做用例的前置和后置
@pytest.fixture(scope="module",parames=参数化,ids=参数化时的变量名,autouse=自动执行) 默认为func


pip install allure-pytest  安装插件美化报告


"""


class TestCase3:
    # 调用conftest.py中的py_fixture方法，实现数据全局共享
    def test_08(self, py_fixture):
        print('--------执行test_08---------')
        print('-------'+str(py_fixture))

    @pytest.mark.smoke
    def test_01(self):
        print('-------开始执行test_01-------')

    @pytest.mark.run(order=1)
    def test_02(self):
        print('------test_02-------')

    @pytest.mark.skip(reason='暂时不执行')
    @pytest.mark.retest
    def test_03(self):
        print('--------执行test_03---------')
        assert 1 == 2

    # pyTest装饰器基本用法
    @pytest.mark.skipif(condition=1 < 2, reason='暂时不执行')
    @pytest.mark.parametrize('arg', ['aa', 'bb', 'cc'])
    def test1(self, arg):
        print(arg)

    """
        # 利用YAML文件数据驱动,yaml文件有几条测试用例就会执行几次，YAML相当于一个list数据列表
        # @pytest.mark.parametrize('args', y_info)
        # def test_yaml_driven(self, args):
        #     url = args['api_request']['path']
        #     name = args['api_name']
        #     method = args['api_request']['method']
        #     paramts = args['api_request']['parameters']
        #     validate = args['api_validate']
        #     if method == 'post':
        #         server_resp = requests.post(url, json=paramts)
        #         print('URL:', server_resp.url)
        #         print('TEXT:', server_resp.text)
        #         print("validate:", validate)
        #         print("code:",server_resp.json())
        #         for val in validate:
        #             assert val['eq']['code'] == server_resp.json()['status']
        #     elif method == 'get':
        #         print('请求方法不对')
        #     else:
        #         pass
        """
