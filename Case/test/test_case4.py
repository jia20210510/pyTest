#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
@Coding: utf-8
@Version: python3.8
@Project: pyTest
@File: test_case4.PY
@Date: 2021/6/17 20:03
@Author: jia
@Description:
"""
import os
import logging
import logging.config
import time
local = time.localtime()
now_time = time.strftime('%Y_%m_%d_%H_%M@', local)
base_dir = os.getcwd()
root_path = base_dir[:base_dir.find("pyTest\\") + len("pyTest\\")]
log_dir = os.path.join(root_path + 'Log/').replace("\\", '/')
debug_log = os.path.join(log_dir + now_time + 'debug.log').replace("\\", '/')
# email_log = os.path.join(log_dir + now_time+'email.log').replace("\\", '/')
# db_log = os.path.join(log_dir + now_time+'db.log').replace("\\", '/')
print('log_dir', log_dir)
print('debug_log', debug_log)
