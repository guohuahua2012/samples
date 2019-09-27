# -*- coding: utf-8 -*-
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

import json
import unittest
#from common.configHttp import RunMain
#import paramunittest
from geturlParams import GetUrlParams
import urllib.parse
import readExcel

url = GetUrlParams().get_Url()
print(url)