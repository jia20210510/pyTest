# _*_ coding:utf-8 _*_
"""
@Coding: utf-8
@Version: python3.8
@Project: pyTest
@File: assert.PY
@Date: 2021/7/8 21:36
@Author: jia
@Description:
"""
import  json
from Common import file_methods
test_data = file_methods.FileMethod.read_yaml('E:/PycharmProject/pyTest/Data/homelink_case.yaml')
case = test_data['test_case']
validate = case[0][6]['validate']
actual_result = {
    'status': 200,
    'message': 'success',
    'model': {
        'userInfo': {'id': 1, 'onlyCode': None, 'odmId': 1, 'odmName': '蓝禾', 'registerType': 1,'registerPlatform': 1,
                     'userName': 'admin', 'password': '123456', 'firstName': 'A', 'nickName': None,
                     'phone': '15814551704','email': '15814551704@163.com', 'sex': 1,
                     'headImage': 'http://oyolyj6wn.bkt.clouddn.com/1ccf62b7-2fa0-4b06-b5a9-aeafacb1c9f7.png',
                     'country': '中国', 'province': '广东省', 'city': '深圳市', 'area': '宝安区', 'hobby': '运动',
                     'hxId': '1', 'hxAccount': '123456', 'isOnLine': 1, 'mesReceive': 1, 'mesPanel': 1, 'language': 1,
                     'status': 1, 'lastAccessTime': 1519544274000, 'createTime': 1519544274000}}}
print('validate-->',validate, type(validate))
key = validate.keys()
va_key = []
for k in key:
    va_key.append(k)
# print(va_key)


for i in va_key:
    # print('validate.i--->',validate[i])
    # print('actual.i-->', actual_result[i])
    if isinstance(validate[i],dict):
        for key, value in validate[i].items():
            if isinstance(value, dict):
                for k ,v in value.items():
                    assert v == actual_result[i][key][k]
                    print('---'+k+'断言OK---')
                print('----------'+i+'['+key+']断言OK----------')
            elif not isinstance(value, dict):
                assert value == actual_result[i][key]
                print('---'+key+'断言OK---')
            else:
                print('---'+key+'断言失败---')
                print(actual_result[i][key])
    elif not isinstance(validate[i], dict):
        assert validate[i] == actual_result[i]
        print('----------'+i+'断言OK----------')
    else:
        print('--'+validate[i]+'断言失败---')

