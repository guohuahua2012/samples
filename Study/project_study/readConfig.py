# -*- coding: utf-8 -*-

import os
import configparser

class ReadConfig:
    path = os.path.dirname(os.path.realpath(__file__))
    config_path = os.path.join(path, 'config.ini')

    cf = configparser.ConfigParser()
    cf.read(config_path, encoding='utf-8')

    '''
    获取config文件的方法有:
    sections()-------------得到所有的section，并以列表的形式返回
    options()--------------得到该section的所有option
    items(section)---------得到该section的所有键值对
    get(section,option)----得到section中option的值，返回为string类型
    getint(section,option)-得到section中option的值，返回为int类型，还有相应的getboolean()和getfloat() 函数
    '''

    # 定义方法，获取config分组下指定name的值
    def getConfigValue(self, name):
        value = self.cf.get('config', name)
        return value

    # 定义方法，获取cmd分组下指定name的值
    def getEmailValue(self, name):
        value = self.cf.get('email', name)
        return value

    # 定义方法，获取log分组下指定name的值
    def getLogValue(self, name):
        value = self.cf.get('log', name)
        return value

if __name__ == '__main__':
    print(ReadConfig().getConfigValue('platformName'))
    print(ReadConfig().getEmailValue('email_server'))
    print(ReadConfig().getLogValue('log_error'))