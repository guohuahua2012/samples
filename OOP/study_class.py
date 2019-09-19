#coding=utf-8

'''
author:chunhua
'''

'''
对象的绑定方法
在类中，没有被任何装饰器的方法就是绑定的到对象到的方法，这类方法专门为对象定制
'''
class People1:
    country = 'China'

    def __init__(self, name):
        self.name = name

    def eat(self):
        print("%s is eating--1" %self.name)

people1 = People1('nick')
print(people1.eat())


'''
类的绑定方法
@classmothod修饰的方法是绑定到类的方法。这类方法专门为类定制。通过类名调用绑定到类的方法时，
会将类本身当做参数传递给类方法的第一参数
'''
class People2:
    country = 'China'

    def __init__(self, name):
        self.name = name
    # 绑定到类的方法
    @classmethod
    def eat(cls):
        print("chunhua is eating--2")
# 通过类名调用，绑定到类的方法eat()
People2.eat()

'''
非绑定方法
在类内部使用@staticmethod 修饰的方法，即为非绑定方法。这类方法和普通定义的函数没有区别，
不与类或对象绑定，谁都可以调用，且没有自动传值的效果。
'''
class People3:
    country = 'China'
    def __init__(self, name):
        self.name = name

    @staticmethod
    def eat():
        print('s% is eating--3')
People3.eat()
People3('nick').eat()




