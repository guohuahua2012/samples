# -*- coding: utf-8 -*-
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

import readConfig

readConfig = readConfig.ReadConfig()

class GetUrlParams(): # 定义一个方法，将从配置文件中读取的进行拼接
    def get_url(self):
        new_url = readConfig.get_http('scheme') + '://' + readConfig.get_http('baseurl') +':' + readConfig.get_http('port') + '/login' + '?'
        return new_url

if __name__ == '__main__':
    print(GetUrlParams().get_url())

