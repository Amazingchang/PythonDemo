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
