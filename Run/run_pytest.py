#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
@version: python3.8
@project:socketAuto
@file:   run_pytest.py
@date:   2021/6/4 15:11
@Author: jia
@Desc:
run文件夹下配置pytest.ini可以自定义配置参数
pip install -r requirement_plugin.txt 安装所有使用插件
"""

import pytest, os

"""
 # -vs 详细输出；--reruns=2 失败重跑2次；-x 失败停止执行；-maxfail=2 失败2个就停止
 # -k 'xi' 只执行用例名包含字符xi的用例; -n 2 多线程运行
 # -m=smoke or retest 执行两种自定义标记的用例
 # pytest.main(['-vs', '-m=smoke or retest', '--reruns=2'])
 # pytest.main(['-s', '../Case', '--html=../Report/Report.html'])

 # pytest --alluredir ../Temp  先执行命令在此目录收集测试结果 
 
 # https://github.com/allure-framework/allure2/releases,下载后将bin地址放在path
 # os.system('allure generate ../Temp -o ../Report --clean') 
 # ../temp临时json文件目录， ../report最终输出报告的目录
 # 经测试temp不在根目录时，OS.SYSTEM操作时找不到文件

 # [0x7FFDA42FE0A4] ANOMALY: use of REX.w is meaningless (default operand size is 64)
 # 命令行报以上错误时打开注册表“regedit”
 # HKEY_LOCAL_MACHINE/SOFTWARE/TEC/Ocular.3/agent/config.yaml.yml 添加二进制数值
 # hookapi_disins,数值数据: 1
 """

if __name__ == '__main__':
    # 主函数
    # pytest.main(['-s', '../Case/test/test_HomeLink.py'])
    pytest.main(['-s', '../Common/assert.py'])


# if __name__ == '__main__':
#     # 控制台生成测试报告
#     pytest.main(['-s', '../Common/common_data_driven.py'])
#     os.system('allure generate ../Temp -o ../Report/allure_report --clean')

