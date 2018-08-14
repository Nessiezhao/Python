#!/usr/bin/env python
# coding=utf-8
#a = (1,2,3)#元组不可变对象，不可对值进行修改
#a[0] = 100

#元组的不可变，指的是元组中包含的元素的id没有发生变化
#如果元组内部包含的对象是可变对象，这样的内部对象也是可以进行修改的
#a = ([1,2],3)
#print id(a[0])
#a[0][0] = 1000
#print a
#print id(a[0])
#([1000,2],3)


#json格式
#a = {
#        'ip': '127.0.0.1',
#        'port': 8080,
#}
#print a['ip']
#a['aaa'] = 1000
#print a['aaa']
#
#for key in a:
#    print key, a[key]

#a['ip'] = '192.168.0.1'
#print a

#时间复杂度O(1)
#if 'aaa' in a:
#    print a['aaa']
#else:
#    print 'key not found'

#print hash(100)
#print hash('hehe')
#print hash(())
#不可哈希，元素可变
#print hash([])
#print hash({})



#a = {
#        'ip': '127.0.0.1',
#        'port': 8080,
#}
#
#print a.keys()
#print a.values()
#print a.items()

#f 是一个文件对象
#f = open('./test.txt', 'r')
#for line in f:
#    print line,#加上，让print不打空行
#效率比较高，吃的内存更多
#print f.readlines()
#f.close()


#f = open('./test.txt', 'w')
##write和writelines不会自动加\n
##f.write('aaaaa\nbbbbb\nccccc\n')
#f.writelines(['a\n','b\n','c\n'])
#f.close()

#类似于
#scoped_ptr boost
#unique_ptr C++11
#with open('./test.txt','r') as f:
#    for line in f:
#        print line,
#
#print 'read done'

#import os.path
#path = '/home/zhaoyue/text.txt'
#print os.path.basename(path)
#print os.path.dirname(path)
#print os.path.split(path)
#print os.path.splitext(path)

#import os
#
#path = '/home/xiaobuding/Git/Python/test5'
#for basedir, dirnames,filenames in os.walk(path):
#    print basedir
#    print dirnames
#    print filenames
#    print '--------------'


#创建一个.py文件，并且运行这个文件
#import os
#import os.path
#import stat
#if os.path.exists('hello.py'):
#    os.remove('hello.py')
#os.mknod('hello.py')
#f = os.open('hello.py',os.O_RDWR)
#
#os.write(f,'print "hello world"')
#os.close(f)
#os.chmod('hello.py',stat.S_IRUSR | stat.S_IXUSR)
#os.system('python hello.py')

#模拟实现ls
#import os
#import sys
#path = '.'
#if len(sys.argv) > 1:
#    path = sys.argv[1]
#for f in os.listdir(path):
#    print f,

#异常处理
#Print 'hehe'
#a = [1,2,3]
#print a[100]
#open('hehe.py')
#print 'done'

#a = [1,2,3]
#try:
#    print a[100]
##我们捕捉到
##except IndexError as e:
##python解释器捕捉
#except IOError as e:
#    print e
#    print type(e)
#print 'done'
#a = [1,2,3]
#try:
#    print a[100]
#except IndexError as e:
#    print e
#    print type(e)
#except IOError as e:
#    print e
#    print type(e)
#print 'done'


#a = [1,2,3]
#try:
#    print a[100]
#except IndexError as e:
#    print e
#except IOError as e:
#    print e
#else:
#    print 'no except'
##finally辅助回收资源
#finally:
#    print 'finally'
#print 'done'


#a = [1,2,3]
#try:
#    print a[100]
#    print e
#except Exception as e:
#    print e
#else:
#    print 'no except'
#finally:
#    print 'finally'
#print 'done'

#如何抛出异常
#def Divide(x,y):
#    if y == 0:
#        return False
#    return x/y
#print Divide(10,0)
#def Divide(x,y):
#    if y == 0:
#        raise Exception('Divide Zero')
#    return x/y
#try:
#    print Divide(10,0)
#except Exception as e:
#    print e
