#coding=utf-8
print "你好";

if True:
    print "True"
    print "aaaa"
else:
    print "False"

print 1,
print 2

str = "Hello World";
print str;
print str[1:7];
print str + " test";
print str * 2;

#list
list = [ 'runoob', 786 , 2.23, 'john', 70.2 ]
print list
print list[1:4]

#元组 不可二次赋值
tuple1 = ('this', 'is', 'tuple', 4)
print tuple1[0]

#字典
dict = {'name': 'john','code':6734, 'dept': 'sales'}
print dict['name']
print dict.keys()
print dict.values()

print type(list) #<type 'list'>

print 20/3  #6
print 20//3 #6
print 20.0/3  #6.66666666667
print 20.0//3 #6.0  返回商的整数部分

print 1 and 2 #2 如果 x 为 False，x and y 返回 False，否则它返回 y 的计算值
print 1 or 2 #1 如果 x 是非 0，它返回 x 的值，否则它返回 y 的计算值
print not(0) #True
print not(1) #False

a = b = c = 1;
a, b, c = 1, 2, "john";
print c;

print r'\(~_~)/ \(~_~)/';

print 11.0 / 4

L = ['Adam', 'Lisa', 'Bart', 'Paul']
L.pop(0);
del L[1];
print L

tuple2 = (range(0,10))
print tuple2

age=20
if age>20:
    print "age>20";
elif age==20:
    print "age=20"
else:
    print "age<20"
print "end"

L = ['Adam', 'Lisa', 'Bart']
for name in L:
    print name;

x=0;
while x<10:
    print x;
    x=x+1;
    if x>5:
        break;

d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59 }

for k,v in d.items():
    print k,':',v;


s = set([1,2,3])
print s
print len(s)

print abs(-1)
print cmp(2,3)
print int(3.14)


def fun1():
    return 1111;
print fun1()

import math
def move(x, y, step, angle):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

x, y = move(100, 100, 60, math.pi / 6)
print x, y
r = move(100, 100, 60, math.pi / 6)
print r

a = range(3)
print a  #[0, 1, 2]
print a[0:2]
