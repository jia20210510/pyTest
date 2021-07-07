# _*_ coding:utf-8 _*_
"""
@Coding: utf-8
@Version: python3.8
@Project: pyTest
@File: upload_image.PY
@Date: 2021/7/7 23:06
@Author: jia
@Description:
"""
from urllib3 import encode_multipart_formdata
import requests

host = "http://*.*.*.*:80/"
def upload():
    url = "upload/public"
    params = {

    }
    header = {
        "content-type":"application/json"
    }
    data = {

    }

    try:
        filename="pic.jpeg"
        file_path = "/Users/admin/Downloads/pic.jpeg"
        data['file']= (filename, open(file_path,'rb').read())
        encode_data = encode_multipart_formdata(data)
        data = encode_data[0]
        header['Content-Type'] = encode_data[1]
        r = requests.post(url=host + url, headers=header, data=data)
        print(r)
        print("返回值：" + r.text)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    upload()
