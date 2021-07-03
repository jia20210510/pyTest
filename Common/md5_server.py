"""
@version:  python3.8
@project:  socketAuto
@file:     md5_server.py
@date:     2021/6/8 10:58
@Author:   jia
@Desc:
"""
from flask import Flask, request
import hashlib,json
app = Flask(__name__)


def gen_md5(*args):
    return hashlib.md5("".join(args).encode('utf-8')).hexdigest()


# 自定义post请求，data传参
@app.route('/login', methods=['post'])
def get_token():
    username = request.values.get('username')
    password = request.values.get('password')
    # Temp = time.time()
    # print('Temp:', Temp)
    md5_username = str(gen_md5('13662566067')).upper()
    md5_password = str(gen_md5('666666')).upper()
    md5_token = str(gen_md5(username)).upper()
    # 自定义cookies
    cookie = [{
        'uuid': '2B72EB83-2F4B-BBCB-9FC7-CEB643FE503078438infoc',
        # 'domain': 'ABC.com',
        # 'path': '/',
        # 'Expires': 'session',
        # 'Max-Age': '2022-06-08T07:37:58.000Z'
        },
        {'buvid3': 'B7890AFA-EC2C-4D49-8E01-F0FF882C10FE13432infoc'},
        {'fingerprint': 'ab4665f376b681cd25e114afb0d644fa'}
    ]
    coo = {'uuid':'aaaaaa', 'id':'bbbbb','finger':'cccc'}
    if username == md5_username and password == md5_password:
        print('md5_token:', md5_token)
        return {'status_code': 200, 'message': 'login successfully', 'token': md5_token, 'cookie': coo}
    else:
        return {'error_code': -1, 'message':'login fail'}


# 自定义接口
@app.route('/getUserInfo', methods=['post'])
def get_user_info():
    # json.loads()针对字符串，.load()针对文件
    resp = json.loads(request.get_data())
    userCode = resp['userCode']
    cookies = request.cookies
    print('usercode=', userCode)
    print('cookies=', cookies)
    if userCode == 'e1d31c81a02248488136dff33968b142'and cookies == {'uuid':'aaaaaa', 'id':'bbbbb','finger':'cccc'}:
        return {'status_code': 200}
    else:
        return {'status_code': 403}


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=9999, debug=True)
