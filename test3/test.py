#!/usr/bin/env python
# coding=utf-8
#a = 10
##print type(a)
#b = type(a)
#print type(b)
#
#
#def Func():
#    print 'hehe'
#
#a = Func()
#print a
#print type(a)


#a = 10
#if a:
#    print 'hehe'
#else:
#    print 'haha'
#
#a = 0
#if a:
#    print 'hehe'
#else:
#    print 'haha'
#
#a = 'aaaa'
#if a:
#    print 'hehe'
#else:
#    print 'haha'
#
#a = ''
#if a:
#    print 'hehe'
#else:
#    print 'haha'
#a = [1,2,3]
#if a:
#    print 'hehe'
#else:
#    print 'haha'
#a = []
#if a:
#    print 'hehe'
#else:
#    print 'haha'

#a = 'hehe'
#b = 'hehe'
#print a == b

#a = 10
#b = 20
#print id(a) == id(b)
#print a is b
#print type(a) == type(b)

#a = 100
#print type(a ** a)


#a,b = divmod(10,3)
#print a
#print b


#import math
#print round(math.pi,3)

#def Func1():
#    def Func2():
#        print 'hehe'
##    Func2()
#    return Func2
#
#a = Func1()
#a()


#def Func(x):
#    print x
#
#Func(10)
#Func('hehe')
#Func([1,2,3])
    


#def Add(x,y):
#    return x + y
#
#print Add(100,200)
#print Add("hehe","haha")
#print Add("hehe",100)#报错


#def Func(x=100):
#    print x
#
#Func()
#Func(200)

#def PrintPoint(x=0, y=0, z=0):
#    print x, y, z
#
#PrintPoint()
#PrintPoint(100)#x =100
#PrintPoint(100,200,300)#x = 100,y = 200,z = 300
#
#PrintPoint(x=100,z=300)

#原链表没有修改
#a = [9,5,2,7]
#print sorted(a)
#print a


#a = [9,5,2,7]
#print sorted(a,reverse=True)

#a = [9,-5,2,7]
#print sorted(a)
#
#def Cmp(x,y):
#    '自定制比较函数，按照绝对值进行排序'
#    if abs(x) < abs(y):
#        return -1
#    elif abs(x) > abs(y):
#        return 1
#    else:
#        return 0
#
#print sorted(a,cmp=Cmp)


#字符串分割：split
#字符串合并：join
#def Log(prefix,*data):
#    print prefix + '\t'.join(data)
#
#
#Log('[WARNING]\t',"100","200","300")


#def Log(prefix,**data):
#    print prefix + '\t'.join(data.values())
#
#Log('[WARNING]\t',ip='192.168.1.1',port=8080)
#日志/错误级别
#python不支持重载，以最后出现的为准
#def Func():
#    print '1'
#
#def Func(x):
#    print '2'


#def Add(x,y):
#    return x + y
#
#print dir(Add)
