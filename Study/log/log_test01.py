# -*- coding: utf-8 -*-
import logging

#创建一个logger
logger = logging.getLogger("mylogger")
logger.setLevel(logging.INFO)

#创建一个handler，将log写入文件中
fh = logging.FileHandler('C:/Users/ChunhuaGuo/Desktop/test.txt','a')
fh.setLevel(logging.INFO)

# 在创建一个handler，将log输出在控制台
ch = logging.StreamHandler()
ch.setLevel(logging.CRITICAL)

# 设置输出格式
log_format = "%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s: %(message)s"
formatter = logging.Formatter(log_format)
fh.setFormatter(formatter)
ch.setFormatter(formatter)

#把handler添加到logger里，其实可以理解为汇报给大领导
logger.addHandler(fh)
logger.addHandler(ch)

logger.error("今天天气阴")