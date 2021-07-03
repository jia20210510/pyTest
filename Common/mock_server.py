#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
@version:  python3.8
@project:  socketAuto
@file:     md5_server.py
@date:     2021/6/8 10:58
@Author:   jia
@Desc:  使用FLASK自定义服务接口

# ctrl+shift+i：查看函数定义
# ctrl+D 复制一行
# shift+ enter  任意地方换行
# ctrl+ ? 注释

"""

from flask import Flask, request

import time, json, hashlib

# 实例化一个WEB服务对象
api = Flask(__name__)


# 生成MD5加密字符串
def gen_md5(*args):
    return hashlib.md5("".join(args).encode('utf-8')).hexdigest()


# 默认为GET方法
@api.route('/')
def home():
    # 支持html格式
    # return "<h1>this is home page....</h1>"
    return "this is home page"

# 自定义'微信购买'服务接口
@api.route('/app/wxpay', methods=['post'])
def wechat_purchase():
    # 获取请求参数中的data
    resp = json.loads(request.get_data())
    # 获取当前时间戳
    timestamp = str(time.time())
    # 转为时间数组
    now_local_time = time.localtime(time.time())
    # 格式化时间
    now_format_time = time.strftime('%Y-%m-%d %H:%M:%S', now_local_time)
    # default data
    body = {
        "status": 200,
        "message": "success",
        "model": {
            "appid": "wx8888888888888888",
            "partnerid": "1900000109",
            "prepayid": "WX1217752501201407033233368018",
            "packageValue": "Sign=WXPay",
            "noncestr": "5K8264ILTKCH16CQ2502SI8ZNMTM67VS",
            "timestamp": "14120000",
            "sign": "C380BEC2BFD727A4B6845133519F3AD6"
        }
    }
    # 根据请求参数动态设置返回值
    body['model']['appid'] = resp['appid']
    body['model']['timestamp'] = timestamp
    body['model']['time'] = now_format_time
    if resp['appid'] == 'wx02a95e2c56e289f7' and resp['userCode'] != "" and resp['orderNo'] != "":
        return body
    elif resp['appid'] == "" or resp['userCode'] == "" or resp['orderNo'] == "":
        return {"code": "5000", "message": "参数错误"}


# 自定义'登录'接口
@api.route('/login', methods=['POST'])
def test_login():
    method = request.method
    # back to bytes类型
    res = request.get_data()
    # print('res: ---', res, type(res))

    # bytes to str
    res_str = str(res, 'utf-8')
    # print('res_str: ---', res_str, type(res_str))

    # str to json
    # res_json = eval(res_str)
    res_json = json.loads(res_str)
    # print('res_json: ---', res_json, type(res_json))
    """
    # json.loads():str转dict;
    # json.dumps():dict转str;
    # json.load(file):将file读取出来
    # json.dump(obj,file):将json信息写入文件
    """

    account = res_json["account"]
    password = res_json['password']
    # print('account:'+account,'password:'+password, sep='------')

    # 服务器MD5加密的账号和密码
    s_account = '031508505A484D20634154E6EE3C0781'
    s_password = 'F379EAF3C831B04DE153469D1BEC345E'
    # 请求参数与服务器一致则返回200
    if password == s_password and account == s_account:
    # if method == 'POST':
        return {
            'status_code': 200,
            'message': 'success',
            'model': {
                'userCode': 'e1d31c81a02248488136dff33968b142',
                'token': 'abc1234'
            }

        }
    else:
        return {'status_code': 10000, 'message': '参数错误'}


# 自定义'查询用户信息'服务接口
@api.route('/getUserInfo', methods=['post'])
def get_user_info():
    res = request.get_data()
    # print('res ---',res, type(res))

    res_str = str(res,'utf-8')
    # print('res_str ---',res_str, type(res_str))

    res_json = eval(res_str)
    # print('res_json ---',res_json, type(res_json))

    server_token = 'abc1234'
    client_token = str(request.headers['token'])
    print('client---', client_token, type(client_token))

    c_userCode = res_json['userCode']
    s_userCode = 'e1d31c81a02248488136dff33968b142'
    # 服务器校验usrCode和token正确则返回200
    if c_userCode == s_userCode and server_token == client_token:
        return {
            'status_code': 200,
            'message': 'success',
            'model': {
                'name': 'jia',
                'areaCode': 'CN',
                'userCode': 'e1d31c81a02248488136dff33968b142',
                'hobby': 'travel and street dance'
            }
        }
    else:
        return {'status_code': 403}


if __name__ == '__main__':
    # 启动服务器,debug=true修改代码后服务器自动刷新
    api.run(host='127.0.0.1', port=9999, debug=True)
