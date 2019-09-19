# -*- coding: utf-8 -*-
# 统计员工信息和工资
'''
成员变量，可以在类中不同的方法间来回调用
'''

class Test():
    s = "我是一个类变量，嘎嘎"

    def __init__(self):
        print("构造方法就是初始化，来一下")
        self.a = 1
        self.b = 28

    def __del__(self):
        print("析构方法就是后期收拾残局的，我来")

    def foo(self):
        print("方法内普通成员")

    @staticmethod
    def baba():
        print("类的静态方法，我可以被类名直接调用哦，来来")

t = Test() #创建一个对象，对象啊对象
'''
思路
init和del在类中仅且执行一次，init是初始化（先勤部队） del是收拾残局（后勤部队）
不管是几个方法的调用都会执行下init和del
'''
t.foo()
Test.baba()
print(Test.s)
print(t.s)


