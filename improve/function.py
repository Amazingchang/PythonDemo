#coding=utf-8

#函数作为方法参数
def add(x,y,f):
    return f(x)+f(y)
print add(-3,-4,abs)

import math
def add(x,y,f):
    return f(x)+f(y)
print add(9,4,math.sqrt)

#map()函数，map()函数，可以把一个 list 转换为另一个 list，不改变原有的 list，而是返回一个新的 list
def f(x):
    return x * x
print map(f,[1,2,3,4,5])

def format(s):
    if isinstance(s,str):
        s = s[0].upper()+s[1:].lower()
    return s
print map(format,['adam', 'LISA', 'barT'])

print sum([1,2,3])

#reduce()函数对list的每个元素反复调用函数f，并返回最终结果值
def sum(x,y):
    return x * y
print reduce(sum,[1,2,3,4,5])

#filter()函数 对每个元素进行判断，返回 True或 False，filter()根据判断结果自动过滤掉不符合条件的元素，返回由符合条件元素组成的新list
def old(x):
    return x%2==0
print filter(old,range(0,11))

#sorted()函数可对list进行排序,升序,但 sorted()也是一个高阶函数，
# 它可以接收一个比较函数来实现自定义排序,如果 x 应该排在 y 的前面，返回 -1，如果 x 应该排在 y 的后面，返回 1。如果 x 和 y 相等，返回 0
print sorted([1,3,2,7,4,0])   #[0, 1, 2, 3, 4, 7]
print sorted('changjie')      #['a', 'c', 'e', 'g', 'h', 'i', 'j', 'n']
def sor(x,y):
    if x>y:
        return -1
    elif x==y:
        return 0
    else:
        return 1
print sorted([1,3,2,7,4,0],sor)

def sort(x,y):
    if str(x).upper() < str(y).upper():
        return -1
    elif str(x).upper() == str(y).upper():
        return 0
    else:
        return 1

print sorted(['bob', 'about', 'Zoo', 'Credit'], sort)




