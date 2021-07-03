# _*_ coding:utf-8 _*_
"""
@Coding: utf-8
@Version: python3.8
@Project: pyTest
@File: debug.PY
@Date: 2021/6/21 21:29
@Author: jia
@Description:
"""
import yaml
u = "&userCode e1d31c81a02248488136dff33968b142"


def test_set_state(state):
    file_name = 'E:/PycharmProject/pyTest/Data/debug.yaml'
    with open(file_name) as f:
        doc = yaml.safe_load(f)
    doc['global_config']['userCode'] = state
    with open(file_name, 'w', ) as f:
        yaml.safe_dump(doc, f, default_flow_style=False)




if __name__ == '__main__':
    test_set_state(u)
