"""
@Coding: utf-8
@Version: python3.7.7
@Project: pyTest
@File: test_case1.PY
@Date: 2021/6/4 1:17
@Author: jia
@Description: pyTest基本用法
"""

import pytest
import allure
from allure_commons.types import LinkType

"""
    # 模块名以test_开头或_test结尾；类名以Test开头；方法名以test开头，可在pytest.ini中自定义

    ****************************************************************************************************
    # pip install pytest-ordering 安装插件后可指定执行顺序
    # pip install pytest-xdist 安装插件用于多线程运行用例
    # pip install pytest-rerunfailures 安装插件用于失败重跑
    # pip install pytest-html       安装插件用于输出报告
    # pip install allure_report-pytest  安装插件美化报告
    # pip install -r requirement_plugin.txt 安装所有使用插件
    # pip install fixture  安装插件做用例的前置和后置
    
    # pytest.main() 第一种主函数方式，不输出print
    # -vs 详细输出；--reruns=2 失败重跑2次；-x 失败停止执行；-maxfail=2 失败2个就停止
    # -k 'xi' 只执行用例名包含字符xi的用例; -n 2 多线程运行
    # -m=smoke or retest 执行两种自定义标记的用例
    
    # pytest.main(['-vs', './Test_Case', '-n=2'])  指定目录以多线程模式执行，详细输出
    # pytest.main(['./Common/test_basic.py：：TestBasic：：test_01']) 目录::类名::方法名
    # pytest.main(['-vs', '-m=smoke or retest', '--reruns=2'])
    # pytest.main(['-s', '../Case', '--html=../Report/Report.html']) 标准报告输出
    
    # pytest --alluredir ../Report/Temp  美化报告输出
    # allure serve allure       测试结束后让测试结果生成报告
    ***************************************************************************************************
    **************************************************************************************************
    # Terminal窗口输入 pytest  第二种命令方式运行所有测试用例，因为在根目录执行
    #pytest -s test_case1.py -n auto  指定模块多线程执行
    #pytest -vs ../Case 指定目录执行
    #pytest --reruns-delay 次数之间的延时（单位：秒）eg: "pytest --reruns 2 --reruns-delay 5"
    **************************************************************************************************
    # [0x7FFDA42FE0A4] ANOMALY: use of REX.w is meaningless (default operand size is 64)
    # 命令行报以上错误时打开注册表“regedit”
    # HKEY_LOCAL_MACHINE/SOFTWARE/TEC/Ocular.3/agent/config.yaml.yml 添加二进制数值
    # hookapi_disins,数值数据: 1
    """
"""
# json.loads():str转dict;
# json.dumps():dict转str;
# json.load(file):将file读取出来
# json.dump(obj,file):将json信息写入文件
# 方法二 body = resp.json(), requests库中json方法
"""

# 多个.py文件只执行一次
def setup_module():
    print('\n------**初始化模块**------')


def teardown_module():
    print('\n-----**清除模块**--------')


class TestCase1:
    # 类中只执行一次
    @classmethod
    def setup_class(cls):
        print('\n-----**初始化类**------')

    @classmethod
    def teardown_class(cls):
        print('\n----**清除类**------')

    def setup_method(self):
        print('\n----**初始化方法**-----')

    def teardown_method(self):
        print('\n----**清除方法**------')

    # 失败重跑
    @pytest.mark.flaky(reruns=2, reruns_delay=2)
    def test_009(self):
        print('\n------test_009------')
        assert 1 == 2

    # 调用conftest.py中的py_fixture方法，实现数据全局共享
    def test_08(self, py_fixture):
        print('----test_08，调用了py_fixture----\n'+str(py_fixture))

    # 自定义标记
    @pytest.mark.retest
    def test_001(self):
        print('\n------test_001------')

    # 自定义标记
    @pytest.mark.smoke
    def test_002(self):
        print('\n------test_002------')

    # 指定顺序
    @pytest.mark.run(order=1)
    def test_003(self):
        print('\n------test_003------')

    # 无条件跳过
    @pytest.mark.skip(reason='暂时跳过，不执行')
    def test_004(self):
        print('\n------test_004------')

    # 参数化装饰器
    @pytest.mark.parametrize('user', [{'user': 'zero'}, {'user': 'charles'}])
    def test_005(self, user):
        print('\n------test_005'+str(user))


class TestCase2:

    def test_001(self):
        print('\n-------TestCase2-test001---------')
        a = "hello"
        assert "h" in a
        # assert not 0
        # assert a != "he"

    def test_002(self):
        print('\n-------TestCase2--test_002---------')
        # hasattr(对象，字符串）：检查对象中是否有属性，有返回true
        assert hasattr(TestCase1, 'test_001')

    @pytest.mark.skip(reason='暂时不执行')
    @pytest.mark.retest
    def test_03(self):
        print('--------TestCase2--执行test_03---------')
        assert 1 == 2

    # pyTest装饰器基本用法
    @pytest.mark.skipif(condition=1 < 2, reason='暂时不执行')
    @pytest.mark.parametrize('arg', ['aa', 'bb', 'cc'])
    def test_004(self, arg):
        print('--------TestCase2--执行test_004---------')
        print(arg)

    @allure.description('allure的第一种描述方法，用来描述，注解，用例的行为')
    def test_description1(self):
        assert 1 == 1

    def test_description2(self):
        """
        allure的第二种描述，用于描述测试的行为
        """
        assert 2 == 2

    @allure.description_html("""
    <h1>allure第三种描述，是一个html页面</h1>
    <img src="https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=1993234373,1554417853&fm=26&gp=0.jpg">
    """)
    def test_description3(self):
        assert 'a' not in 'hello'

    @allure.link('http://127.0.0.1:9999', link_type=LinkType.LINK, name='flask服务')
    def test_link(self):
        print('这是一个链接')

    @allure.issue('https://www.baidu.com/', '百度')
    def test_issue(self):
        print('一个bug的链接')

    # 添加附件
    @allure.step('开始截图并上传至报告')
    def test_attachments(self):
        # 在测试报告中画了一个html页面
        allure.attach('<head></head><body><strong>HTML页面，HelloWorld！</strong> </body>', 'Attach with HTML type',
                      allure.attachment_type.HTML)
        # 添加一个html附件
        # allure.attach.file('./report.html', attachment_type=allure.attachment_type.HTML)
        # 添加一个图片附件
        # allure.attach.file('./demo.jpg', attachment_type=allure.attachment_type.JPG)

    # 传多个参数
    @pytest.mark.debug
    @pytest.fixture()
    def getlogins(self,request):
        param = request.param
        # print(f" 获取用户名: {param['username']} 获取密码：{param['password']}")
        return param

    data = [{"username": "jojo", "password": "123456"},
            {"username": "hanmeimei", "password": "123456"},
            {"username": "lilei", "password": "123456"}]

    # indirect=true时，getlogins才作为函数使用
    @pytest.mark.debug
    @pytest.mark.parametrize("getlogins", data, indirect=False)
    def test_getlogin(self, getlogins):
        print(f"用户名：{getlogins['username']} 密码：{getlogins['password']}")

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