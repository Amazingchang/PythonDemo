#coding=utf-8
#无序不可重复
a = set([1,2,3])

a.add(4)
a.remove(1      )

#由于set存储的是无序集合，所以没法通过索引来访问
# print a[0]
print 1 in a

for item in a:
    print item