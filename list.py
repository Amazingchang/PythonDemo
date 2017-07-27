#coding=utf-8
a = []
print a

classmates = ['Michael', 'Bob', 'Tracy']
print classmates
print classmates[0]
print classmates[0:3]

print classmates[-1]

#append()总是把新的元素添加到 list 的尾部
classmates.append('changjie')

#insert()方法，第一个参数是索引号，第二个参数是待添加的新元素
classmates.insert(0, 'changjie1')

#删除元素,两种方式
classmates.pop(0)
del(classmates[0])

classmates[-1] = 'Chang'

for item in classmates:
    print item

L = ['Adam', 'Lisa', 'Bart', 'Paul']
print L[-2:]
print L[:-2]

for index, name in enumerate(L):
    print index,name
for index in enumerate(L):
    print index

for index in enumerate(L):
    print index[1]

#列表生成式
print [x * x for x in range(1,11)]

print range(1, 100, 2)

print [x * (x+1) for x in range(1,100,2)]
#条件过滤
print [x * x for x in range(1,11) if x % 2 == 0]


def toUppers(L):
    return [ x.upper() for x in L if isinstance(x,str)]

print toUppers(['Hello', 'world', 101])


def toUppers1(L):
    for item in enumerate(L):
        if isinstance(item[1],str):
            L[item[0]] = item[1].upper()
        else:
            L.remove(item[1])
    return L
print toUppers1(['Hello', 'world', 101])

print [x for x in range(100,1000) if x/100 == x%10]
