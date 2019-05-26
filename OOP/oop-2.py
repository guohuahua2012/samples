# 继承示例
class Person():
    # 公开 public
    name = "chunhua"
    age = 18
    # 受保护的 protected
    _xiaoming = "huahua"
    # 私有的 private
    __money = 0

    def work(self):
        print("学习python")
        return None

class MySelf(Person):
    name = "myself"        #子类中的成员名与父类中的成员名相同
    my_name = "guochunhua"
    my_age = 20

    def study(self):
        print("我在提升自己")
        return None

my = MySelf()
'''
1.子类一旦继承父类，则可以使用父类中除私有成员外的所有内容
'''
print(my.name)
print(my.age)
print(my._xiaoming)
print(my.work())
# 子类访问父类私有的成员,报错
#print(my.__money)

'''
2.子类继承父类，子类引用父类的成员 id值一致
'''
print(id(my.name))
print(id(MySelf.name))

'''
3.子类中可以定义独有的成员属性和方法
'''
print(my.my_name)
print(my.my_age)
print(my.study())

'''
4.子类中定义的成员和父类成员如果相同，则优先使用子类成员
'''
print(my.name)






