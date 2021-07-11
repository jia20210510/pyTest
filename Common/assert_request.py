# _*_ coding:utf-8 _*_
"""
@Coding: utf-8
@Version: python3.8
@Project: pyTest
@File: assert.PY
@Date: 2021/7/8 21:36
@Author: jia
@Description:  接口断言
"""
import allure
import traceback
import json
from Config import log
logger = log.log_execute("debug_logger")


# 断言
@allure.step('断言')
def assert_request(self, resp):
    try:
        expect_result = self.last_validate  # 预期结果
        actual_result = json.loads(resp.text)  # 实际结果

        # 写入日志
        logger.info('--<<' + self.last_title + '>>预期结果：' + str(expect_result))
        logger.info('--<<' + self.last_title + '>>实际结果：' + str(actual_result))

        # 解析validate
        for v_key, v_value in expect_result.items():
            # 如果v_value是一个值，则判断值是否相等.eg:200 == 200
            if not isinstance(v_value, dict):
                assert v_value == actual_result[v_key]
                logger.debug("--<<" + v_key + ">>断言OK--")
            else:
                # 如果v_value是一个字典对象，则继续解析
                for key, value in v_value.items():
                    # 如果value是一个值，则判断值是否相等.eg:userInfo == userInfo
                    if not isinstance(value, dict):
                        assert value == actual_result[v_key][key]
                        logger.debug("---" + key + "断言ok---")
                    else:
                        # 如果value是一个字典对象，则继续解析
                        for k, v in value.items():
                            assert v == actual_result[v_key][key][k]
                            logger.debug("---" + k + "断言ok---")
                        logger.debug("---[" + key + "]断言ok---")
                    logger.debug("--<<" + v_key + ">>断言ok--")
    except Exception:
        logger.error('<<' + self.last_title + '>>执行失败！异常信息：%s' % str(traceback.format_exc()))
        raise
    finally:
        logger.info("--<<"+self.last_title+">>测试结束！\n\n")

