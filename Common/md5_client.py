"""
@version: python3.8
@project:socketAuto
@file:   md5_client.py
@date:   2021/6/8 10:31
@Author: jia
@Desc:
"""

import hashlib, requests, time, calendar
import pytest, json


class TestMd5:
    login_cookie = ''

    def test_login_md5(self):
        url = 'http://127.0.0.1:9999/login'
        username = hashlib.md5("13662566067".encode('utf-8')).hexdigest()
        password = hashlib.md5("666666".encode('utf-8')).hexdigest()

        data = {
            'username': str(username).upper(),
            'password': str(password).upper()
        }
        # data请求头是x-wwww-form-urlencode,json请求头是application/json
        resp = requests.post(url, data=data)

        body = resp.json()
        # .json是requests库中的方法，json.loads()是python内置方法，都是将str转为dict
        # body = json.loads(resp.text)
        TestMd5.login_cookie = body['cookie']
        # print('client back cookie:', self.login_cookie)
        # print(type, self.login_cookie)

    def test_cookie(self):
        url = 'http://127.0.0.1:9999/getUserInfo'
        userCode = {'userCode': 'e1d31c81a02248488136dff33968b142'}
        resp = requests.post(url, json=userCode, cookies=TestMd5.login_cookie)
        print(resp.status_code)
        print('test_cookie is  cookie:', TestMd5.login_cookie)

    # def gen_time(self):
    #     local = time.localtime()
    #     local2 = time.strftime('%Y-%m-%d', local)
    #     local3 = calendar.month(2021,6)
    #     local4 = time.strptime('20220608', '%Y%m%d')
    #     print(local4)


if __name__ == '__main__':
    pytest.main(['-vs', 'md5_client.py'])
