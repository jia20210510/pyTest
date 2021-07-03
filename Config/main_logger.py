"""
@version: python3.8
@project:socketAuto
@file:   main_logger.py
@date:   2021/6/11 14:27
@Author: jia
@Desc:  日志全局配置
"""


import logging
import time, os

# 定义日志文件名
local = time.localtime()
now_time = time.strftime('%Y_%m_%d_%H_%M_%S', local)
log_name = now_time+'.txt'

# 定义日志路径
rel_path = os.path.abspath(__file__)
abs_path = os.path.dirname(rel_path)
join_path = os.path.join(abs_path, "Log", log_name)
log_dir = join_path.replace("\\", '/')

# 实例化一个日志对象
logger = logging.getLogger("MainLogger")
logger.setLevel(level=logging.INFO)

# 定义日志输出到文件的handler类型(文件流),等级,格式
handler = logging.FileHandler(log_dir)
handler.setLevel(logging.INFO)
formatter = logging.Formatter('[%(asctime)s] %(filename)s -- %(funcName)s line:%(lineno)d -- %(message)s')
handler.setFormatter(formatter)

# 定义日志输出到控制台的handler类型(流),等级,格式
console = logging.StreamHandler()
console.setLevel(logging.INFO)
console.setFormatter(formatter)

# 添加两种日志格式到logger
logger.addHandler(handler)
logger.addHandler(console)

logger.info("-----starting  output log !--------")
