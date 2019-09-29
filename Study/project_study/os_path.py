# -*- coding: utf-8 -*-
import os
#basename(),返回路径的基名
path_basename = os.path.basename(os.path.realpath('/user/lib/bin'))
print(path_basename)

#将路径分割成两部分(head, tail),head是路径除最后一个文件名外的前面部分，tail是路径的最后一个文件名，当path值以“ /”结尾时，tail为空
path_split = os.path.split(os.path.realpath('/user/lib/bin'))
print(path_split)

#将文件名组合成一个完整的路径
path_join = os.path.realpath(os.path.join('user','lib','bin'))
print(path_join)

#返回文件的真实路径
path_realpath = os.path.realpath('/user/lib/bin')
print(path_realpath)

#返回目录名
path_dirname = os.path.dirname('/user/lib/bin')
print(path_dirname)