#coding=utf-8

#函数作为方法参数
def add(x,y,f):
    return f(x)+f(y)
print add(-3,-4,abs)

import math
def add(x,y,f):
    return f(x)+f(y)
print add(9,4,math.sqrt)

