# -*- coding: utf-8 -*-

import configparser

file_path = '.\cofing.ini'
config = configparser.ConfigParser()
result = config.read(file_path, encoding='utf-8')

class ReadConfig():

    def get_http(self, name):
        value = config.get('HTTP', name)
        return value

    def get_email(self, name):
        value = config.get('EMAIL', name)
        return value


if __name__ == '__main__':
    print("HTTP中的baseurl值为：", ReadConfig().get_http('baseurl'))
    print("EMAIL中的addressee值为：", ReadConfig().get_email('addressee'))
