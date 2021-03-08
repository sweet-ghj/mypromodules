import logging
from logging import handlers
"""
logging模块

多个渠道可以共享一个日志级别，也可以在日志收集器的日志级别内设置更小的的日志级别
控制台不会输出低于渠道的级别的日志，只会输出高于渠道的级别的日志。
                           -->日志级别(渠道2可以添加日志级别，渠道的日志级别)
              渠道2(Handle)-->日志格式（Formtter）
日志收集器--> (1)渠道1(Handle)-->日志格式（Formtter）
                           -->日志级别(渠道1可以添加日志级别，渠道的日志级别)
              (2)日志级别(日志收集器的日志级别)
日志收集器最重要两点：1.设置渠道(渠道可以不设级别，也可以设置自己的级别) 2.输出日志级别
日志收集器不支持debug,
0、日志收集器
1、日志级别（Level）：DEBUG、INFO、WARNING、ERROR、CRITICAL(FATAL)
2、输出渠道(Handle)：控制台(SteamHandle)、文件(FileHandle)
----在控制台输出日志使用SteamHandle，在文件中输出日志使用FileHandle，用法以及步骤都是一样的
3、日志内容(Format):时间-哪个文件-哪行代码-输出内容

logging模块，默许的root日志收集器。默认的输出级别：WARNING

给日志收集器设置日志级别：logger.setLevel(logging.INFO)

第一步：创建一个日志收集器：logging.getLogger("收集器的名字")

第二步：给日志收集器设置日志级别：logging.getLogger(logging.INFO)

第三步：给日志收集器创建一个输出渠道(实例化一个渠道类)。handle1=logging.StreamHandler()

第四步：给渠道设置一个日志输出内容的格式。(多个渠道可以共享一个日志级别，也可以在日志收集器的日志级别内设置更小的的日志级别)

第五步：将设置的格式，绑定到渠道中。将格式与渠道关联

第六步：将设置好的渠道，添加到日志收集器上。
"""


#info级别的不会在控制台输出
# logging.info("hello,py30,第一次日志输出操作！")
# #日志收集器的名称不设置的话，默认为名叫root
# logging.warning("第一次警告")
logger=logging.getLogger("logger_collector")

#因为源码中日志收集器的默认级别是warning，所以低于日志级别warning级别的不会输出在控制台
#设置日志输出级别为info(info级别的不会在控制台输出)
logger.setLevel(logging.INFO)

#设置日志输出在哪些渠道
handle1=logging.StreamHandler()

#设置渠道输出内容格式
fmt = '%(asctime)s  %(name)s %(levelname)s %(filename)s-(line%(lineno)d):%(message)s '
formatter=logging.Formatter(fmt)

#将日志格式绑定到渠道当中
handle1.setFormatter(formatter)
#设置渠道自己的输出级别
handle1.setLevel(logging.ERROR)

#第六步
#将设置好的渠道，添加到日志收集器中
logger.addHandler(handle1)

#添加渠道filehandle
handle2=logging.FileHandler("my_log1.log",encoding="utf-8")
handle2.setFormatter(formatter)
logger.addHandler(handle2)


logger.info("日志收集器设置成功！！！")
#这里不会输出
logger.debug("debug!!")
logger.error("ERROR出错啦!!")