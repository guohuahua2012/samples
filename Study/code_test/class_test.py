# -*- coding: utf-8 -*-
'''
面向对象
'''
class Test():                    #定义类
    car = "buick"                #类变量，定义在类方法外，可被对象直接调用，具有全局效果
    def __init__(self):          #构造方法
        self.name = 1            #成员变量，可以在类的不同方法调用，也可以由类创建对象进行调用
        print("name=",self.name)

    def say(self):               #类方法必须包含参数self，且为第一个参数
        print("------调用类的say()方法------")
        address = "guiyang"      #方法中的局部变量
        print("address=",address)
        print("myname=",self.name)

        self.address = address   #局部变量可以在类方法间调用

    def cry(self):
        print("-------调用类的cry()方法------")
        print(self.address)      #打印上面局部变量

    @staticmethod                #静态方法可以被类名直接调用
    def fun1():
        print("------调用类的静态方法fun1()-----")
        print("我是静态方法")

a = Test()                       #创建类的实例对象a
print(a.car)                     #打印类变量，对象a直接调用
a.say()
a.cry()
Test.fun1()                      #静态方法的调用，直接用类名进行调用

