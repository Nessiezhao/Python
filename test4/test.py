#!/usr/bin/env python
# coding=utf-8
#a和b顺序相关
#a = 'abcd'
#b = 'dcba'

#a = [1,2,3]
#print 100 in a
#print 100 not in a

#a = 'hehe'
#print 'h' in a  时间复杂度O(n)

#生成新的列表,原列表没有修改
#a = [1,2]
#b = [3,4]
#print a + b
#print a
#print b

#extend修改对象自身
#a = [1,2]
#b = [3,4]
#a.extend(b)
#print a


#10个1，2拼接在一起
#a = [1,2]
#print a * 10
#print 10 * a

#a = [1,2,3,4]
#print a[100]


#[::]最后一个为步长
#隔一个取一个元素
#a = [1,2,3,4,5]
#print a[::2]


#逆序输出
#不改变a
#a = "abcdef"
#print a[::-1]
#print a

#a = 'abcd'
#print len(a)时间复杂度O(1)
#
#b = [1,2,3]
#print len(b)


#a = [1,2,3,4]
#print max(a)

#给定列表，找到指定元素在列表的下标
#def Find(input_list,x):
#    for i in range(0,len(input_list)):
#        if input_list[i] == x:
#            return i
#    return None
#
#def Find(input_list,x):
#    for i, item in enumerate(input_list):#item 为i下标对应的值
#        if item == x:
#            return i
#    return None

#a = [1,2,3]
#b = [4,5,6]
#c = [7,8,9]
#[(1,4,7),(2,5,8),(3,6,9)]
#print zip(a,b,c)

#python中字符串,数字是不可变对象 
#a = 'abcd'
#a[0] = 'f'是错的
#print 'f' + a[1:]


#a = 100
#print 'a = %d' % a

#原始字符串 raw_string
#path = r'D:\project\ke\C'

#a = 1
#print repr(a)
#print type(repr(a))
#
#repr vs str

#a = 1.0/7.0
#print repr(a)解释器，精度更高
#print str(a)


#a = 'hehe'
#print repr(a)
#print str(a)
 
#字符串合并
#a = ['aa','bb']
#print ','.join(a)
#
##字符串切分
#a = 'aa,bb,cc'
#print a.split(',')

#判定字符串的开头结尾
#a = 'hello world'
#print a.startswith('hello')
#print a.endswith('world')


#去除字符串开头和结尾的空白字符（换行，空格，回车，制表符）
#a = '        aaaaa                     \n        '
#print '[%s]' % a.strip()


#左对齐，右对齐，中间对齐
#a = 'hello world'
#print '[%s]' % a.ljust(50)
#print '[%s]' % a.rjust(50)
#print '[%s]' % a.center(50)

#查找子字符串
#a = 'hello world'
#print a.find('world')
#
##替换子字符串
#a = 'hello world'
#print a.replace('world','python')

#判定字符串是纯字母/数字
#a = 'hello world'
#print a.isalpha()

#b = '12345'
#print b.isdigit()

#转换大小写
#a = 'Hello World'
#print a.lower()
#print a.upper()

#追加元素
#修改原对象，不会从生成新对象（append，extend）
#a = [1,2]
#a.append(3)
#a.append([3,4])
#[1,2,[3,4]]
#print a

#a = [1,2]
#a.extend([3,4])
#print a

#a = [1,2,3]
#del a[0]
#print a
#del (a[0])
#print a

#a  =[1,2,3]
#a.pop(0)
#print a

#a = [1,2,3]
#a.remove(1)
#print a

#a = [1,2,3]
#a[0] = 100
#print a

#a = [1,2,3]
#b = [2,3,1]
#print a == b
