"""
===============================
author: ghj
Time: 2020/6/19 15:39
Project: 数据库编程
File: logger_test.py
================================
"""
# -_- coding=utf-8 -_-
import logging

logging.info("这是info 级别的日志操作！")
# logging.debug("这是debug级别的日志操作！")
# logging.warning("这是warning级别的日志操作！")
logger = logging.getLogger("This is my logger clollector!!")
# 输出日志级别
logger.setLevel(logging.INFO)
# 设置日志输出在哪些渠道
handle1 = logging.StreamHandler()
# 设置日志渠道输出内容格式
fmt = '%(asctime)s  %(name)s %(levelname)s %(filename)s %(lineno)d 行:%(message)s '
# fmt = '%(asctime)s %(name)s %(levelname)s'
# fmt = '%Y-%m-%d %H:%M:%S '
formatter = logging.Formatter(fmt)
# 将日志格式绑定到渠道
handle1.setFormatter(formatter)
handle2=logging.FileHandler("my_log.log",encoding="uft-8")
handle2.setFormatter(formatter)
logger.addHandler(handle2)
#将设置好的渠道添加到日志收集器
logger.addHandler(handle1)
logger.info("第一个日志收集器！")
logger.error("debug!!")