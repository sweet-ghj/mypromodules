"""
===============================
author: ghj
Time: 2020/6/17 11:38
Project: 数据库编程
File: main_with_testrunner.py
================================
"""
# -_- coding=utf-8 -_-
from HTMLTestRunnerNew import HTMLTestRunner
from BeautifulReport import BeautifulReport
import unittest
import os

case_dir = os.path.dirname(os.path.abspath(__file__))
s = unittest.TestLoader().discover(case_dir)
# br = BeautifulReport(s)
# br.report("register module unittest report", "beautifulreport.html")
with open("testrunner.report.html", "wb") as fs:
    print("开始生成html")
    runner = HTMLTestRunner(fs, title="register module unittest Test Report", tester='ghj')
    runner.run(s)
