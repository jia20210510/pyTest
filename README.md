接口自动化项目

项目介绍：

this project is automatic interface !frame: pytest+allure+jenkins

技术特点：

1.关键字驱动

2.使用yaml文件编辑测试用例

3.allure自动生成测试报告，使用jenkins执行时jenkins自动生成测试报告

页面展示：

![image](https://user-images.githubusercontent.com/83941545/202336674-4918d50c-21cf-4a9b-8aaf-e26ac24eed3e.png)

![image](https://user-images.githubusercontent.com/83941545/202335212-6a14b8a2-7546-4648-a90f-509ed603f9cf.png)


安装环境：

System.version = win10

author = jia

python = 3.8.0

pyTest = 6.2.4

allure = 2.9.43

flask = 2.0.1

html = 3.1.1

环境安装：

pip install -r requirement_plugin.txt 安装所有使用插件

requirement_plugin.txt内容如下：

pytest

pytest-html

pytest-xdist

pytest-ordering

pytest-rerunfailures

allure-pytest


