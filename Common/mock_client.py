"""
@version:  python3.8
@project:  socketAuto
@file:     md5_server.py
@date:     2021/6/8 10:58
@Author:   jia
@Desc:  自定义接口

"""
import requests
import hashlib

base_usl = 'http://127.0.0.1:9999'
login_cookie = ''


# 自定义访问主页接口
def home():
    resp = requests.get(base_usl)
    print(resp.text)


# 自定义'微信购买'接口
def wechat_purchase():
    path = '/app/wxpay'
    data = {
        "userCode": "e1d31c81a02248488136dff33968b142",
        "orderNo": "20200806193733269297838",
        "appid": "wx02a95e2c56e289f7"
    }
    data2 = {
        "userCode": "",
        "orderNo": "",
        "appid": ""
    }

    resp = requests.post(base_usl+path, data=data2)
    print(resp.json())


# 自定义'登录'接口
def test_login_md5():
    url = base_usl+'/login'
    # MD5加密
    account = hashlib.md5("13662566067".encode('utf-8')).hexdigest()
    password = hashlib.md5("666666".encode('utf-8')).hexdigest()
    # print(username)
    data = {
        'account': str(account).upper(),
        'password': str(password).upper(),
        'areaCode': 'CN'
    }
    # data请求头是x-wwww-form-urlencode,json请求头是application/json
    resp = requests.post(url, json=data)
    """
    # json.loads():str转dict;
    # json.dumps():dict转str;
    # json.load(file):将file读取出来
    # json.dump(obj,file):将json信息写入文件
    # 方法二 body = resp.json(), requests库中json方法
    """
    # body = json.loads(resp.text)
    body = resp.text
    # login_cookie = body['cookie']
    print('client back to cookie:', login_cookie)
    print('body:', body)


# 自定义'查询用户信息'接口,带COOKIE
def test_user_info():
    url = base_usl+'/getUserInfo'
    # !!! 内部加双引号，外部加单引号，以字符串方式保存，否则解析时bytes-->str---->dict时报错
    userCode = '{"userCode": "e1d31c81a02248488136dff33968b142"}'
    headers = {"token": "abc1234"}
    resp = requests.post(url, data=userCode, headers=headers)
    # print(resp.status_code)
    print('body', resp.text)


if __name__ == '__main__':
    # wechat_purchase()
    test_login_md5()
    # test_user_info()