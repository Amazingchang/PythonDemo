#coding=utf-8

a = 21
b = 10
c = 0

c = a + b
print "1 - c 的值为：", c

c = a - b
print "2 - c 的值为：", c

c = a * b
print "3 - c 的值为：", c

c = a / b
print "4 - c 的值为：", c

c = a % b
print "5 - c 的值为：", c

# 修改变量 a 、b 、c
a = 2
b = 3
c = a ** b
print "6 - c 的值为：", c

a = 10
b = 5
c = a // b
print "7 - c 的值为：", c

a = 10
b = 20
list = [1, 2, 3, 4, 5];

if (a in list):
    print "1 - 变量 a 在给定的列表中 list 中"
else:
    print "1 - 变量 a 不在给定的列表中 list 中"

if (b not in list):
    print "2 - 变量 b 不在给定的列表中 list 中"
else:
    print "2 - 变量 b 在给定的列表中 list 中"

# 修改变量 a 的值
a = 2
if (a in list):
    print "3 - 变量 a 在给定的列表中 list 中"
else:
    print "3 - 变量 a 不在给定的列表中 list 中"

a = 20
b = 20

if (a is b):
    print "1 - a 和 b 有相同的标识"
else:
    print "1 - a 和 b 没有相同的标识"

if (a is not b):
    print "2 - a 和 b 没有相同的标识"
else:
    print "2 - a 和 b 有相同的标识"
#  is 用于判断两个变量引用对象是否为同一个， == 用于判断引用变量的值是否相等

a=44445
b=44445
print a is b

if 1:
    print 1;
else:
    print 2;

count = 0
while (count < 9):
    print 'The count is:', count
    count = count + 1

print "Good bye!"


tup1 = (50,);
print tup1[0]

import time;  # 引入time模块

ticks = time.time()
print "当前时间戳为:", ticks

localtime = time.localtime(time.time())
print "本地时间为 :", localtime

localtime = time.asctime( time.localtime(time.time()) )
print "本地时间为 :", localtime

print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

a = "Sat Mar 28 22:24:24 2016"
print time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y"))


def printme( str ):
   "打印传入的字符串到标准显示设备上"
   print str
   return

printme("aaa")

# str = raw_input("请输入：");
# print "你输入的内容是: ", str


