#coding=utf-8
#key不能重复,无序

d = {'name':'changjie'}

#新增元素
d['age'] = 24
d['age'] = 25

print d
print d['name']
print d.get('age')
print len(d)
print d.keys()
print d.values()

if 'a' in d:
    print d['age']
else:
    print "不在字典"

for index in enumerate(d):
    print index
#迭代key
for item in d:
    print item
for index in d.keys():
    print index
for item in d.iterkeys():
    print item

#迭代value
# 1. values() 方法实际上把一个 dict 转换成了包含 value 的list
# 2. itervalues() 方法不会转换，它会在迭代过程中依次从 dict 中取出 value，所以 itervalues() 方法比 values() 方法节省了生成 list 所需的内存
for item in d.values():
    print item
for item in d.itervalues():
    print item

#迭代key,value
for key,value in d.items():
    print key,value
for key,value in d.iteritems():
    print key,value








