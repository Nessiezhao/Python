#!/usr/bin/env python
# coding=utf-8

#a和b都是100这个对象的别名（引用）两个id相同
#a = 100
#b = a
#print id(a)
#print id(b)

#两个id不同，python中不是改变同一块地方的值，而是再开一块地方，改变a的指向
#a = 100
#print id(a)
#a = 200
#print id(a)


#count = 0
#while count < 5:
#    print count
#    #pyhton中没有++需要+=1
#    count += 1


#分别打印出1/2/3/4
#不同于C语言的for循环
#a = "1234"
#for c in a:
#    print c

#以下是一个C++代码    
#range based for
#for(auto item : v)

#b = [1,2,3,4]
#for value in b:
#    print value
#
#c = {'a':1,'b':2}
#for key in c:
#    print key,c[key]


#打印0～99
#for i in range(0,100):
#    print i


#只打印偶数，最后一个参数为步长
#for i in range(0,100,2):
#    print i

#打印【0，99】第一个3的倍数
#变量作用域
#for i in range(0,100):
#    if i % 3 == 0:
#        break
#print i
#
#
##打印【0，99】所有3的倍数
#for i in range(0,100):
#    if i % 3 != 0:
#        continue
#    print i


#pass 空语句，Shell中：为空语句


#生成【0，4】每个元素的平方和，放到列表之中
#a = [i * i for i in range(0,5)]
#print a


#生成【0，4】每个奇数元素的平方和，放到列表之中
#a = [i * i for i in range(0,5) if i % 2 == 1]
#print a

#函数定义
#def Add(x,y):
#    return x + y
#调用
#print Add(10,20)
#print Add('hello ','world')



#python 中的函数是一个普通的对象，同名函数之间会覆盖
#后者覆盖前者
#def Func():
#    print 'a'
#
#def Func(a):
#    print 'b'
#Func()#会报错
#Func(10)#打印b


#解包unpack
#def GetPoint():
#    x = 10
#    y = 20
#    return x, y
#
#x, y = GetPoint()
#print x
#print y
#不要x，只要y，x的位置用_代替
#_,y = GetPoint()
#a = GetPoint()
#print type(a)#返回一个元组tuple


#f = open("text.txt")
#
#for line in f:
#    print line,#加上逗号不换行
#
#f.close()
#
#print type(f)  -->file

#import add 
#print add.Add(10,20)

#x, y = 10, 20
#x, y = y, x


#python中true和false是变量不是关键字
#True, False = False, True


#函数类会影响作用域，但是for和if不会影响


#避免前后一个下划线和前后两个下划线
#def Func():
#    print 'hehe'
#
#
#print dir(Func)

#def Func():
#    '这个函数是一 个测试函数'
#    print 'hehe'
#
##print Func.__doc__
#help(Func)


