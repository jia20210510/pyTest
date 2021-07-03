"""
@version: python3.8
@project:socketAuto
@file:   Log.py
@date:   2021/6/2 19:13
@Author: jia
@Desc:  公共日志配置

"""

import os
import logging
import logging.config
import time


def log_execute(loggers):

    """
    定义各类型日志的目录
    """
    local = time.localtime()
    now_time = time.strftime('%Y_%m_%d_%H_%M@', local)
    base_dir = os.getcwd()
    root_path = base_dir[:base_dir.find("pyTest\\") + len("pyTest\\")]
    log_dir = os.path.join(root_path + 'Log/').replace("\\", '/')
    debug_log = os.path.join(log_dir + now_time+'debug.log').replace("\\", '/')
    # email_log = os.path.join(log_dir + now_time+'email.log').replace("\\", '/')
    # db_log = os.path.join(log_dir + now_time+'db.log').replace("\\", '/')
    print('log_dir', log_dir)
    print('debug_log', debug_log)
    """
    目录为空时创建目录
    """
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    log_conf = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "simple": {
                'format': '%(asctime)s [%(filename)s:%(lineno)d] [%(levelname)s]- %(message)s'
            },
            'standard': {
                'format': '%(asctime)s [%(threadName)s:%(thread)d] [%(filename)s:%(lineno)d] [%(levelname)s]- %(message)s'
            },
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "level": "DEBUG",
                "formatter": "simple",
                "stream": "ext://sys.stdout"
            },
            # "email": {
            #     "class": "logging.handlers.RotatingFileHandler",
            #     "level": "DEBUG",
            #     "formatter": "simple",
            #     "filename": email_log,
            #     'mode': 'w+',
            #     "maxBytes": 1024 * 1024 * 10,  # 10 MB
            #     "backupCount": 5,
            #     "encoding": "utf8"
            # },
            # "db": {
            #     "class": "logging.handlers.RotatingFileHandler",
            #     "level": "DEBUG",
            #     "formatter": "simple",
            #     "filename": db_log,
            #     'mode': 'w+',
            #     "maxBytes": 1024 * 1024 * 10,  # 10 MB
            #     "backupCount": 5,
            #     "encoding": "utf8"
            # },
            "file": {
                "class": "logging.handlers.RotatingFileHandler",
                "level": "DEBUG",
                "formatter": "simple",
                "filename": debug_log,
                'mode': 'w+',
                "maxBytes": 1024 * 1024 * 10,  # 10 MB
                "backupCount": 5,
                "encoding": "utf-8"
            }
        },
        "loggers": {
            "console_logger": {
                "level": "DEBUG",
                "handlers": ["console"],
                "propagate": "no"
            },
            # "email_logger": {
            #     "level": "DEBUG",
            #     "handlers": ["console", "email"],
            #     "propagate": "no"
            # },
            # "db_logger": {
            #     "level": "DEBUG",
            #     "handlers": ["console", "db"],
            #     "propagate": "no"
            # },
            "debug_logger": {
                "level": "DEBUG",
                "handlers": ["console", "file"],
                "propagate": "no"
            }
        }
    }

    logging.config.dictConfig(log_conf)
    log_type = logging.getLogger(loggers)
    return log_type

