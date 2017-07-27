#coding=utf-8
def f1():
    return 1

print f1()
print abs(-222)
print int('123')
# print int('1.2') 报错
print int(1.2)


import math
def move(x, y, step, angle):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny
r = move(100, 100, 60, math.pi / 6)
print r
print r[0]

#可变参数
def f2(*a):
    return 222
print f2()
print f2(1)
