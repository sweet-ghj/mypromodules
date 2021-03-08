import logging


class MyLogger(logging.Logger):
    def __init__(self, Name, Level=logging.INFO, file=None):
        # 设置输出渠道、输出级别、输出日志格式
        super().__init__(Name, Level)
        # 设置日志格式
        fmt = '%(asctime)s  %(name)s %(levelname)s %(filename)s(%(lineno)d line):%(message)s '
        formatter = logging.Formatter(fmt)
        # 设置日志输出在哪些渠道
        handle1 = logging.StreamHandler()
        handle1.setFormatter(formatter)
        # 设置渠道自己的输出级别
        handle1.setLevel(Level)
        self.addHandler(handle1)
        if file:
            # 文件渠道
            handle2 = logging.FileHandler(file, encoding="utf-8")
            # 设置渠道自己的输出级别
            handle2.setFormatter(formatter)
            self.addHandler(handle2)

logger = MyLogger("my_py", file="my_logger.log")
if __name__ == '__main__':
    logger = MyLogger("my_py", file="my_logger.log")
    # my_logger = MyLogger("my_py")
    logger.info("测试，我自己封装的日志类！")
