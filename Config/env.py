"""
@version: python3.8
@project:socketAuto
@file:   env.py
@date:   2021/7/7 17:24
@Author: jia
@Desc: 主要用于jenkins读取环境变量
"""
import os


class USPRO:
    # 北美生产服
    base_url = 'http://****.ops.com'


class CHPRO:
    # 中国生产服
    base_url = 'http://******/xgusercenter'


class USTEST:
    # 北美测试服
    base_url = 'http://*****.ops.com'


class CHDEV:
    # 中国开发服
    base_url = 'http://*****.ops.com'


# 设置环境，主要是为了后续Jenkins集成，读取环境变量
env = os.getenv('Environment', 'chdev')

if env == "chdev":
    CONFIG = CHDEV
elif env == "ustest":
    CONFIG = USTEST
elif env == "uspro":
    CONFIG = USPRO
elif env == "chpro":
    CONFIG = CHPRO
else:
    CONFIG = CHDEV
