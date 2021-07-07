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

import requests
import os
from requests_toolbelt.multipart.encoder import MultipartEncoder

url = "http://192.168.3.52:9010/app/user-info/userFeedback"
headers = {'headInfo': '{"deviceCode":"768831dc21f44033a5c31d5ef3dc3b38","client":"android",'
                       '"token":"4169622bb4a942879b55dd5b0253e9db","apiName":"app/user-info/login",'
                       '"userCode":"e1d31c81a02248488136dff33968b142","odmId":"36ed7e5ae9a442418bfe5acc42fcaf1",'
                       '"odmName":"Home Linking","language":"zh","version":"1.0","time":"202107518"}'}

# file_path = 'C:/Users/hleyf/Pictures/Saved Pictures/scare.jpg'
file_path = 'E:/PycharmProject/pyTest/Data/mm.jpg'
file_name = os.path.split(file_path)[1]
file_type = str(file_name.split('.', 1)[1])

print('file_name:%s,file_type:%s' % (file_name, file_type))

data = MultipartEncoder(
    fields={
       'files': (file_name, open(file_path, 'rb'), 'image/'+file_type),
       "userCode": "e1d31c81a02248488136dff33968b142",
       "content": "这个APP很好用",
    },
    boundary='----WebKitFormBoundaryZR5EZPH1yDBju'
)

# 将这个content-type：加入headers里面，否则上传不上去
headers['Content-Type'] = data.content_type
print('headers', str(headers))
print('data', data)
res = requests.post(url=url, data=data, headers=headers)
print(res.status_code)
print(res.text)


