#!/usr/bin/env python
# coding=utf-8


#count = 0
#pi = 3.14
#name = 'tz'
#print count
#print pi
#print name

#count = 0 
##count += 1
#++count #结果还是0 ，python不支持++，--操作,当作两个+号处理
#count++#语法错误
#print count

#可以在运行过程中修改类型
#动态类型
#a = 10
#a = 'str'
#print a


#a = 10
#b = 3.14
#print type(a)#内建函数
#print type(b)

#数字变量的取值范围上不封顶
#浮点数只有一种float,相当于double
#a = 1000000000000
#b = a ** 1000#**乘方操作
#print b

#My name is 'xiaobuding'
#原字符串是单引号，就用双引号
#a = "My name is 'xiaobuding'"
##原字符串是双引号，就用单引号
#b = 'My name is "xiaobuding"'
#print a
#print b
##既包含单引号又包含双引号就用三引号
#c = '''My "name" is 'xiaobuding'  '''
#d = """My "name" is 'xiaobuding' """
#print c
#print d

#没有字符类型
#a = 'abcd'
#print a[0],a[1],a[2],a[3]
##print a[100]
##允许下标为-
##a[-1] 相当于 len - 1 ==》第三个元素
#print a[-1]
#print a[-2]
#print a[-3]
#print a[-4]
#print a[1:3]#前闭后开区间，切片操作
#print a[0:3]
#print a[:3]
#print a[1:]
#print a[:]
#print a[:-1]
#print a[:100]#能取到多少算多少，不会报错
#print a[2:1]#不存在的区间，空字符串
##print  type(a)
#print type(a[0])

#a = 'hehe'
#b = 'haha'
#print a + b

#mystr = '-'
#print mystr * 20

#a = 'hehe'
#print len(a)

#a = 100
#print "a = %d" % a 格式化字符串
#b = "a = %d" % a
#print b


#C语言也有bool类型C89没有C99有
#a = True
#print a
#print type(a)


#print是一个语句也是一个函数，加上()是函数，不加()是语句
#print('hehe')#尽量写带()为了更好的兼容

#name = raw_input('>')
#raw_input返回的是字符串
#num1 = raw_input('num1:')
#num2 = raw_input('num2:')
#print int(num1) + int(num2)

#传统除法(C语言)
#a = 1
#b = 2
#print a/b

#地板除(向下取整)
#a = 1
#b = 2
#print a // b

#精确除法
#from __future__ import division
#a = 1
#b = 2
#print a / b


#list 列表
#a = [1, 2, 3, 4]#,号后面最好有空格
#print a

#a = [1, 'hehe']
#print a

#支持取下标操作
#print a[2]
#print a[-1]

#通过取下标修改元素
#a[0] = 100
#print a


#tuple元组
#元组中不能修改元素
#不能修改有好多好处
#1.让用户不可以修改的时候
#2.
#3.
#list中的元素可以修改
#a = (1,2,3,4)
#print a
#a = (1,'hehe')
#print a
#print a[0]
#print a[1]

#dict 字典
#a = {'ip':'127.0.0.1','port':80}
#a = {'ip':'127.0.0.1','port':80,}
#print a
#print a['ip']
