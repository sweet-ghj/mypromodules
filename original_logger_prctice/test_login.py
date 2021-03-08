"""
===============================
author: ghj
Time: 2020/6/17 10:23
Project: 数据库编程
File: test_login.py
================================
"""
# -_- coding=utf-8 -_-
import unittest,os
from original_logger_prctice.handle_excel import HandleExcel
from my_ddt import ddt,data
from original_logger_prctice.register import register
from original_logger_prctice.my_logger import logger
file_name = os.path.join(os.path.dirname(os.path.abspath(__file__)), "login_cases_data.xlsx")
exc = HandleExcel(file_name, "login_case")
cases = exc.read_all_datas()
exc.close_excel()

@ddt
class test_register(unittest.TestCase):
    @classmethod
    def setUp(cls):
        print("*" * 10, "用例开始执行", "*" * 10, )

    @classmethod
    def tearDown(cls):
        print("*" * 10, "用例执行结束", "*" * 10)

    @data(*cases)
    def test_login(self, case):
        logger.info("——————开始执行测试用例————————")
        logger.info(f"测试数据为:{case}")
        res = register(case["user"], case["password1"], case["password2"])
        logger.info(f"实际运行结果为{res}")
        try:
            self.assertEqual(case["check"], res)
        # raise
        except AssertionError:
            logger.exception("断言失败，用例不通过！")
        else:
            logger.exception("断言成功，用例通过！")
        logger.info("——————测试用例执行结束————————")
