#coding=utf-8
#key不能重复,无序

d = {'name':'changjie'}

#新增元素
d['age'] = 24
d['age'] = '25'

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

#遍历得到的是key
for item in d:
    print 'key:'+ item +',value:' + d[item]







