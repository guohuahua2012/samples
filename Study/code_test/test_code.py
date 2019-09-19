#-*- coding: utf-8 -*-
print("-->文件句柄的获取，读操作：")

f = open('./无题.txt','r',encoding='utf-8') # 此行作用就是获取文件句柄
d = f.read() #read方法读取文件所有内容
f.close()
print(d)

print('-->例二：')
f = open('./无题.txt','r', encoding='utf-8')
e = f.read(9)  #read方法中索引表示读取字符数
f.close()
print(e)

print("写的操作，写文件的时候，不能调用读方法，读文件的时候，不能调用写的方法")
f = open('python', 'w', encoding='utf-8')
f.write('I must learn python \nbecause, python is importtant \n')
f.write("java is better?")
f.write("maybe")
f.close()

f = open('python', 'a', encoding='utf-8')
f.write("花落又花开")
f.close()

