# _*_ coding:utf-8 _*_
"""
@Coding: utf-8
@Version: python3.8
@Project: pyTest
@File: multipart_encoder.PY
@Date: 2021/7/11 22:03
@Author: jia
@Description: 上传文件的方式
"""

from requests_toolbelt.multipart.encoder import MultipartEncoder
path = 'E:/PycharmProject/pyTest/Data/mm.jpg'
data = MultipartEncoder(
    fields={
        'img': ('scare.jpg', open(path, 'rb'), 'image/jpg'),
        "userCode": "e1d31c81a02248488136dff33968b142",
        "content": "这个APP很好用",
    },
    boundary='----WebKitFormBoundaryZR5EZPH1yDBju'
)